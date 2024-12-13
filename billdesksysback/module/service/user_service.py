#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from module.dao import UserDao, BillThemeDao
from module.entity import EditUserModel, CrudRSModel, AddUserThemeRelationModel, CrudDataRSModel
import datetime
from utils.utils import query_to_dict
import pandas as pd
from utils.log import logger
import traceback


class UserService:
    """
    用户管理模块服务层
    """

    @classmethod
    def get_userinfo_by_id(cls, result_db: Session, bill_id:str):
        """
        根据用户编号查询单条用户信息
        """        
        return UserDao.query_user_by_id(result_db, user_id=bill_id)


    @classmethod
    async def edit_userinfo(cls, result_db: Session, page_object: EditUserModel):
        """
        编辑单条用户信息
        """
        if page_object.user_id is None:
            return CrudRSModel(is_success=False, message='未明确用户编号')
 

        edit_data = page_object.dict(exclude_unset=True)
        if len(edit_data) <= 1:
            return CrudRSModel(is_success=False, message='没有信息需要更新')

        ## 查下是否存在该条用户
        user = UserDao.query_user_by_id(result_db, user_id=page_object.user_id)
        if not user:
            return CrudRSModel(is_success=False, message='用户不存在')

        ## 判断编辑的信息是否与库中不同
        user = query_to_dict(user)
        is_same = True
        for ky, vl in edit_data.items():
            if user.get(ky) != vl:
                is_same = False
                user.update({ky:vl})

        if is_same:
            return CrudRSModel(is_success=False, message='没有信息需要更新')

        try:
            user.update({'update_time':datetime.datetime.now()})
            UserDao.update_user(result_db, user)
            result_db.commit()

            result = dict(is_success=True, message='用户信息更新成功')
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message=f'数据库操作异常')

        return CrudRSModel(**result)
        
    @classmethod
    async def switch_user_theme(self, result_db: Session, user_id:str, theme_id:int):
        """
        切换用户的账单主题
        """
        if not BillThemeDao.query_theme_info_by_id(result_db, theme_id):
            return CrudRSModel(is_success=False, message='账单主题不存在')

        try:
            switch_info = {
                "user_id":user_id, 
                "theme_id":theme_id,
                'update_time':datetime.datetime.now()
                }
            UserDao.update_user(result_db, switch_info)
            result_db.commit()

            result = dict(is_success=True, message='用户账单主题切换成功')
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message='数据库操作异常')

        return CrudRSModel(**result)




    @classmethod
    async def add_relation_user_theme(self, result_db: Session, page_object:AddUserThemeRelationModel) -> CrudRSModel:
        """
        新增用户与账单主题的关联关系
        """    
        if UserDao.query_user_theme_relation_by_id(result_db, user_id=page_object.user_id, theme_id=page_object.theme_id):
            return CrudRSModel(is_success=True, message='用户账单主题关联关系已存在')
        
        page_object.status = '1'
        page_object.operate_time = datetime.datetime.now()

    
        try:
            UserDao.insert_user_theme_relation(result_db, page_object )
            result_db.commit()
            result = dict(is_success=True, message='用户账单主题关联关系录入成功')
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message='数据库操作异常')
        return CrudRSModel(**result)
    

    @classmethod
    async def delete_relation_user_theme(cls, result_db: Session, user_id:str, theme_id:int) -> CrudRSModel:
        """
        删除用户与账单主题的关联关系
        """
        if not UserDao.query_user_theme_relation_by_id(result_db, user_id=user_id, theme_id=theme_id):
            return CrudRSModel(is_success=False, message='用户账单主题关联关系不存在')

        try:
            UserDao.delete_user_theme_relation(result_db, user_id=user_id, theme_id=theme_id)
            result_db.commit()
            result = dict(is_success=True, message='用户账单主题关联关系删除成功')
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message='数据库操作异常')
        return CrudRSModel(**result)


    @classmethod
    async def get_user_all_theme_relations(cls, result_db: Session, user_id:str) -> CrudDataRSModel:
        """
        查询用户的所有账单主题关联关系
        """
        try:
            relations = UserDao.query_user_theme_relations_by_user_id(result_db, user_id)
    
            if not relations:
                result = dict(is_success=False, message='未查询到账单', data=[])
                
   
            theme_infos = BillThemeDao.query_theme_info_by_ids(result_db, theme_ids=[f.theme_id for f in relations])
            result = dict(is_success=True, message='查询成功', 
                          data=pd.DataFrame([query_to_dict(f) for f in theme_infos])[["theme_id", "theme_label"]].to_dict('records')
                          )

        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, message='数据库操作异常', data=[])

        return CrudDataRSModel(**result)

    @classmethod
    async def get_user_all_theme_relations_exclude_user(cls, result_db: Session, user_id:str) -> CrudDataRSModel:
        """
        查询用户所有未关联的账单主题
        """
        try:
            user_relations = UserDao.query_user_theme_relations_by_user_id(result_db, user_id)
            user_relations = [f.theme_id for f in user_relations] if user_relations else []

            all_relations = UserDao.query_all_user_theme_relations(result_db)
            all_relations = [f.theme_id for f in all_relations] if all_relations else []
            
            exclude_relations = list(set(all_relations) - set(user_relations))

            if not exclude_relations:
                result = dict(is_success=False, message='未查询到账单', data=[])
            
            theme_infos = BillThemeDao.query_theme_info_by_ids(result_db, theme_ids=exclude_relations)
            result = dict(is_success=True, message='查询成功', 
                          data=pd.DataFrame([query_to_dict(f) for f in theme_infos])[["theme_id", "theme_label"]].to_dict('records')
                          )

        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, message='数据库操作异常', data=[])
        
        return CrudDataRSModel(**result)

    


