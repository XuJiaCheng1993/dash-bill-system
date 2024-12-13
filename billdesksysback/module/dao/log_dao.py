#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from module.entity import (SysLoginLogMapping, SysOperLogMapping, SysLoginLogModel, SysOperLogModel)


class LogDao:
    @classmethod
    def insert_operation_log_dao(cls, db: Session, oper_log: SysOperLogModel):
        """
        新增操作日志数据库操作
        :param db: orm对象
        :param operation_log: 操作日志对象
        :return: 新增校验结果
        """
        data = SysOperLogMapping(**oper_log.dict())
        db.add(data)
        db.flush()

        return data
    
    @classmethod
    def insert_login_log_dao(cls, db: Session, login_log: SysLoginLogModel):
        """
        新增登录日志数据库操作
        :param db: orm对象
        :param login_log: 登录日志对象
        :return: 新增校验结果
        """
        data = SysLoginLogMapping(**login_log.dict())
        db.add(data)
        db.flush()
        return data
    
