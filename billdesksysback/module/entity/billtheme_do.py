#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy import Column, String, DateTime, BigInteger
from config.dbconfig import Base


class BillThemeMapping(Base):
    ''' 账单主题表ORM'''
    __tablename__ = 'bill_theme'
    __table_args__ = {'comment': '账单主题信息表'}
    theme_id = Column(BigInteger, primary_key=True,  comment='主题编号')
    theme_label = Column(String(40),  unique=True, comment='主题名称')
    theme_desc = Column(String(100),  default='', comment='主题描述')
    theme_status = Column(String(4), nullable=False, comment='主题状态')
    create_by = Column(String(60), nullable=False, comment='创建者')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_by = Column(String(60), nullable=False, comment='更新者')
    update_time = Column(DateTime, nullable=False, comment='更新时间')