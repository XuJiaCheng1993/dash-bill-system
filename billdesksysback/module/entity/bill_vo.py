#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from pydantic import BaseModel
from typing import Optional, List, Union

class BillModel(BaseModel):
    """ 账单模型 """
    bill_id : Optional[str]
    bill_type : Optional[str]
    bill_name : Optional[str]
    pay_channel : Optional[str]
    settle_channel : Optional[str]
    consume_object : Optional[str]
    bill_scene : Optional[str]
    bill_status : Optional[str]
    bill_amount : Optional[float]
    bill_date : Optional[str]
    remark : Optional[str]
    user_id : Optional[str]
    theme_id : Optional[int]
    into_unix_time : Optional[int]

    class Config:
        from_attributes = True


class QueryBillModel(BaseModel):
    """ 查询账单条件模型 """
    user_id : Optional[str] = None
    theme_id : Optional[int] = None
    bill_type : Optional[str] = None
    bill_name : Optional[str] = None
    pay_channel : Optional[str] = None
    settle_channel : Optional[str] = None
    consume_object : Optional[str] = None
    bill_scene : Optional[str] = None
    bill_status : Optional[str] = None
    bill_amount_min : Optional[float] = None
    bill_amount_max : Optional[float] = None
    bill_date_start : Optional[str] = None
    bill_date_end : Optional[str] = None
    n_limit : Optional[int] = None

class AddBillModel(BillModel):
    """ 新增账单模型 """
    user_id : Optional[str] = None
    into_unix_time : Optional[int] = None


class EditBillModel(BillModel):
    """ 编辑账单模型 """
    bill_type: Optional[str] = None
    bill_name: Optional[str] = None
    pay_channel: Optional[str] = None
    settle_channel: Optional[str] = None
    consume_object: Optional[str] = None
    bill_scene: Optional[str] = None
    bill_status: Optional[str] = None
    bill_amount: Optional[float] = None
    bill_date: Optional[str] = None
    remark: Optional[str] = None
    user_id: Optional[str] = None
    theme_id: Optional[int] = None
    into_unix_time: Optional[int] = None


class AnalyzeBillModel(BaseModel):
    """ 分析账单模型 """
    analyze_by : Union[str, List[str]]
    is_contain_date_field : Optional[bool] = False
    date_field: Union[str] = None
    date_dim : Optional[str] = None  
    is_return_code : Optional[bool] = True
    is_summary : Optional[bool] = False
    refund_method : Optional[str] = 'default'
    