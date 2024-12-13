#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from pydantic import BaseModel
from typing import Any

class CrudRSModel(BaseModel):
    """ CRUD操作的响应模型 """
    is_success: bool
    message: str

class CrudDataRSModel(CrudRSModel):
    """ CRUD操作的响应模型 带额外参数"""
    data : Any