#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from pydantic import BaseModel
from typing import Union, Optional, List


class SysOperLogModel(BaseModel):
    """
    操作日志表对应pydantic模型
    """
    oper_id: Optional[int]  = None
    title: Optional[str]
    business_type: Optional[int]
    method: Optional[str]
    request_method: Optional[str]
    operator_type: Optional[str]
    oper_user_id : Optional[str]
    oper_name: Optional[str]
    oper_url: Optional[str]
    oper_ip: Optional[str]
    oper_param: Optional[str]
    json_result: Optional[str]
    status: Optional[str]
    error_msg: Optional[str]
    oper_time: Optional[str]
    cost_time: Optional[int]

    class Config:
        from_attributes = True


class SysLoginLogModel(BaseModel):
    """
    登录日志表对应pydantic模型
    """
    info_id: Optional[int] = None
    user_name: Optional[str]
    ipaddr: Optional[str]
    browser: Optional[str]
    os: Optional[str]
    status: Optional[str]
    msg: Optional[str]
    login_time: Optional[str]

    class Config:
        from_attributes = True