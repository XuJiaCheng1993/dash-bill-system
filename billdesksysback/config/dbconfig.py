#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy import create_engine, MetaData, URL
from sqlalchemy.orm import sessionmaker, declarative_base
from config.env import DataBaseConfig
from urllib.parse import quote_plus



# ## 创建数据库链接PGSQL
# SQLALCHEMY_DATABASE_URL = URL.create(
#     'postgresql+psycopg2',
#     username=DataBaseConfig.USERNAME,
#     password=DataBaseConfig.PASSWORD,
#     host=DataBaseConfig.HOST,
#     port=DataBaseConfig.PORT,
#     database=DataBaseConfig.DB,
#     query={'options': f"-c search_path={DataBaseConfig.SCHEMANAME}"}
# )

## 创建数据库链接MYSQL
SQLALCHEMY_DATABASE_URL = URL.create(
    'mysql+pymysql',
    username=DataBaseConfig.USERNAME,
    password=DataBaseConfig.PASSWORD,
    host=DataBaseConfig.HOST,
    port=DataBaseConfig.PORT,
    database=DataBaseConfig.DB
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    echo=False,
    max_overflow=5,
    pool_size=5,
    pool_recycle=3600,
    pool_timeout=30,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()