#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import os

class PathConfig:

    # 项目绝对根目录
    ABS_ROOT_PATH = os.path.abspath(os.getcwd())


class RouterConfig:

    # 合法pathname列表
    BASIC_VALID_PATHNAME = [
        '/', '/login', '/forget'
    ]

    # 静态路由列表
    STATIC_VALID_PATHNAME = ['/', '/login', '/forget', '/user/profile']


class ApiBaseUrlConfig:

    # api基本url
    BaseUrl = 'http://127.0.0.1:8880'