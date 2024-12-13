#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from module.entity import SysUserMapping


def login_by_account(db: Session, user_name: str):
    """
    根据用户名查询用户信息
    :param db: orm对象
    :param user_name: 用户名
    :return: 用户对象
    """
    user = (
        db.query(SysUserMapping)
        .filter(SysUserMapping.user_name == user_name)
        .first()
        )

    return user



if __name__ == '__main__':
    from config.dbconfig import SessionLocal

    db = SessionLocal()
    theme = login_by_account(db, 'admin')
    db.close()

