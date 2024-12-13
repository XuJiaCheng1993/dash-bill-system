#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from config.dbconfig import Base, SessionLocal, engine

def get_db_pro():
    """每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接

    Yields:
        _type_: _description_
    """
    current_db = SessionLocal()
    try:
        yield current_db
    finally:
        current_db.close()


async def init_create_table():
    """应用启动时初始化数据库连接"""    
    # logger.info("初始化数据库连接...")
    Base.metadata.create_all(bind=engine)
    # logger.info("数据库连接成功")


get_db = get_db_pro