#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from pydantic import BaseModel
from typing import Optional
# from .user_vo import SysUserModel

class UserLoginRQModel(BaseModel):
    user_name: str
    password: str
    session_id: Optional[str]


class TokenRSModel(BaseModel):
    access_token: str
    token_type: str


class ResetUserRQModel(BaseModel):
    """
    重置用户密码模型
    """
    user_id :Optional[str]
    old_password: Optional[str]
    new_password: Optional[str]