#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from module.dao import BillDictDataDao, BillDetDao
from module.entity import CrudRSModel, QueryBillModel, BillDictDataModel, CrudDataRSModel

import datetime
import pandas as pd
from utils.utils import query_to_dict
import re
from utils.log import logger
import traceback

class BillDictService:
    """
    账单字典类型管理模块服务
    """
    @classmethod
    def check_code_item_exist_data(cls, result_db: Session, theme_id:int, dict_id_base:str, code_key:str):
        """
        判断某条码值下是否存在账单
        """        
        key_map = {'BD001':'bill_name', 'BD002':'pay_channel', 'BD003':'settle_channel', 'BD004':'consume_object', 'BD005':'bill_scene'}
        

        target_method = 'eq'
        if dict_id_base in ['BD001', 'BD001','BD003']:
            if len(re.findall(r'\d+', code_key)) <= 0:
                target_method = 'like'

        res = BillDetDao.query_bills_by_code_key(result_db, 
                                                 theme_id=theme_id, 
                                                 target_field=key_map[dict_id_base], 
                                                 target_value=code_key, 
                                                 target_method=target_method
                                                 )
        
        return True if res else False
        

    @classmethod
    def get_dict_codes_list_by_theme_id(cls, result_db: Session, theme_id:int):
        """
        获取某账单主题下的所有字典列表数据，通过账单主题ID查询
        """           
        try:
            data = pd.DataFrame([query_to_dict(f) for f in BillDictDataDao.query_dict_list_by_theme_id(db=result_db, theme_id=theme_id)])
            data = data[['dict_id_base', 'dict_cn_name', 'dict_en_name', 'code_key', 'father_key', 'level', 'code_sort',
                        'code_value', 'icon', 'icon_color', 'icon_css', 'is_default', 'status']]
            if len(data) > 0:
                result = dict(is_success=True, message='查询成功', data=data.to_dict('records'))
            else:
                result = dict(is_success=False, message='未查询到数据', data=[])

        except:
            logger.error(traceback.format_exc())
            result =  dict(is_success=False, message='数据库操作异常', data=[])

        return CrudDataRSModel(**result)


    @classmethod
    def get_code_info_by_key(cls, result_db: Session, theme_id: int, dict_id_base:str, code_key:str):
        """
        通过账单账单主题编号、码表编号、码键，获取主题ID查询获取码值项信息
        """  
        try:
            code = BillDictDataDao.query_code_info_by_key(db=result_db, theme_id=theme_id, dict_id_base=dict_id_base, code_key=code_key)
            if code:
                result = dict(is_success=True, message='查询成功', data=query_to_dict(code))
            else:
                result = dict(is_success=False, message='未查询到码值', data={})
        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, message='数据库操作异常', data={})
        return CrudDataRSModel(**result)


    @classmethod
    def get_code_info_by_id(cls, result_db: Session, code_id:int):
        """
        通过码值ID，获取码值项详情
        """
        try:
            code = BillDictDataDao.query_code_info_by_code_id(result_db, code_id=code_id)
            if code:
                result = dict(is_success=True, message='查询成功', data=query_to_dict(code))
            else:
                result = dict(is_success=False, message='未查询到码值', data={})
        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, message='数据库操作异常', data={})
        return CrudDataRSModel(**result)


    @classmethod
    async def init_new_theme_bill_dict_data(self, result_db: Session, theme_id:int, user_id:str):
        """
        初始化账单主题的码值数据
        """
        is_exist = BillDictDataDao.query_dict_list_by_theme_id(db=result_db, theme_id=theme_id)
        if is_exist:
            return CrudRSModel(is_success=False, message='初始化失败，该主题已经存在')

        base_data = pd.DataFrame([query_to_dict(f) for f in BillDictDataDao.query_base_dict_data(result_db)])
        base_info = pd.DataFrame([query_to_dict(f) for f in BillDictDataDao.query_base_dict_info(result_db)])
        n_cur = BillDictDataDao.query_max_code_id(result_db)

        data = (
            base_data
                .merge(base_info[['dict_id', 'dict_cn_name', 'dict_en_name']], on='dict_id', how='left')
                .rename(columns={'dict_id':'dict_id_base'})
                .assign(dict_id = lambda df:df.index + 1 + n_cur,
                        theme_id = theme_id,
                        status='1',
                        create_by = user_id,
                        create_time= datetime.datetime.now(),
                        update_by=user_id,
                        update_time=datetime.datetime.now()
                        )
            .to_dict('records')
        )

        try:
            BillDictDataDao.batch_insert_dict_codes(result_db, data)
            result_db.commit()
            result = dict(is_success=True, message='主题字典内容初始化成功')
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message='数据库操作异常')

        return CrudRSModel(**result)


    @classmethod
    async def edit_code_info(cls, result_db: Session, page_object:BillDictDataModel):
        """
        编辑单条码值项信息
        """
        ## 是否存在该条码值
        bill_dict_data = BillDictDataDao.query_code_info_by_code_id(result_db, 
                                                                    code_id=page_object.dict_id)

        if not bill_dict_data:
            return CrudRSModel(is_success=False, message='未查询到该条码值信息')

        
        bill_dict_data = query_to_dict(bill_dict_data)
        for ky, vl in page_object.dict(exclude_unset=True).items():
            bill_dict_data.update({ky:vl})

        try:
            BillDictDataDao.update_bill_dict_data_record(result_db, bill_dict_data)
            result_db.commit()
            result = dict(is_success=True, message='码值更新成功')
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message='数据库操作异常')
        return CrudRSModel(**result)


    @classmethod
    async def delete_dict_codes(cls, result_db: Session, mode='by_key', code_id=None, theme_id:int=None, dict_id_base:str=None, code_key:str=None):
        """
        根据条件删除单条或者多条码值：
        1、根据码值ID删除；
        2、根据账单主题ID、码表ID和码键的联合删除。
        """
        if mode not in ['by_key', 'by_id']:
            raise CrudDataRSModel(is_success=False,  message='删除模式参数`mode`错误，请检查', data=-1)

        ## 是否存在账单记录，存在则禁止删除
        key_map = {'BD001':'bill_name', 'BD002':'pay_channel', 'BD003':'settle_channel', 'BD004':'consume_object', 'BD005':'bill_scene',}
        if mode == 'by_key':
            dict_data = BillDictDataDao.query_code_info_by_key(result_db, theme_id=theme_id, dict_id_base=dict_id_base, code_key=code_key)

            if not dict_data:
                return CrudDataRSModel(is_success=True, message='没有码值需要删除', data=0)

            bill_query = {
                'theme_id':theme_id,
                key_map[dict_id_base]:code_key
            } if dict_id_base else {'theme_id':theme_id}


        else:
            dict_data = BillDictDataDao.query_code_info_by_code_ids(result_db, code_ids=code_id)
            if not dict_data:
                return CrudDataRSModel(is_success=True, message='没有码值需要删除', data=0)            
            bill_query = {
                'theme_id':dict_data[0].theme_id,
            }


        ## 是否存在账单记录，存在则禁止删除
        bill_query = QueryBillModel(**bill_query)
        res = BillDetDao.query_bills_by_condition(result_db, bill_query)
        if res:
            return CrudDataRSModel(is_success=False, message='该条码值存在数据，禁止修改', data=-1)


        try:
            if mode == 'by_id':
                res = BillDictDataDao.delete_dict_code_by_id(db=result_db, code_ids=code_id)
            else:
                res = BillDictDataDao.delete_dict_code_by_key(db=result_db, theme_id=theme_id, dict_id_base=dict_id_base, code_key=code_key)
            result_db.commit()
  
            return CrudDataRSModel(is_success=True, message='字典项删除成功', data=res)
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            return CrudDataRSModel(is_success=False, message='数据库操作异常', data=-1)


    @classmethod
    async def add_dict_code(self, result_db: Session, page_object:BillDictDataModel):
        """
        添加单个码值项信息
        """
        res = BillDictDataDao.query_code_info_by_key(db=result_db, theme_id=page_object.theme_id, dict_id_base=page_object.dict_id_base, code_key=page_object.code_key)
        if res:
            return CrudRSModel(is_success=False, message='该条码值已存在')

        res = BillDictDataDao.query_code_info_by_key(db=result_db, theme_id=page_object.theme_id, dict_id_base=page_object.dict_id_base)
        if not res:
            return CrudRSModel(is_success=False, message='未创建字典不存在，请先初始化字典内容')


        ## 获取当前最大的code_id
        n_cur = BillDictDataDao.query_max_code_id(result_db)
        page_object.dict_id = n_cur + 1

        ## 获取字典的中英文名称
        dict_info = BillDictDataDao.query_base_dict_info_by_id(db=result_db, base_dict_id=page_object.dict_id_base)
        if not dict_info:
            return CrudRSModel(is_success=False, message='未知的基础字典类型')
        page_object.dict_cn_name = dict_info.dict_cn_name
        page_object.dict_en_name = dict_info.dict_en_name


        try:
            BillDictDataDao.insert_dict_code(result_db, page_object)
            result_db.commit()
            result = dict(is_success=True, message='新增码值成功')
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message=f'数据库操作异常')

        return CrudRSModel(**result)


