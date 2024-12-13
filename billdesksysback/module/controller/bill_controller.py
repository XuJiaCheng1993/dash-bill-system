#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import datetime

from fastapi import APIRouter, Depends, Request
from module.service import get_current_user, BillService
from module.entity import (
    CrudRSModel,
    CurrentUserInfoServiceRSModel,
    QueryBillModel,
    AddBillModel,
    EditBillModel,
)

from sqlalchemy.orm import Session
from config.get_db import get_db
from utils.response import response_200, response_400, response_500
from module.decorators.log_decorators import log_decorator

from utils.log import logger
import traceback

billController = APIRouter(dependencies=[Depends(get_current_user)])


@billController.post("/getBillById", response_model=CrudRSModel)
@log_decorator(title="账单管理", business_type=5, log_type="operation")
async def get_bill_by_id(
    request: Request, bill_id: str, query_db: Session = Depends(get_db)
):
    try:
        result = BillService.get_bill_by_id(query_db, bill_id=bill_id)
        if result.is_success:
            return response_200(data=result.data, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billController.post("/addBill", response_model=CrudRSModel)
@log_decorator(title="账单管理", business_type=1, log_type="operation")
async def add_bill(
    request: Request,
    add_bill: AddBillModel,
    query_db: Session = Depends(get_db),
    current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user),
):
    try:
        add_bill.user_id = current_user.user_id
        add_bill_result = await BillService.add_bill(query_db, add_bill)
        if add_bill_result.is_success:
            return response_200(data=add_bill_result, message=add_bill_result.message)
        else:
            return response_400(data="", message=add_bill_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billController.patch("/editBill", response_model=CrudRSModel)
@log_decorator(title="账单管理", business_type=2, log_type="operation")
async def edit_bill(
    request: Request,
    edit_bill: EditBillModel,
    query_db: Session = Depends(get_db),
    current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user),
):
    try:
        edit_bill.user_id = current_user.user_id
        edit_bill_result = await BillService.edit_bill(query_db, edit_bill)
        if edit_bill_result.is_success:
            return response_200(data=edit_bill_result, message=edit_bill_result.message)
        else:
            return response_400(data="", message=edit_bill_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billController.post("/getBillTableData", response_model=CrudRSModel)
@log_decorator(title="账单管理", business_type=5, log_type="operation")
async def get_bill_table_data(
    request: Request,
    query_bill: QueryBillModel,
    query_db: Session = Depends(get_db),
    current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user),
):

    if query_bill.theme_id is None:
        return response_400(data="", message="账单主题ID不能为空")

    query_bill.user_id = current_user.user_id
    try:
        query_result = BillService.get_bills(query_db, query_bill)
        if query_result.is_success:
            return response_200(data=query_result.data, message=query_result.message)
        else:
            return response_400(data="", message=query_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billController.post("/delBill", response_model=CrudRSModel)
@log_decorator(title="账单管理", business_type=3, log_type="operation")
async def delete_bill(
    request: Request, bill_id: str, query_db: Session = Depends(get_db)
):
    try:
        del_result = await BillService.delete_bill(query_db, bill_id)
        if del_result.is_success:
            return response_200(data=del_result, message=del_result.message)
        else:
            return response_400(data="", message=del_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
