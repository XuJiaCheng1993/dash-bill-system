#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from pydantic import BaseModel
from typing import Optional, Union, List


class BillDictDataModel(BaseModel):
    dict_id : Optional[int]
    dict_id_base : Optional[str]
    dict_cn_name : Optional[str]
    dict_en_name : Optional[str]
    code_key : Optional[str]
    father_key : Optional[str]
    level : Optional[int]
    code_sort : Optional[int]
    code_value : Optional[str]
    icon : Optional[str]
    icon_color : Optional[str]
    icon_css : Optional[str]
    is_default : Optional[str]
    status: Optional[str]
    create_by : Optional[str]
    create_time : Optional[str]
    update_by : Optional[str]
    update_time : Optional[str]
    theme_id : Optional[int]

    class Config:
        from_attributes = True


class AddBillDictCodeModel(BillDictDataModel):
    dict_id : Optional[int] = None
    dict_cn_name : Optional[str] = None
    dict_en_name : Optional[str] = None
    create_by : Optional[str] = None
    create_time : Optional[str] = None
    update_by : Optional[str] = None
    update_time : Optional[str] = None


class EditBillDictCodeModel(BillDictDataModel):
    dict_id : Optional[int] = None
    dict_id_base : Optional[str] = None
    dict_cn_name : Optional[str] = None
    dict_en_name : Optional[str] = None
    code_key : Optional[str] = None
    father_key : Optional[str] = None
    level : Optional[int] = None
    code_sort : Optional[int] = None
    code_value : Optional[str] = None
    icon : Optional[str] = None
    icon_color : Optional[str] = None
    icon_css : Optional[str] = None
    is_default : Optional[str] = None
    status: Optional[str] = None
    create_by : Optional[str] = None
    create_time : Optional[str] = None
    update_by : Optional[str] = None
    update_time : Optional[str] = None
    theme_id : Optional[int] = None


class DelBillDictCodeModel(BaseModel):
    del_mode: Optional[str]   
    dict_id_base : Optional[str] = None
    theme_id : Optional[int] = None
    code_key : Optional[str] = None
    dict_id : Union[List[int], int, None] = None
    is_multiple: Optional[bool] = False