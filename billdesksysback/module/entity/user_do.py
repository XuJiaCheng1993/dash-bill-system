#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy import Column, Integer, String, DateTime, BigInteger, CHAR, VARCHAR
from config.dbconfig import Base

class SysUserMapping(Base):
    ''' 用户当前信息表'''
    __tablename__ = 'sys_user'
    __table_args__ = {'comment': '用户信息表'}
    user_id  = Column(String(60), primary_key=True, comment='用户编号')
    user_name = Column(String(50), nullable=False, comment='账户名称')
    user_nick = Column(String(50), nullable=False, comment='账户昵称')
    password = Column(String(100), nullable=False,  comment='账户密码')
    status = Column(CHAR(4), nullable=False, comment='账户状态')
    phone_number = Column(String(11), nullable=True, comment='手机号')
    email = Column(String(30), nullable=True, comment='电子邮箱')
    role = Column(CHAR(4), nullable=False,  comment='用户角色')
    industry = Column(String(30), nullable=True, comment='行业')
    job = Column(String(30), nullable=True, comment='职业')
    theme_id = Column(BigInteger, nullable=False, comment='当前使用的主题编号')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_time = Column(DateTime, nullable=False, comment='更新时间')


class SysUserBillThemeMapping(Base):
    ''' 用户账单主题关联表'''
    __tablename__ = 'sys_user_bill_theme'
    __table_args__ = {'comment': '用户账单主题关联表'}
    user_id  = Column(String(60), primary_key=True, comment='用户编号')
    theme_id = Column(BigInteger, primary_key=True,  comment='主题编号')
    status = Column(VARCHAR(4), nullable=False, comment='关联状态', insert_default='1')
    operate_time = Column(DateTime, nullable=False, comment='关联时间')