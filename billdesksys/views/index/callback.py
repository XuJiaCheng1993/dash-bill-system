#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

from dash import dcc
from server import app
from dash.dependencies import Input, Output, State
# from flask_login import logout_user


# @app.callback(
#     Output('index-redirect-container', 'children'),
#     Input('index-header-dropdown', 'clickedKey'),
# )
# def relogin(clickedKey):
#     if clickedKey == '退出登录':
#         logout_user()
#         return dcc.Location(pathname='/login', id='jsc_report_monitor-redirect')
#     return None
#
#
#
# ## 全屏化
# app.clientside_callback(
#     '''(nClicks, isFullscreen) => {
#         return !isFullscreen;
#     }''',
#     Output('index-full-screen', 'isFullscreen'),
#     Input('index-full-screen-button', 'nClicks'),
#     State('index-full-screen', 'isFullscreen'),
#     prevent_initial_call=True
# )


# ## 折叠侧边连
# app.clientside_callback(
#     '''(nClicks, collapsed) => {
#         return [!collapsed, collapsed ? 'antd-menu-fold' : 'antd-menu-unfold'];
#     }''',
#     [Output('index-sider', 'collapsed'),
#      Output('index-menu-fold-icon', 'icon')],
#     Input('index-menu-fold-button', 'nClicks'),
#     State('index-sider', 'collapsed'),
#     prevent_initial_call=True
# )

#
# ## 刷新页面
# app.clientside_callback(
#     '''() => {return 'location.reload(true);'}''',
#     Output('execute-js-output', 'jsString'),
#     Input('index-page-refresh-button', 'nClicks'),
#     prevent_initial_call=True
# )
