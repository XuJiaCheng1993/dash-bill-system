#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import uuid
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
import datetime

from module.entity import UserLoginRQModel, TokenRSModel, CurrentUserInfoServiceRSModel, CrudRSModel, ResetUserRQModel
from module.service.login_service import authenticate_user, create_access_token, CustomOAuth2PasswordRequestForm, get_current_user, reset_password_services
from config.get_db import get_db
from config.env import JwtConfig

from utils.response import response_400, LoginException, response_200, response_500
from module.decorators.log_decorators import log_decorator


from utils.log import logger
import traceback


loginController = APIRouter()


@loginController.post("/loginByAccount", response_model=TokenRSModel)
@log_decorator(title="用户登录", business_type=0, log_type='login')
async def login(request: Request, form_data: CustomOAuth2PasswordRequestForm = Depends(), query_db: Session = Depends(get_db)):

    user = UserLoginRQModel(
        **dict(
            user_name=form_data.username,
            password=form_data.password,
            session_id=form_data.session_id,
        )
    )
    try:
        result = await authenticate_user(request, query_db, user)
    except LoginException as e:
        return response_400(data="", message=e.message)
    
    try:
        access_token_expires = JwtConfig.jwt_expire_minutes
        session_id = str(uuid.uuid4())
        access_token = create_access_token(
            data={
                "user_id": str(result.user_id),
                "user_name": result.user_name,
                "session_id": session_id,
            },
            expires_delta=access_token_expires
        )
        await request.app.state.redis.set(f"access_token:{result.user_id}", access_token,
                                            ex=datetime.timedelta(minutes=JwtConfig.jwt_redis_expire_minutes))     
        # 判断请求是否来自于api文档，如果是返回指定格式的结果，用于修复api文档认证成功后token显示undefined的bug
        request_from_swagger = request.headers.get('referer').endswith('docs') if request.headers.get('referer') else False
        request_from_redoc = request.headers.get('referer').endswith('redoc') if request.headers.get('referer') else False
        if request_from_swagger or request_from_redoc:
            return {'access_token': access_token, 'token_type': 'Bearer'}
        return response_200(
            data={'access_token': access_token, 'token_type': 'Bearer'},
            message='登录成功'
        )
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@loginController.post("/getLoginUserInfo", response_model=CurrentUserInfoServiceRSModel)
async def get_login_user_info(request: Request, current_user: CurrentUserInfoServiceRSModel = Depends(get_current_user)):
    try:
        return response_200(data=current_user, message="获取成功")
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))


@loginController.post("/resetPassword", response_model=CrudRSModel)
@log_decorator(title="用户登录", business_type=0, log_type='operation')
async def reset_user_pwd(request: Request, reset_user: ResetUserRQModel, query_db: Session = Depends(get_db)):
    try:
        reset_user_result = await reset_password_services(request, query_db, reset_user)
        if reset_user_result.is_success:
            return response_200(data=reset_user_result, message=reset_user_result.message)
        else:
            return response_400(data="", message=reset_user_result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data="", message=str(e))