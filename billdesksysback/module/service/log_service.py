#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from module.entity import SysLoginLogModel, SysOperLogModel, CrudRSModel
from module.dao import LogDao


class LogService:
    """
    系统日志管理服务
    """
    @classmethod
    def add_login_log_services(cls, result_db: Session, page_object: SysLoginLogModel):
        """
        新增单条系统登录记录
        """
        try:
            LogDao.insert_login_log_dao(result_db, page_object)
            result_db.commit()
            result = dict(is_success=True, message='新增成功')
        except Exception as e:
            result_db.rollback()
            result = dict(is_success=False, message=str(e))

        return CrudRSModel(**result)
    

    @classmethod
    def add_oper_log_services(cls, result_db: Session, page_object: SysOperLogModel):
        """
        新增单条系统操作记录
        """
        try:
            LogDao.insert_operation_log_dao(result_db, page_object)
            result_db.commit()
            result = dict(is_success=True, message='新增成功')
        except Exception as e:
            result_db.rollback()
            result = dict(is_success=False, message=str(e))
        
        return CrudRSModel(**result)

