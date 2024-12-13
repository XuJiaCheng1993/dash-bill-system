#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import datetime
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from config.get_db import get_db
from module.service import get_current_user, BillThemeService, BillDictService, UserService
from module.entity import CrudRSModel, AddBillThemeModel, CurrentUserInfoServiceRSModel, EditBillThemeModel, AddUserThemeRelationModel, EditUserModel
from module.decorators.log_decorators import log_decorator


from utils.response import response_200, response_400, response_500

from utils.log import logger
import traceback

billThemeController = APIRouter(dependencies=[Depends(get_current_user)])



@billThemeController.post("/getThemeById", response_model=CrudRSModel)
@log_decorator(title="账单主题", business_type=5, log_type='operation')
async def get_theme_by_id(request: Request, theme_id:int, query_db: Session = Depends(get_db)):
    try:
        query_result = BillThemeService.get_theme_info_by_id(query_db, theme_id=theme_id)
        if query_result.is_success:
            return response_200(data=query_result.data, message=query_result.message)
        else:
            return response_400(data="", message=query_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billThemeController.post("/getThemeByName", response_model=CrudRSModel)
@log_decorator(title="账单主题", business_type=5, log_type='operation')
async def get_theme_by_name(request: Request, theme_name:str, query_db: Session = Depends(get_db)):
    try:
        query_result = BillThemeService.get_theme_info_by_name(query_db, theme_name=theme_name)
        if query_result.is_success:
            return response_200(data=query_result.data, message=query_result.message)
        else:
            return response_400(data="", message=query_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
    

@billThemeController.post("/addBillTheme", response_model=CrudRSModel)
@log_decorator(title="账单主题", business_type=1, log_type='operation')
async def add_bill_theme(request: Request, add_billtheme: AddBillThemeModel, query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    try:
        add_billtheme.create_by = current_user.user_id
        add_billtheme.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_billtheme.theme_status = '1'
        add_billtheme.update_by = current_user.user_id
        add_billtheme.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_user_result = await BillThemeService.add_theme(query_db, add_billtheme)
        if add_user_result.is_success:
            return response_200(data=add_user_result, message=add_user_result.message)
        else:
            return response_400(data="", message=add_user_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billThemeController.patch("/editBillTheme", response_model=CrudRSModel)
@log_decorator(title="账单主题", business_type=2, log_type='operation')
async def edit_bill_theme(request: Request, edit_billtheme: EditBillThemeModel, query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    try:
        edit_billtheme.update_by = current_user.user_id
        edit_billtheme.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        edit_user_result = await BillThemeService.edit_theme(query_db, edit_billtheme)

        if edit_user_result.is_success:
            return response_200(
                data=edit_user_result,
                message=edit_user_result.message    
            )
        
        else:
            return response_400(data="", message=edit_user_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_400(data="", message=str(e))


@billThemeController.post("/initBillTheme", response_model=CrudRSModel)
@log_decorator(title="账单主题", business_type=1, log_type='operation')
async def init_theme(request: Request, add_billtheme: AddBillThemeModel,  query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    try:
        ## 创建新的账单主题
        add_billtheme.create_by = current_user.user_id
        add_billtheme.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_billtheme.theme_status = '1'
        add_billtheme.update_by = current_user.user_id
        add_billtheme.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_billtheme_result = await BillThemeService.add_theme(query_db, add_billtheme)
        if not add_billtheme_result.is_success:
            return response_400(data="", message=add_billtheme_result.message)
        
        ## 获取账单主题ID
        theme_id = add_billtheme_result.data
        init_bill_dict_result = await BillDictService.init_new_theme_bill_dict_data(query_db, theme_id=theme_id, user_id=current_user.user_id)
        if not init_bill_dict_result.is_success:
            return response_400(data="", message=init_bill_dict_result.message)

        ## 切换用户的默认主题
        switch_theme_result = await UserService.switch_user_theme(query_db, user_id=current_user.user_id, theme_id=theme_id)
        if not switch_theme_result.is_success:
            return response_400(data="", message=switch_theme_result.message)

        ## 新增用户主题关联关系
        add_relation_result = await UserService.add_relation_user_theme(query_db, AddUserThemeRelationModel(theme_id=theme_id, user_id=current_user.user_id))
        if not add_relation_result.is_success:
            return response_400(data="", message=add_relation_result.message)
        
        return response_200(data="", message="初始化账单主题成功")

    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@billThemeController.post("/switchBillTheme", response_model=CrudRSModel)
@log_decorator(title="账单主题", business_type=2, log_type='operation')
async def switch_bill_theme(request: Request, theme_id:int, query_db: Session = Depends(get_db), current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    try:

        ## 切换用户的默认主题
        switch_theme_result = await UserService.switch_user_theme(query_db, user_id=current_user.user_id, theme_id=theme_id)
        if not switch_theme_result.is_success:
            return response_400(data="", message=switch_theme_result.message)

        ## 新增用户主题关联关系
        add_relation_result = await UserService.add_relation_user_theme(query_db, AddUserThemeRelationModel(theme_id=theme_id, user_id=current_user.user_id))
        if not add_relation_result.is_success:
            return response_400(data="", message=add_relation_result.message)
        
        return response_200(data="", message=switch_theme_result.message)
    
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))