#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from config.dbconfig import Base


class BillDictBaseMapping(Base):
    ''' 基础账单码值表ORM'''
    __tablename__ = 'bill_dict_base'
    __table_args__ = {'comment': '基础账单字典表'}
    dict_id = Column(String(20), primary_key=True, comment='字典编号')
    dict_cn_name = Column(String(100), nullable=False, default='', comment='字典中文名称')
    dict_en_name = Column(String(50), nullable=False, default='', comment='字典英文名称')
    icon = Column(String(30), nullable=False, default='', comment='字典图标')
    icon_color = Column(String(10), nullable=False, default='', comment='图标颜色')
    css_style = Column(String(100), nullable=False, default='', comment='CSS样式')
    max_lv = Column(Integer, nullable=False, default=1, comment='最大层级')


class BillDictDataBaseMapping(Base):
    '''基础账单码值项表ORM'''
    __tablename__ = 'bill_dict_data_base'
    __table_args__ = {'comment': '基础账单字典码值表'}
    dict_id = Column(String(20), primary_key=True, comment='字典编号')
    code_key = Column(String(15), primary_key=True, nullable=False, comment='码键' )
    father_key = Column(String(15), nullable=True, comment='父键' )
    level = Column(Integer, nullable=False, comment='所处层级')
    code_sort = Column(Integer, nullable=True, comment='码键顺序' )
    code_value = Column(String(60), nullable=False, default='', comment='码值')
    icon = Column(String(50), nullable=True, comment='图标' )
    icon_color = Column(String(10), nullable=True, comment='图标颜色' )
    icon_css = Column(String(100), nullable=True, comment='其他CSS样式')
    is_default = Column(String(4), nullable=True, comment='是否默认' )


class BillDictDataMapping(Base):
    '''账单码值项表ORM'''
    __tablename__ = 'bill_dict_data'
    __table_args__ = {'comment': '账单字典码值表'}
    dict_id = Column(BigInteger, primary_key=True, comment='字典编号')
    dict_id_base = Column(String(20), comment='基础字典编号')
    dict_cn_name = Column(String(100), nullable=False, default='', comment='字典中文名称')
    dict_en_name = Column(String(50), nullable=False, default='', comment='字典英文名称')
    code_key = Column(String(15), primary_key=True, nullable=False, comment='码键' )
    father_key = Column(String(15), nullable=True, comment='父键' )
    level = Column(Integer, nullable=False, comment='所处层级')
    code_sort = Column(Integer, nullable=True, comment='码键顺序' )
    code_value = Column(String(60), nullable=False, default='', comment='码值')
    icon = Column(String(50), nullable=True, comment='图标' )
    icon_color = Column(String(10), nullable=True, comment='图标颜色' )
    icon_css = Column(String(100), nullable=True, comment='其他CSS样式')
    is_default = Column(String(4), nullable=True, comment='是否默认' )
    status = Column(String(4), nullable=False, comment='码值状态')
    create_by = Column(String(60), nullable=False, comment='创建者')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_by = Column(String(60), nullable=False, comment='更新者')
    update_time = Column(DateTime, nullable=False, comment='更新时间')
    theme_id = Column(BigInteger,  nullable=False, comment='主题编号')