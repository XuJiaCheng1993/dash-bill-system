#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy import Column, BIGINT, String, DECIMAL, DATE
from config.dbconfig import Base



class BillMapping(Base):
    '''账单类型ORM'''
    __tablename__ = 'f_bill_data'
    __table_args__ = {'comment': '账单主题信息表'}
    bill_id = Column(String(60), primary_key=True, comment='账单编号')
    bill_type = Column(String(15), nullable=False, comment='账单类型编码' )
    bill_name = Column(String(15), nullable=False, comment='账单名称编码' )
    pay_channel = Column(String(15), nullable=False, comment='支付渠道编码' )
    settle_channel = Column(String(15), nullable=False, comment='结算渠道编码' )
    consume_object = Column(String(15), nullable=False, comment='消费对象编码' )
    bill_scene = Column(String(15), nullable=False, comment='账单场景编码' )
    bill_status = Column(String(15), nullable=False, comment='账单状态编码' )
    bill_amount = Column(DECIMAL(10, 2), nullable=False, comment='账单金额'  )
    bill_date = Column(DATE, nullable=False, comment='账单日期'  )
    remark = Column(String(600), default='', comment='备注' )
    user_id  = Column(String(60), nullable=False, comment='创建用户编号' )
    theme_id  = Column(BIGINT, nullable=False, comment='账单字典主题编号' )
    into_unix_time = Column(BIGINT, nullable=False, comment='录入时间戳'  )