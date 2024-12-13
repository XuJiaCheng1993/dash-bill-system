#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 


from sqlalchemy.orm import Session
from module.dao import BillThemeDao
from module.entity import (
    BillThemeModel,
    AddBillThemeModel,
    CrudDataRSModel,
    CrudRSModel,
)
from utils.utils import query_to_dict
from utils.log import logger
import traceback

class BillThemeService:
    """
    账单主题管理服务
    """

    @classmethod
    def get_theme_info_by_ids(cls, result_db: Session, theme_ids: list):
        """
        根据账单主题编号查询多条账单主题信息
        """
        return BillThemeDao.query_theme_info_by_ids(result_db, theme_ids=theme_ids)

    @classmethod
    def get_theme_info_by_id(cls, result_db: Session, theme_id):
        """
        根据账单主题编号查询单条账单主题信息
        """
        try:
            theme = BillThemeDao.query_theme_info_by_id(result_db, theme_id=theme_id)
            if theme:
                result = dict(
                    is_success=True, data=query_to_dict(theme), message="查询成功"
                )
            else:
                result = dict(
                    is_success=False, data="", message="查询失败，未查询到数据"
                )

        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, data="", message="查询失败，数据库异常")

        return CrudDataRSModel(**result)

    @classmethod
    def get_theme_info_by_name(cls, db: Session, theme_name: str):
        """
        根据账单主题名称查询账单主题信息
        """
        try:
            theme = BillThemeDao.query_theme_info_by_label(db, theme_label=theme_name)
            if theme:
                result = dict(
                    is_success=True, data=query_to_dict(theme), message="查询成功"
                )
            else:
                result = dict(
                    is_success=False, data="", message="查询失败，未查询到数据"
                )

        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, data="", message="查询失败，数据库异常")

        return CrudDataRSModel(**result)

    @classmethod
    async def add_theme(cls, result_db: Session, page_object: AddBillThemeModel):
        """
        添加单条账单主题信息
        """
        themeinfo = BillThemeDao.query_theme_info_by_label(
            result_db, theme_label=page_object.theme_label
        )
        if themeinfo:
            return CrudDataRSModel(is_success=False, message="主题已存在", data=-1)

        cur_max = BillThemeDao.query_max_id(result_db)
        page_object.theme_id = cur_max + 1
        data = BillThemeModel(**page_object.dict())

        try:
            BillThemeDao.insert_theme_record(result_db, data)
            result_db.commit()
            result = dict(is_success=True, message="主题新增成功", data=cur_max + 1)
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message=f"数据库操作异常", data=-1)

        return CrudDataRSModel(**result)

    @classmethod
    async def edit_theme(cls, result_db: Session, page_object: BillThemeModel):
        """
        编辑单条账单主题信息
        """
        theme = BillThemeDao.query_theme_info_by_id(
            result_db, theme_id=page_object.theme_id
        )
        if not theme:
            return CrudRSModel(is_success=False, message="主题不存在")

        page_object.theme_status = theme.theme_status
        page_object.create_by = theme.create_by
        page_object.create_time = theme.create_time

        try:

            BillThemeDao.update_theme_record(result_db, theme_data=page_object.dict())
            result_db.commit()

            result = dict(is_success=True, message="账单主题更新成功")
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message=f"数据库操作异常")

        return CrudRSModel(**result)
