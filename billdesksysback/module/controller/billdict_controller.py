#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import datetime

from fastapi import APIRouter, Depends, Request
from module.service import get_current_user, BillDictService
from module.entity import CrudRSModel, CurrentUserInfoServiceRSModel, EditBillDictCodeModel, DelBillDictCodeModel, AddBillDictCodeModel

from sqlalchemy.orm import Session
from config.get_db import get_db
from utils.response import response_200, response_400, response_500
from module.decorators.log_decorators import log_decorator

from utils.log import logger
import traceback


billDictController = APIRouter(dependencies=[Depends(get_current_user)])


@billDictController.post("/checkCodeItemHasBillData", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=6, log_type='operation')
async def check_code_item_has_bill(request: Request, theme_id:int, dict_id:str, code_key:str, query_db: Session = Depends(get_db)):
    try:
        check_result = BillDictService.check_code_item_exist_data(query_db, theme_id=theme_id, dict_id_base=dict_id, code_key=code_key)
        return response_200(data='Y' if check_result else 'N', message="存在账单" if check_result else "不存在账单")    

    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
    
@billDictController.post("/initDictData", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=1, log_type='operation')
async def init_bill_dict_data_according_theme_id(request: Request, theme_id:int, query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):

    try:
        result = await BillDictService.init_new_theme_bill_dict_data(query_db, theme_id=theme_id, user_id=current_user.user_id)
        if result.is_success:
            return response_200(data=result, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))

@billDictController.post("/getDictCodeList", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=5, log_type='operation')
async def get_dict_code_list(request: Request, theme_id:int, query_db: Session = Depends(get_db)):
    try:
        query_result = BillDictService.get_dict_codes_list_by_theme_id(query_db, theme_id=theme_id)
        if query_result.is_success:
            return response_200(data=query_result.data, message=query_result.message)
        else:
            return response_400(data="", message=query_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))

@billDictController.post("/getCodeById", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=5, log_type='operation')
async def get_code_by_id(request: Request, code_id:int, query_db: Session = Depends(get_db)):
    try:
        query_result = BillDictService.get_code_info_by_id(query_db, code_id=code_id)
        if query_result.is_success:
            return response_200(data=query_result.data, message=query_result.message)
        else:
            return response_400(data="", message=query_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))

@billDictController.post("/getCodeByKey", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=5, log_type='operation')
async def get_code_by_key(request: Request, theme_id: int, dict_id:str, code_key:str, query_db: Session = Depends(get_db)):
    try:
        query_result =  BillDictService.get_code_info_by_key(query_db, theme_id=theme_id, dict_id_base=dict_id, code_key=code_key)
        if query_result.is_success:
            return response_200(data=query_result.data, message=query_result.message)
        else:
            return response_400(data="", message=query_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billDictController.post("/addDictCode", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=1, log_type='operation')
async def add_bill_dict_code_info(request: Request, add_code:AddBillDictCodeModel, query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    if not all([add_code.dict_id_base, add_code.code_key, add_code.theme_id]):
        return response_400(data="", message="缺少必要参数")
    
    ## 记录创建者和更新折的用户信息
    add_code.create_by = current_user.user_id
    add_code.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_code.update_by = current_user.user_id
    add_code.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        result = await BillDictService.add_dict_code(query_db, add_code)
        if result.is_success:
            return response_200(data=result, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billDictController.patch("/editDictCode", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=2, log_type='operation')
async def edit_bill_dict_code_info(request: Request, edit_code:EditBillDictCodeModel, query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    
    if (not edit_code.dict_id) and (not all([edit_code.dict_id_base, edit_code.code_key, edit_code.theme_id])):
       return response_400(data="", message="缺少必要参数")

    ## 记录用户信息
    edit_code.update_by = current_user.user_id
    edit_code.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        result = await BillDictService.edit_code_info(query_db, edit_code)
        if result.is_success:
            return response_200(data=result, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
    

@billDictController.post("/delDictCodes", response_model=CrudRSModel)
@log_decorator(title="账单字典", business_type=3, log_type='operation')
async def del_bill_dict_codes(request: Request, del_codes:DelBillDictCodeModel, query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    
    if del_codes.del_mode not in ['by_key', 'by_id']:
        return response_400(data="", message="del_mode参数错误, 'by_key' or 'by_id'")

    if del_codes.del_mode == 'by_id':
        if del_codes.dict_id is None:
            return response_400(data="", message="'by_id'模式下，dict_id参数不能为空")

        if del_codes.is_multiple:
            if not isinstance(del_codes.dict_id, list):
                return response_400(data="", message="删除多个字典项时, dict_id参数类型错误, 需为list类型")
            
        if not del_codes.is_multiple:
            del_codes.dict_id = [del_codes.dict_id, ]

        del_func_params = {'code_id':del_codes.dict_id, 'mode':'by_id'}    

    else:
        if del_codes.theme_id is None:
            return response_400(data="", message="'by_key'模式下，theme_id参数不能为空")
        
        if not del_codes.is_multiple:
            if not del_codes.code_key:
                return response_400(data="", message="删除单个字典项时, code_key参数不能为空")
        
        del_func_params = {'theme_id':del_codes.theme_id, 'dict_id_base':del_codes.dict_id_base, 'code_key':del_codes.code_key, 'mode':'by_key'}

    try:
        result = await BillDictService.delete_dict_codes(query_db, **del_func_params)
        if result.is_success:
            return response_200(data=result, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))    