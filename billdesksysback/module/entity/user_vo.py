#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from pydantic import BaseModel, Field
from typing import Optional, Union

class SysUserModel(BaseModel):
    user_id : Optional[str]
    user_name : Optional[str]
    user_nick : Optional[str]
    password : Optional[str]
    status : Optional[str]
    phone_number : Optional[str]
    email : Optional[str]
    role : Optional[str]
    industry : Optional[str]
    job : Optional[str]
    theme_id : Optional[int]
    create_time : Optional[str]
    update_time : Optional[str]

    class Config:
        from_attributes = True



class CurrentUserInfoServiceRSModel(BaseModel):
    """
    获取当前用户信息响应模型
    """
    user_id: Optional[str]
    user_name: Optional[str]
    user_nick: Optional[str]
    phone_number : Optional[str]
    email : Optional[str]
    role : Optional[str]
    industry : Optional[str]
    job : Optional[str]
    theme_id : Optional[int]



class EditUserModel(BaseModel):
    user_id: Optional[str] = None
    user_nick: Optional[str] = None
    status: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    industry: Optional[str] = None
    job: Optional[str] = None
    theme_id: Optional[int] = None


class UserThemeRelationModel(BaseModel):
    user_id  : Optional[str]
    theme_id  : Optional[int]
    status : Optional[str]
    operate_time : Optional[str]
    class Config:
        from_attributes = True

class AddUserThemeRelationModel(UserThemeRelationModel):
    status : Optional[str] = None
    operate_time : Optional[str] = None


class EditUserThemeRelationModel(UserThemeRelationModel):
    pass