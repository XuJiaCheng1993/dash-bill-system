#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import datetime

def query_to_dict(q) -> dict:
    """_summary_

    Args:
        q (_type_): _description_

    Returns:
        dict: _description_
    """    
    if hasattr(q, '__table__'):
        return {c.name: getattr(q, c.name) for c in q.__table__.columns}


def list_format_datetime(lst, fmt='%Y-%m-%d %H:%M:%S') -> list:
    """_summary_

    Args:
        lst (_type_): _description_
        fmt (str, optional): _description_. Defaults to '%Y-%m-%d %H:%M:%S'.

    Returns:
        list: _description_
    """    
    for obj in lst:
        for attr in dir(obj):
            value = getattr(obj, attr)
            if isinstance(value, datetime.datetime):
                setattr(obj, attr, value.strftime(fmt))
    return lst
