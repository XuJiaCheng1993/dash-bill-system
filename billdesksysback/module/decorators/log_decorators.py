#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from functools import wraps
from fastapi import Request
from fastapi.responses import JSONResponse, ORJSONResponse, UJSONResponse
import inspect
import os
import json
import time
from datetime import datetime
from user_agents import parse
from typing import Optional
from module.service import get_current_user, LogService
from module.entity import SysLoginLogModel, SysOperLogModel


def log_decorator(title: str, business_type: int, log_type: Optional[str] = 'operation'):
    """
    日志装饰器
    :param log_type: 日志类型（login表示登录日志，为空表示为操作日志）
    :param title: 当前日志装饰器装饰的模块标题
    :param business_type: 业务类型（0其它 1新增 2修改 3删除 4分析 5查询 6检验）
    :return:
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            # 获取被装饰函数的文件路径
            file_path = inspect.getfile(func)
            # 获取项目根路径
            project_root = os.getcwd()
            # 处理文件路径，去除项目根路径部分
            relative_path = os.path.relpath(file_path, start=project_root)[0:-2].replace('\\', '.')
            # 获取当前被装饰函数所在路径
            func_path = f'{relative_path}{func.__name__}()'
            # 获取上下文信息
            request: Request = kwargs.get('request')
            token = request.headers.get('Authorization')
            query_db = kwargs.get('query_db')
            request_method = request.method
            operator_type = 'ot'
            user_agent = request.headers.get('User-Agent')
            if "Windows" in user_agent or "Macintosh" in user_agent or "Linux" in user_agent:
                operator_type = 'pc'
            if "Mobile" in user_agent or "Android" in user_agent or "iPhone" in user_agent:
                operator_type = 'mob'
            # 获取请求的url
            oper_url = request.url.path

            # 获取请求的ip及ip归属区域
            oper_ip = request.headers.get('remote_addr')
            oper_ip = '127.0.0.1' if oper_ip is None else oper_ip


            # 根据不同的请求类型使用不同的方法获取请求参数
            content_type = request.headers.get("Content-Type")
            oper_param = ''
            if content_type:
                if ("multipart/form-data" in content_type or 'application/x-www-form-urlencoded' in content_type):
                    payload = await request.form()
                    oper_param = "\n".join([f"{key}: {value}" for key, value in payload.items()])
                else:
                    payload = await request.body()
                    oper_param = json.dumps(json.loads(str(payload, 'utf-8')), ensure_ascii=False)
            # 日志表请求参数字段长度最大为2000，因此在此处判断长度
            if len(oper_param) > 2000:
                oper_param = f'[参数过长被截断]{oper_param[:1990]}'


            # 获取操作时间
            oper_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 此处在登录之前向原始函数传递一些登录信息，用于监测在线用户的相关信息
            login_log = {}
            if log_type == 'login':
                user_agent_info = parse(user_agent)
                browser = f'{user_agent_info.browser.family} {user_agent_info.browser.version[0]}'
                system_os = f'{user_agent_info.os.family} {user_agent_info.os.version[0]}'
                login_log = dict(
                    ipaddr=oper_ip,
                    browser=browser,
                    os=system_os,
                    login_time=oper_time
                )


            # 调用原始函数
            result = await func(*args, **kwargs)


            # 获取请求耗时 单位：毫秒
            cost_time = int(float(time.time() - start_time) * 1000)


            # 判断请求是否来自api文档
            request_from_swagger = request.headers.get('referer').endswith('docs') if request.headers.get('referer') else False
            request_from_redoc = request.headers.get('referer').endswith('redoc') if request.headers.get('referer') else False
            
            # 根据响应结果的类型使用不同的方法获取响应结果参数
            if isinstance(result, JSONResponse) or isinstance(result, ORJSONResponse) or isinstance(result, UJSONResponse):
                result_dict = json.loads(str(result.body, 'utf-8'))
            else:
                if request_from_swagger or request_from_redoc:
                    result_dict = {}
                else:
                    if result.status_code == 200:
                        result_dict = {'code': result.status_code, 'message': '获取成功'}
                    else:
                        result_dict = {'code': result.status_code, 'message': '获取失败'}
            json_result = json.dumps(dict(code=result_dict.get('code'), message=result_dict.get('message')), ensure_ascii=False)

            # 根据响应结果获取响应状态及异常信息
            status = 'S'
            error_msg = ''
            if result_dict.get('code') != 200:
                status = 'F'
                error_msg = result_dict.get('message')


            # 根据日志类型向对应的日志表插入数据
            if log_type == 'login':
                user = kwargs.get('form_data')
                user_name = user.username
                login_log['user_name'] = user_name
                login_log['status'] = status
                login_log['msg'] = error_msg

                LogService.add_login_log_services(query_db, SysLoginLogModel(**login_log))

            else:
                current_user = await get_current_user(request, token, query_db)
                oper_id = current_user.user_id
                oper_name = current_user.user_name

                operation_log = dict(
                    title=title,
                    business_type=business_type,
                    method=func_path,
                    request_method=request_method,
                    operator_type=operator_type,
                    oper_user_id=oper_id,
                    oper_name=oper_name,
                    oper_url=oper_url,
                    oper_ip=oper_ip,
                    oper_param=oper_param,
                    json_result=json_result,
                    status=status,
                    error_msg=error_msg,
                    oper_time=oper_time,
                    cost_time=cost_time
                )
                LogService.add_oper_log_services(query_db, SysOperLogModel(**operation_log))


            return result

        return wrapper

    return decorator
