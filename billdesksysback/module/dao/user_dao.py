#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from sqlalchemy.orm import Session
from module.entity import SysUserMapping, SysUserBillThemeMapping, UserThemeRelationModel, SysUserModel
from utils.utils import list_format_datetime

class UserDao:
    """
    用户管理模块数据库操作层
    """
    @classmethod
    def query_user_by_name(cls, db: Session, user_name: str):
        """
        根据用户名获取用户信息
        :param db: orm对象
        :param user_name: 用户名
        :return: 当前用户名的用户信息对象
        """
        user_info = (
            db.query(SysUserMapping)
            .filter(SysUserMapping.user_name == user_name)
            .first()
        )
        return user_info


    @classmethod
    def query_user_by_id(cls, db: Session, user_id: str):
        """
        根据用户id获取用户信息
        :param db: orm对象
        :param user_name: 用户名
        :return: 当前用户名的用户信息对象
        """
        user_info = (
            db.query(SysUserMapping)
            .filter(SysUserMapping.user_id == user_id)
            .first()
        )
        return user_info



    @classmethod
    def update_user(cls, db: Session, user: dict):
        """
        编辑用户数据库操作
        :param db: orm对象
        :param user: 需要更新的用户字典
        :return: 编辑校验结果
        """
        (
            db.query(SysUserMapping)
            .filter(SysUserMapping.user_id == user.get("user_id"))
            .update(user)
         )


    @classmethod
    def query_user_theme_relation_by_id(self, db: Session, user_id:str, theme_id:int):
        """_summary_

        Args:
            db (Session): orm对象
            user_id (str): 用户ID
            theme_id (int): 账单主题ID

        Returns:
            _type_: 当前用户与账单主题的关联信息对象
        """        
        relation_info = (
            db.query(SysUserBillThemeMapping)
            .filter(SysUserBillThemeMapping.user_id == user_id,
                    SysUserBillThemeMapping.theme_id == theme_id)
            .first()
        )
        return relation_info

    @classmethod
    def query_user_theme_relations_by_user_id(self, db: Session, user_id:str):
        relations = (
            db.query(SysUserBillThemeMapping)
            .filter(SysUserBillThemeMapping.user_id == user_id)
            .all()
        )
        return list_format_datetime(relations)


    @classmethod
    def query_all_user_theme_relations(self, db: Session):
        relations = (
            db.query(SysUserBillThemeMapping)
            .all()
        )
        return list_format_datetime(relations)
    

    @classmethod
    def insert_user_theme_relation(self, db: Session, relation:UserThemeRelationModel):
        data = SysUserBillThemeMapping(**relation.dict())
        db.add(data)
        db.flush()
        return data



    @classmethod
    def delete_user_theme_relation(self, db: Session, user_id:str, theme_id:int):
        (
            db.query(SysUserBillThemeMapping)
            .filter(SysUserBillThemeMapping.user_id == user_id,
                    SysUserBillThemeMapping.theme_id == theme_id)
            .delete()
         )