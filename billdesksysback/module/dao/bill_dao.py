#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy import and_, desc
from sqlalchemy.orm import Session
from module.entity import BillMapping, BillModel, QueryBillModel
from typing import Union, List

import pandas as pd




class BillDetDao:
    """
    账单明细表数据库操作层
    """
    @classmethod
    def query_bill_by_id(cls, db: Session, bill_id: str):
        """
        根据字典类型id获取字典类型详细信息
        :param db: orm对象
        :param dict_id: 字典类型id
        :return: 字典类型信息对象
        """
        record = (
            db.query(BillMapping)
            .filter(BillMapping.bill_id == bill_id)
            .first()
        )
        return record


    @classmethod
    def query_bills_by_condition(cls, db: Session, query_object:QueryBillModel):
        records = (
            db.query(BillMapping)
            .filter(BillMapping.user_id == query_object.user_id if query_object.user_id else True,
                    BillMapping.theme_id == query_object.theme_id if query_object.theme_id else True,
                    BillMapping.bill_type == query_object.bill_type if query_object.bill_type else True,
                    BillMapping.bill_name == query_object.bill_name if query_object.bill_name else True,
                    BillMapping.pay_channel == query_object.pay_channel if query_object.pay_channel else True,
                    BillMapping.settle_channel == query_object.settle_channel if query_object.settle_channel else True,
                    BillMapping.consume_object == query_object.consume_object if query_object.consume_object else True,
                    BillMapping.bill_scene == query_object.bill_scene if query_object.bill_scene else True,
                    BillMapping.bill_status == query_object.bill_status if query_object.bill_status else True,
                    BillMapping.bill_amount.between(query_object.bill_amount_min, query_object.bill_amount_max)
                                if all([query_object.bill_amount_min, query_object.bill_amount_max]) else True,
                    BillMapping.bill_date.between(query_object.bill_date_start, query_object.bill_date_end)
                                if all([query_object.bill_date_start, query_object.bill_date_end]) else True,
                    )
            .order_by(desc(BillMapping.into_unix_time))
            .limit(query_object.n_limit if query_object.n_limit else None)
            .all()
        )
        return records
    
    @classmethod
    def query_bills_by_code_key(cls, db: Session, theme_id:int, target_field:str, target_value:Union[str, List[str]], target_method:str):
        
        if target_method == 'eq':      
            res = (
                db
                .query(BillMapping)
                .filter(
                    BillMapping.theme_id == theme_id,
                    getattr(BillMapping, target_field) == target_value
                )
                .first()                    
            )
            
        elif target_method == 'in':
             res = (
                db
                .query(BillMapping)
                .filter(
                    BillMapping.theme_id == theme_id,
                    getattr(BillMapping, target_field).in_(target_value)
                )
                .first()                    
            )

        else :       
             res = (
                db
                .query(BillMapping)
                .filter(
                    BillMapping.theme_id == theme_id,
                    getattr(BillMapping, target_field).like(f'%{target_value}%')
                )
                .first()                    
            )
             
        return res

    @classmethod
    def insert_bill(cls, db: Session, bill_data:BillModel):
        """
        新增账单记录操作
        :param db: orm对象
        :param dict_type: 字典类型对象
        :return:
        """

        bill_data = BillMapping(**bill_data.dict())
        db.add(bill_data)
        db.flush()
        return bill_data


    @classmethod
    def update_bill(cls, db: Session, bill_data: BillModel):
        """
        编辑字典类型数据库操作
        :param db: orm对象
        :param dict_type: 需要更新的字典类型字典
        :return:
        """
        (
        db
            .query(BillMapping)
            .filter(BillMapping.bill_id == bill_data.bill_id)
            .update(bill_data.dict())
        )


    @classmethod
    def delete_bill(cls, db: Session, bill_id: str):
        """
        删除字典数据数据库操作
        :param db: orm对象
        :param dict_data: 字典数据对象
        :return:
        """
        (
            db.query(BillMapping)
            .filter(BillMapping.bill_id == bill_id)
            .delete()
         )
        
    @classmethod
    def batch_insert_bills(cls, db: Session, bills:list[dict]):
        """
        批量新增账单记录操作
        :param db: orm对象
        :param dict_type: 账单对象
        :return:
        """
        res = db.bulk_insert_mappings(BillMapping, bills)
        return res