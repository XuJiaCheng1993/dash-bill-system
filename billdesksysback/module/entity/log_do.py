#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy import Column, Integer, String, DateTime, Text, BigInteger, Index
from config.dbconfig import Base
from datetime import datetime


class SysLoginLogMapping(Base):
    """
    系统访问记录
    """
    __tablename__ = 'sys_login_log'
    __table_args__ = {'comment': '系统访问记录表'}
    info_id = Column(Integer, primary_key=True, autoincrement=True, comment='访问日志自增ID')
    user_name = Column(String(50), nullable=True, default='', comment='用户账号')
    ipaddr = Column(String(128), nullable=True, default='', comment='登录IP地址')
    browser = Column(String(50), nullable=True, default='', comment='浏览器类型')
    os = Column(String(50), nullable=True, default='', comment='操作系统')
    status = Column(String(1), nullable=True, default='S', comment='登录状态（S成功 F失败）')
    msg = Column(String(255), nullable=True, default='', comment='提示消息')
    login_time = Column(DateTime, nullable=True, default=datetime.now(), comment='访问时间')

    idx_sys_logininfor_s = Index('idx_sys_login_log_s', status)
    idx_sys_logininfor_lt = Index('idx_sys_login_log_lt', login_time)


class SysOperLogMapping(Base):
    """
    操作日志记录
    """
    __tablename__ = 'sys_oper_log'
    __table_args__ = {'comment': '系统操作日志记录表'}
    oper_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='日志主键')
    title = Column(String(50), nullable=True, default='', comment='模块标题')
    business_type = Column(Integer, default=0, comment='业务类型（0其它 1新增 2修改 3删除）')
    method = Column(String(100), nullable=True, default='', comment='方法名称')
    request_method = Column(String(10), nullable=True, default='', comment='请求方式')
    operator_type = Column(String(4), default='ot', comment='操作类别（ot其它 pc后台用户 mob手机端用户）')
    oper_user_id = Column(String(50), nullable=True, default='', comment='操作用户ID')
    oper_name = Column(String(50), nullable=True, default='', comment='操作用户名称')
    oper_url = Column(String(255), nullable=True, default='', comment='请求URL')
    oper_ip = Column(String(128), nullable=True, default='', comment='主机地址')
    oper_param = Column(String(2000), nullable=True, default='', comment='请求参数')
    json_result = Column(String(2000), nullable=True, default='', comment='返回参数')
    status = Column(String(1), default='S', comment='操作状态（S成功 F失败）')
    error_msg = Column(String(2000), nullable=True, default='', comment='错误消息')
    oper_time = Column(DateTime, nullable=True, default=datetime.now(), comment='操作时间')
    cost_time = Column(BigInteger, default=0, comment='消耗时间')

    idx_sys_oper_log_bt = Index('idx_sys_oper_log_bt', business_type)
    idx_sys_oper_log_s = Index('idx_sys_oper_log_s', status)
    idx_sys_oper_log_ot = Index('idx_sys_oper_log_ot', oper_time)


