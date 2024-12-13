#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from sqlalchemy import func
from module.entity import (BillThemeMapping, BillThemeModel)

class BillThemeDao:

    @classmethod
    def query_theme_info_by_ids(cls, db: Session, theme_ids: list):
        theme_infos = (
            db
            .query(BillThemeMapping)
            .filter(BillThemeMapping.theme_id.in_(theme_ids))
            .all()
        )
        return theme_infos
    
    @classmethod
    def query_theme_info_by_id(cls, db: Session, theme_id: int):
        theme_info = (
            db
            .query(BillThemeMapping)
            .filter(BillThemeMapping.theme_id == theme_id)
            .first()
        )
        return theme_info

    @classmethod
    def query_theme_info_by_label(cls, db: Session, theme_label: str):
        theme_info = (
            db
            .query(BillThemeMapping)
            .filter(BillThemeMapping.theme_label == theme_label)
            .first()
        )
        return theme_info


    @classmethod
    def query_max_id(cls, db: Session):
        return db.query(func.max(BillThemeMapping.theme_id)).scalar()


    @classmethod
    def insert_theme_record(cls, db: Session, theme_data:BillThemeModel):
        """
        新增账单记录操作
        :param db: orm对象
        :param dict_type: 字典类型对象
        :return:
        """

        theme_data = BillThemeMapping(**theme_data.dict())
        db.add(theme_data)
        db.flush()

        return theme_data


    @classmethod
    def update_theme_record(cls, db: Session, theme_data: dict):
        """
        编辑字典类型数据库操作
        :param db: orm对象
        :param dict_type: 需要更新的字典类型字典
        :return:
        """
        (
        db
            .query(BillThemeMapping)
            .filter(BillThemeMapping.theme_id == theme_data.get('theme_id'))
            .update(theme_data)
        )


