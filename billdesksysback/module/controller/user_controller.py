#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from config.get_db import get_db
from module.service import get_current_user, UserService
from module.entity import CrudRSModel, EditUserModel, CurrentUserInfoServiceRSModel, AddUserThemeRelationModel
from module.decorators.log_decorators import log_decorator

from utils.response import response_200, response_400, response_500


from utils.log import logger
import traceback

userController = APIRouter(dependencies=[Depends(get_current_user)])


@userController.patch("/editUser", response_model=CrudRSModel, description="编辑用户信息")
@log_decorator(title="用户管理", business_type=2, log_type='operation')
async def edit_system_user(request: Request, edit_user: EditUserModel, query_db: Session = Depends(get_db),
                           current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):  
    try:
        edit_user.user_id = current_user.user_id
        edit_user_result = await UserService.edit_userinfo(query_db, edit_user)
        if edit_user_result.is_success:
            return response_200(data=edit_user_result, message=edit_user_result.message)
        else:
            return response_400(data="", message=edit_user_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
    

@userController.post("/addRelationUserTheme", response_model=CrudRSModel, description="新增用户与账单主题的关联关系")
@log_decorator(title="用户管理", business_type=1, log_type='operation')
async def add_relation_user_theme(request: Request, theme_id:int, query_db: Session = Depends(get_db),
                           current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):  
    try:
        relation = AddUserThemeRelationModel(user_id=current_user.user_id, theme_id=theme_id)
        result = await UserService.add_relation_user_theme(query_db, relation)
        if result.is_success:
            return response_200(data=result, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
        

@userController.post("/deleteRelationUserTheme", response_model=CrudRSModel, description="删除用户与账单主题的关联关系")
@log_decorator(title="用户管理", business_type=3, log_type='operation')
async def delete_relation_user_theme(request: Request, theme_id:int, query_db: Session = Depends(get_db),
                           current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):  
    try:
        result = await UserService.delete_relation_user_theme(query_db, current_user.user_id, theme_id)
        if result.is_success:
            return response_200(data=result, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
    
@userController.post("/getUserThemeRelations", response_model=CrudRSModel, description="获取用户所有关联的主题")
@log_decorator(title="用户管理", business_type=5, log_type='operation')
async def get_user_theme_relations(request: Request, query_db: Session = Depends(get_db),
                           current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    try:
        result = await UserService.get_user_all_theme_relations(query_db, current_user.user_id)
        if result.is_success:
            return response_200(data=result.data, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))
    

@userController.post("/getUserThemeRelationsExcludeUser", response_model=CrudRSModel, description="获取用户所有未关联的主题")
@log_decorator(title="用户管理", business_type=5, log_type='operation')
async def get_user_theme_relations_exclude_user(request: Request, query_db: Session = Depends(get_db),
                           current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    try:
        result = await UserService.get_user_all_theme_relations_exclude_user(query_db, current_user.user_id)
        if result.is_success:
            return response_200(data=result.data, message=result.message)
        else:
            return response_400(data="", message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))