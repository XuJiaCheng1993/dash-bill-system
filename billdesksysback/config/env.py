#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 


class DataBaseConfig:
    """
    MYSQL数据库配置
    """
    HOST: str = '192.168.244.129'
    PORT: int = 3306
    USERNAME: str = 'root'
    PASSWORD: str = '123456'
    DB: str = 'billwebsys'



## 生成Jwt key
# import secrets
# keys = secrets.token_hex(32)

class JwtConfig:
    """
    Jwt配置
    """
    jwt_secret_key: str = '67abac984bbd185132da708de23afba6b26cb7773153a438e7e7a5f468b9e9f7'
    jwt_algorithm: str = 'HS256'
    jwt_expire_minutes: int = 1440
    jwt_redis_expire_minutes: int = 60


class RedisConfig:
    """
    Redis配置
    """
    redis_host: str = '192.168.244.129'
    redis_port: int = 6379
    redis_username: str = ''
    redis_password: str = '112233'
    redis_database: int = 3