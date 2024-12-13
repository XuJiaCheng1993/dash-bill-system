#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import datetime

from sqlalchemy.orm import Session
from module.entity import UserLoginRQModel, CurrentUserInfoServiceRSModel, ResetUserRQModel, CrudRSModel, SysUserModel

from module.dao import UserDao, login_by_account


from config.env import JwtConfig
from jose import JWTError, jwt
from passlib.context import CryptContext
from config.get_db import get_db
from fastapi import Depends, Request, Form

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from typing import Union, Optional


from utils.response import AuthException, LoginException
from utils.utils import query_to_dict

from utils.log import logger
import traceback


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/loginByAccount")


class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    """
    自定义OAuth2PasswordRequestForm类，增加会话编号参数
    """
    def __init__(
            self,
            grant_type: str = Form(default=None, regex="password"),
            username: str = Form(),
            password: str = Form(),
            scope: str = Form(default=""),
            client_id: Optional[str] = Form(default=None),
            client_secret: Optional[str] = Form(default=None),
            session_id: Optional[str] = Form(default=""),
    ):
        super().__init__(grant_type=grant_type, username=username, password=password,
                         scope=scope, client_id=client_id, client_secret=client_secret)
        self.session_id = session_id


async def get_current_user(request: Request = Request, token: str = Depends(oauth2_scheme),
                           result_db: Session = Depends(get_db)):
    """
    根据token获取当前用户信息
    """
    if token.startswith('Bearer'):
        token = token.split(' ')[1]
        
    try:
        payload = jwt.decode(token, JwtConfig.jwt_secret_key, algorithms=[JwtConfig.jwt_algorithm])
        user_id: str = payload.get("user_id")
        session_id: str = payload.get("session_id")

        if user_id is None:
            raise AuthException(data="", message="用户token不合法")
        
    except JWTError:
        raise AuthException(data="", message="用户token已失效，请重新登录")


    user = UserDao.query_user_by_id(result_db, user_id=user_id)
    if user is None:
        raise AuthException(data="", message="用户token不合法")

    redis_token = await request.app.state.redis.get(f"access_token:{user.user_id}")

    if token == redis_token:
        await request.app.state.redis.set(f"access_token:{user.user_id}", redis_token,
                                          ex=datetime.timedelta(minutes=JwtConfig.jwt_redis_expire_minutes))

        return CurrentUserInfoServiceRSModel(
            user_id = user.user_id,
            user_name = user.user_name,
            user_nick = user.user_nick,
            phone_number = user.phone_number,
            email = user.email,
            role = user.role,
            industry = user.industry,
            job = user.job,
            theme_id = user.theme_id,
        )
    else:
        raise AuthException(data="", message="用户token已失效，请重新登录")



async def authenticate_user(request: Request, query_db: Session, login_user: UserLoginRQModel):
    """ 
    用户登录鉴权 
    """
    user = login_by_account(query_db, user_name=login_user.user_name)

    if not user:
        raise LoginException(data="", message="用户不存在")

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    if not pwd_context.verify(login_user.password, user.password):
        raise LoginException(data="", message="密码不正确")

    if user.status == '0':
        raise LoginException(data="", message="用户已停用")

    return user


def create_access_token(data: dict, expires_delta: Union[int, None] = 15):
    """
    根据登录信息创建当前用户token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JwtConfig.jwt_secret_key, algorithm=JwtConfig.jwt_algorithm)
    return encoded_jwt


async def reset_password_services(request: Request, result_db: Session, forget_user: ResetUserRQModel):
    """
    用户重置密码服务
    """
    ## 查询用户信息
    user = UserDao.query_user_by_id(result_db, user_id=forget_user.user_id)

    ## 查询不到用户
    if not user:
        return CrudRSModel(is_success=False, message='未知用户ID')

    ## 验证密码是否正确
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    if not pwd_context.verify(forget_user.old_password, user.password):
        return CrudRSModel(is_success=False, message='旧密码错误')

    ## 验证新旧密码是否相同
    if pwd_context.verify(forget_user.new_password, user.password):
        return CrudRSModel(is_success=False, message='新密码不能与旧密码相同')

    ## 数据库操作
    try:
        user = query_to_dict(user)
        user.update({'password': pwd_context.hash(forget_user.new_password),
                     'update_time':datetime.datetime.now()})
        UserDao.update_user(result_db, user)
        result_db.commit()
        result = dict(is_success=True, message='密码重置成功')
    except:
        logger.error(traceback.format_exc())
        result_db.rollback()
        result = dict(is_success=False, message=f"数据库操作异常")

    return CrudRSModel(**result)

# async def logout_services(request: Request, user_id: str):
#     """
#     退出登录services
#     :param request: Request对象
#     :param session_id: 会话编号
#     :return: 退出登录结果
#     """
#     await request.app.state.redis.delete(f"access_token:{user_id}")

#     return True