#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:20:32    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:20:32 

from api.request import api_request

## ========================================== 登录接口 ==========================================================================
def login_api(page_obj: dict):
    return api_request(method='post', url='/login/loginByAccount', is_headers=False, data=page_obj)

def get_current_user_info_api():
    return api_request(method='post', url='/login/getLoginUserInfo', is_headers=True)

def reset_password_api(page_obj: dict):
    return api_request(method='post', url='/login/resetPassword', is_headers=True, json=page_obj)


## ========================================== 用户管理接口 ==========================================================================
def edit_user_info_api(page_obj:dict):
    return api_request(method='patch', url='/user/editUser', is_headers=True, json=page_obj)

def get_current_user_theme_infos_api():
    return api_request(method='post', url='/user/getUserThemeRelations', is_headers=True)

def get_market_theme_infos_api():
    return api_request(method='post', url='/user/getUserThemeRelationsExcludeUser', is_headers=True)


def add_user_theme_relation_api(theme_id:int):
    return api_request(method='post', url='/user/addRelationUserTheme', is_headers=True, params={'theme_id':theme_id})

## ========================================= 账单管理接口 ===========================================================================
def get_bill_by_id_api(bill_id:str):
    return api_request(method='post', url=f'/bill/getBillById', is_headers=True, params={'bill_id': bill_id})

def get_bills_api(page_obj:dict):
    return api_request(method='post', url='/bill/getBillTableData', is_headers=True, json=page_obj)

def add_bill_api(page_obj:dict):
    return api_request(method='post', url='/bill/addBill', is_headers=True, json=page_obj)

def edit_bill_api(page_obj:dict):
    return api_request(method='patch', url='/bill/editBill', is_headers=True, json=page_obj)

def del_bill_api(bill_id:str):
    return api_request(method='post', url='/bill/delBill', is_headers=True, params={'bill_id': bill_id})


## ========================================== 账单字典接口 ==========================================================================
def add_bill_dict_code_api(page_obj:dict):
    return api_request(method='post', url='/billDict/addDictCode', is_headers=True, json=page_obj)

def edit_bill_dict_code_api(page_obj:dict):
    return api_request(method='patch', url='/billDict/editDictCode', is_headers=True, json=page_obj)

def del_bill_dict_codes_api(page_obj:dict):
    return api_request(method='post', url='/billDict/delDictCodes', is_headers=True, json=page_obj)

def get_bill_dict_code_by_id_api(code_id:int):
    return api_request(method='post', url='/billDict/getCodeById', is_headers=True, params={'code_id':code_id})

def get_bill_dict_code_by_key_api(theme_id:int, dict_id:str, code_key:str):
    return api_request(method='post', url='/billDict/getCodeByKey', is_headers=True, params={'theme_id':theme_id, 'dict_id':dict_id, 'code_key':code_key})

def get_bill_dict_code_list_api(theme_id:int):
    return api_request(method='post', url='/billDict/getDictCodeList', is_headers=True, params={'theme_id':theme_id})

def check_dict_code_has_bill_api(theme_id:int, dict_id:str, code_key:str):
    return api_request(method='post', url='/billDict/checkCodeItemHasBillData', is_headers=True, params={'theme_id':theme_id, 'dict_id':dict_id, 'code_key':code_key})

## ========================================== 账单主题接口 ==========================================================================
def init_bill_theme_api(page_obj:dict):
    return api_request(method='post', url='/billTheme/initBillTheme', is_headers=True, json=page_obj)

def edit_bill_theme_api(page_obj:dict):
    return api_request(method='patch', url='/billTheme/editBillTheme', is_headers=True, json=page_obj)

def switch_bill_theme_api(theme_id:int):
    return api_request(method='post', url='/billTheme/switchBillTheme', is_headers=True, params={'theme_id':theme_id})

def get_bill_theme_by_id_api(theme_id:int):
    return api_request(method='post', url='/billTheme/getThemeById', is_headers=True, params={'theme_id':theme_id})

def get_bill_theme_by_name_api(theme_name:str):
    return api_request(method='post', url='/billTheme/getThemeByName', is_headers=True, params={'theme_name':theme_name})


## ========================================== 账单分析接口 ==========================================================================
def get_bill_analysis(query_obj:dict, analysis_obj:dict):
    return api_request(method='post', url='/billAnalysis/analyzeBill', is_headers=True, json={'query_bill':query_obj, 'analysis_params':analysis_obj})
