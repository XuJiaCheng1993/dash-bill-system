#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from module.entity import (BillDictDataMapping, BillDictDataBaseMapping, BillDictBaseMapping, BillDictDataModel)
from utils.utils import list_format_datetime
from sqlalchemy import func
from typing import List

class BillDictDataDao:
    """
    账单字典类型管理模块数据库操作层
    """

    @classmethod
    def query_dict_list_by_theme_id(cls, db: Session, theme_id: int):
        """
        根据主题ID获取账单字典类型详细信息
        :param db: orm对象
        :param theme_id: 账单主题ID
        :return: 字典类型信息对象
        """
        dict_values = (
            db
            .query(BillDictDataMapping)
            .filter(BillDictDataMapping.theme_id == theme_id)
            .all()
        )
        return list_format_datetime(dict_values)


    @classmethod
    def query_code_info_by_key(cls, db: Session, theme_id: int = None, dict_id_base:str= None, code_key:str= None):
        """
        根据主题ID、基础字典ID及码键来共同获取码值详细信息
        :param db: orm对象
        :param theme_id: 账单主题ID
        :return: 字典类型信息对象
        """
        code_info = (
            db.query(BillDictDataMapping)
            .filter(BillDictDataMapping.theme_id == theme_id if theme_id else True,
                    BillDictDataMapping.dict_id_base == dict_id_base if dict_id_base else True,
                    BillDictDataMapping.code_key == code_key if code_key else True)
            .first()
        )
        return code_info


    @classmethod
    def query_code_info_by_code_id(cls, db: Session, code_id:int):
        """
        根据码键ID来获取码值详细信息
        :param db: orm对象
        :param theme_id: 账单主题ID
        :return: 字典类型信息对象
        """
        code_info = (
            db.query(BillDictDataMapping)
            .filter(BillDictDataMapping.dict_id == code_id)
            .first()
        )
        return code_info

    @classmethod
    def query_code_info_by_code_ids(cls, db: Session, code_ids:List[int]):
        code_info = (
            db.query(BillDictDataMapping)
            .filter(BillDictDataMapping.dict_id.in_(code_ids))
            .all()
        )
        return code_info



    @classmethod
    def query_max_code_id(cls, db: Session):
        max_id = db.query(func.max(BillDictDataMapping.dict_id)).scalar()
        return max_id if max_id else 0

    @classmethod
    def query_base_dict_data(cls, db: Session):
        """
        获取基础的账单字典详细信息
        """
        dict_data = (
            db
            .query(BillDictDataBaseMapping)
            .all()
        )
        return dict_data


    @classmethod
    def query_base_dict_info(cls, db: Session):
        """
        获取基础的账单字典信息
        """
        dict_info = (
            db
            .query(BillDictBaseMapping)
            .all()
        )
        return dict_info


    @classmethod
    def query_base_dict_info_by_id(cls, db: Session, base_dict_id:str):
        """
        获取某条基础账单字典的字典描述信息
        """
        dict_info = (
            db
            .query(BillDictBaseMapping)
            .filter(BillDictBaseMapping.dict_id == base_dict_id)
            .first()
        )
        return dict_info


    @classmethod
    def insert_dict_code(cls, db: Session, bill_dict_data:BillDictDataModel):
        """
        新增账单字典记录操作
        :param db: orm对象
        :param dict_type: 字典类型对象
        :return:
        """
        data = BillDictDataMapping(**bill_dict_data.dict())
        db.add(data)
        db.flush()

        return data

    @classmethod
    def batch_insert_dict_codes(cls, db: Session, bill_dict_data:list[dict]):
        """
        批量新增账单字典记录操作
        :param db: orm对象
        :param dict_type: 字典类型对象
        :return:
        """
        res = db.bulk_insert_mappings(BillDictDataMapping, bill_dict_data)
        return res


    @classmethod
    def delete_dict_code_by_key(self, db: Session, theme_id:int=None, code_key:str=None, dict_id_base:str=None):
        res = (
            db.query(BillDictDataMapping)
            .filter(BillDictDataMapping.theme_id == theme_id if theme_id else True,
                    BillDictDataMapping.code_key == code_key if code_key else True,
                    BillDictDataMapping.dict_id_base == dict_id_base if dict_id_base else True)
            .delete()
        )
        return res

    @classmethod
    def delete_dict_code_by_id(self, db: Session, code_ids:List[int]):
        res = (
            db.query(BillDictDataMapping)
            .filter(BillDictDataMapping.dict_id.in_(code_ids))
            .delete()
        )
        return res




    @classmethod
    def update_bill_dict_data_record(cls, db: Session, bill_dict_data: dict):
        """
        编辑用户数据库操作
        :param db: orm对象
        :param user: 需要更新的用户字典
        :return: 编辑校验结果
        """
        (
            db.query(BillDictDataMapping)
            .filter(BillDictDataMapping.dict_id == bill_dict_data.get("dict_id"))
            .update(bill_dict_data)
         )







if __name__  == '__main__':
    from config.dbconfig import SessionLocal
    db = SessionLocal()
    theme = BillDictDataDao.query_dict_list_by_theme_id(db, theme_id=1)
    codeinfo = BillDictDataDao.query_code_info_by_key(db, theme_id=1, dict_id_base='BD001', code_key='A')


    # db.close()




