#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from pydantic import BaseModel
from typing import Optional


class BillThemeModel(BaseModel):
    theme_id : Optional[int]
    theme_label : Optional[str]
    theme_desc : Optional[str]
    theme_status : Optional[str]
    create_by : Optional[str]
    create_time : Optional[str]
    update_by : Optional[str]
    update_time : Optional[str]

    class Config:
        from_attributes = True


class AddBillThemeModel(BillThemeModel):
    theme_id : Optional[int] = None
    theme_status : Optional[str] = None
    create_by : Optional[str] = None
    create_time : Optional[str] = None
    update_by : Optional[str] = None
    update_time : Optional[str] = None


class EditBillThemeModel(BillThemeModel):
    theme_status : Optional[str] = None
    create_by : Optional[str] = None
    create_time : Optional[str] = None
    update_by : Optional[str] = None
    update_time : Optional[str] = None