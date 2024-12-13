#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 09:49:29    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 09:49:29 

import os
import dash
import feffery_antd_components as fac
import feffery_utils_components as fuc
from server import app, server
from dash import html, dcc, set_props
from dash.dependencies import Input, Output, State, ALL
from views import (index, billadd, billhome, billmanage, login, config)
from flask import session

app.layout = html.Div(
    [
        # 注入url监听
        fuc.FefferyLocation(id='url-container'),
        # 用于回调菜单内的pathname信息
        dcc.Location(id='dcc-url', refresh=False),

        fuc.FefferyMousePosition(
            id='global-mouse-position'
        ),

        # 注入js执行容器
        fuc.FefferyExecuteJs(
            id='execute-js-container'
        ),

        # 注入页面内容挂载点
        html.Div(id='app-mount'),

        # 注入全局配置容器
        fac.AntdConfigProvider(id='app-config-provider'),

        ## 挂载配置缓存
        fac.Fragment([
            dcc.Store(id='bill-dict-options-config'),
            dcc.Store(id='bill-dict-data-store', storage_type='session'),
            dcc.Store(id='token-store', storage_type='session'),
            dcc.Store(id='bill-theme-market-info', storage_type='session'),                       
        ]),
        

        # 辅助处理多输入 -> 存储接口返回token校验信息
        # render_store_container(),

        # 重定向容器
        html.Div(id='redirect-container'),

        # 登录消息失效对话框提示
        fac.AntdModal(
            html.Div(
                [
                    fac.AntdIcon(icon='fc-high-priority', style={'font-size': '28px'}),
                    fac.AntdText('用户信息已过期，请重新登录', style={'margin-left': '5px'}),
                ]
            ),
            id='token-invalid-modal',
            visible=False,
            title='提示',
            renderFooter=True,
            centered=True
        ),

        # 注入全局消息提示容器
        html.Div(id='global-message-container'),
        # 注入全局通知信息容器
        html.Div(id='global-notification-container'),


        # 关闭浏览器的清理组件
        fuc.FefferyListenUnload(id='listen-unload'),
    ]
)

from api.apis import get_current_user_info_api, get_bills_api
from views.view_utils import get_bill_form_options_from_bill_dict_data, get_bill_config_table_data_from_bill_dict_data, transform_bill_card_data

@app.callback(
    [Output('docs-content', 'children'),
     Output('menu', 'currentKey')],
    Input('dcc-url', 'pathname'),
    [State('bill-dict-data-store', 'data'),
     State('bill-theme-market-info', 'data'),],
)
def menu_router(pathname, bill_dict_data, theme_market_data):
    ''' 菜单路由回调'''
    if pathname in ['/billadd', '/billmanage']:
        ## 将账单字典转换成选项，并存入缓存
        bill_dict_options = get_bill_form_options_from_bill_dict_data(bill_dict_data)
        set_props(
                'bill-dict-options-config',
                {'data':bill_dict_options}
            )

        if pathname == '/billadd':
            get_bills_res = get_bills_api(page_obj={'user_id':session['user_id'], 'theme_id':session['theme_id'], 'n_limit':15})
            bill_card_data = transform_bill_card_data(get_bills_res['data']) if get_bills_res['code'] == 200 else []
            
            return [billadd.render_content(options_add_modal=bill_dict_options, bill_card_datas=bill_card_data), 'billAdd']
        else:
            return [billmanage.render_content(bill_dict_options=bill_dict_options), 'billManage']
        
    elif pathname ==  '/billhome':
        return [billhome.render_content(), 'billAnalysis']
    elif pathname ==  '/billmanage':
        return [billmanage.render_content(bill_dict_options=bill_dict_options), 'billManage']
    elif pathname == '/config':
                
        return [config.render_content(code_items_data=get_bill_config_table_data_from_bill_dict_data(bill_dict_data),
                                      theme_market_data=theme_market_data), dash.no_update]

    else:
        return [billhome.render_content(), 'billAnalysis']


## 当桌面端启动时才需要
@app.callback(
    Output('platform-content', 'children', allow_duplicate=True),  # 无用
    Input('listen-unload', 'unloaded'),
    prevent_initial_call=True
)
def listen_unload_demo(unloaded):
    ''' 退出清理资源，如页面全部退出，自动停止服务'''
    if unloaded:
        os._exit(0)
    return dash.no_update






@app.callback(
    [Output('app-mount', 'children'),
     Output('redirect-container', 'children', allow_duplicate=True),
     Output('global-message-container', 'children', allow_duplicate=True)
     ],
    Input('url-container', 'pathname'),
    [State('url-container', 'trigger'),
     State('token-store', 'data'),],
    prevent_initial_call=True
)
def render_docs_content(pathname, url_trigger, session_token):
    ''' 路由回调'''
    # 检查当前会话是否已经登录
    token_result = session.get('Authorization')
    valid_href_list = ['/', '/home', '', '/billadd', '/billhome', '/billmanage', '/config', '/login', '/forget']



    

    # 若已登录
    if token_result and session_token and token_result == session_token:
        ## TOken过期，退出到登录界面
        get_user_res = get_current_user_info_api()
        if get_user_res["code"] == 401:
            session.clear()
            return [dash.no_update, dcc.Location(pathname='/login', id='router-redirect'), fuc.FefferyFancyMessage("Token已失效，请重新登录", type='error')]

        if pathname in valid_href_list:
            if url_trigger == 'load':
                # 根据pathname控制渲染行为
                if pathname == '/login' or pathname == '/forget':
                    # 重定向到主页面
                    return [dash.no_update,dcc.Location(pathname='/', id='router-redirect'),None,]

                # 否则正常渲染主页面
                return [index.render_content(),None,None]

            else:
                return [dash.no_update,None,None]

        else:
            # 渲染404状态页
            return [fac.AntdResult(status='404', title='缺少访问权限') ,None, None]


    else:
        # 若未登录
        # 根据pathname控制渲染行为
        # 检验pathname合法性
        # if pathname not in valid_href_list:
        #     # 渲染404状态页
        #     return [fac.AntdResult(status='404', title='缺少访问权限') ,None, None]

        if pathname == '/login':
            return [login.render_content(), None, None]

        # if pathname == '/forget':
        #     return [login.render_content(), None, None]

        # 否则重定向到登录页
        return [dash.no_update,dcc.Location(pathname='/login', id='router-redirect'),None]






if __name__ == '__main__':

    # from models.dbconfig import Base, engine
    # from models.entity.do.user_do import *
    # from models.entity.do.billdict_do import *
    # from models.entity.do.bill_do import *
    #
    #
    # Base.metadata.create_all(bind=engine)

    #

    app.run_server(port=19880,
                   debug=True,
                   # host='0.0.0.0'
                   )




