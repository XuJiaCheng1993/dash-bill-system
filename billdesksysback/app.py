#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 


from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from module.controller.billdict_controller import billDictController
from module.controller.login_controller import loginController
from module.controller.user_controller import userController
from module.controller.billtheme_controller import billThemeController
from module.controller.bill_controller import billController
from module.controller.billanalysis_controller import billAnalysisController

from fastapi.exceptions import HTTPException
from utils.response import AuthException, PermissionException, response_401, response_403, JSONResponse,jsonable_encoder

from config.get_redis import RedisUtil
from config.get_db import init_create_table
from utils.log import logger


app = FastAPI(
    title='BILLWEBSYSAPI',
    description=f'BillWebSys接口文档',
    version='0.0.1',
    root_path='',
)

# 前端页面url
origins = [
    "http://localhost:19880",
    "http://127.0.0.1:19880",
]

# 后台api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logger.info(f"项目开始启动")
    # worship()
    await init_create_table()
    app.state.redis = await RedisUtil.create_redis_pool()
    # await RedisUtil.init_sys_dict(app.state.redis)
    # await RedisUtil.init_sys_config(app.state.redis)
    logger.info(f"项目启动成功")


@app.on_event("shutdown")
async def shutdown_event():
    await RedisUtil.close_redis_pool(app)



# 自定义token检验异常
@app.exception_handler(AuthException)
async def auth_exception_handler(request: Request, exc: AuthException):
    return response_401(data=exc.data, message=exc.message)


# 自定义权限检验异常
@app.exception_handler(PermissionException)
async def permission_exception_handler(request: Request, exc: PermissionException):
    return response_403(data=exc.data, message=exc.message)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        content=jsonable_encoder({"message": exc.detail, "code": exc.status_code}),
        status_code=exc.status_code
    )



app.include_router(loginController, prefix="/login", tags=['登录模块'])
app.include_router(userController, prefix="/user", tags=['用户管理模块'])
app.include_router(billDictController, prefix="/billDict", tags=['账单字典管理模块'])
app.include_router(billThemeController, prefix="/billTheme", tags=['账单主题管理模块'])
app.include_router(billController, prefix="/bill", tags=['账单管理模块'])
app.include_router(billAnalysisController, prefix="/billAnalysis", tags=['账单分析模块'])

if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host='127.0.0.1',
        port=8880,
        # reload=True
    )
