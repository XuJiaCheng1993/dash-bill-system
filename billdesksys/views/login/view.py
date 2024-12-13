#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import dash
from dash import html, get_asset_url, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc

def render_content(is_captcha=True, is_forget=False):
    doc_content = html.Div([

        fac.Fragment([
            dcc.Store('login-store-checkCaptcha', data=False),
            html.Div(id='login-message-container'),
        ]),

        fac.AntdCard([
            fac.AntdForm([
                fac.AntdFormItem(
                    fac.AntdAvatar(
                        id='login-avatar-user',
                        size=128,
                        mode='image',
                        src='/assets/imgs/default_avatar.jpg'),
                    style={'textAlign': 'center'},
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        placeholder='请输入用户名',
                        id='login-input-username',
                        size='large',
                        prefix=fac.AntdIcon(icon='antd-user'),
                    ),
                    id='login-formitem-username',
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        placeholder='请输入密码',
                        id='login-input-password',
                        mode='password',
                        passwordUseMd5=True,
                        size='large',
                        prefix=fac.AntdIcon(icon='antd-lock'),
                    ),
                    id='login-formitem-password',
                ),

                html.Div([
                    fac.AntdSpace([
                        fac.AntdFormItem(
                            fac.AntdInput(
                                placeholder='请输入验证码',
                                id='login-input-captcha',
                                size='large',
                                # status='error',
                                # prefix=fac.AntdIcon(icon='antd-check-circle'),
                                style={'width': '210px'}
                            ),
                            id='login-formitem-captcha',
                            validateStatus='error',
                            help='未输入验证码！',
                            hasFeedback=True,
                        ),

                        fac.AntdFormItem(
                                fuc.FefferyCaptcha(
                                    id='login-captcha-image',
                                    height=37,
                                    width=100,
                                ),
                        ),
                    ],
                        align='end',
                        size=10
                    ),
                ],
                    # id='captcha-row-container',
                    hidden= not is_captcha
                ),

                fac.AntdSpace([
                    # html.Div(id='test'),
                    fac.AntdButton(
                        '忘记密码',
                        id='forget-password-link',
                        type='link',
                        href='/forget',
                        target='_self'
                    )
                ],
                    align='center',
                    size=240
                ) if is_forget else [],

                fac.AntdFormItem(
                    fac.AntdButton(
                        '登录',
                        id='login-button-submit',
                        type='primary',
                        loadingChildren='登录中',
                        autoSpin=True,
                        block=True,
                        size='large',
                        disabled=False,
                    ),
                    style={'marginTop': '20px'}
                )
            ],
                layout='vertical',
                style={'width': '100%'}
            ),
        ],
            id='login-form-container',
            title=fac.AntdText('登录', strong=True, style={'fontSize': '24px'}),
            headStyle={'textAlign':'center'},
            hoverable=True,
            style={
                'position': 'fixed',
                'top': '16%',
                'left': '70%',
                'width': '430px',
                'padding': '0px 30px',
                'transform': 'translateX(-50%)'
            }
        ),

        fac.AntdFooter(
            html.Div(
                fac.AntdText(
                    '版权所有©2024 Billsys',
                    style={'margin': '0'}
                ),
                style={
                    'display': 'flex',
                    'height': '100%',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            style={
                'backgroundColor': 'rgb(255 255 255 / 0%)',
                'height': '40px',
                'position': 'fixed',
                'bottom': 0,
                'left': '50%',
                'width': '500px',
                'padding': '20px 50px',
                'transform': 'translateX(-50%)'
            }
        ),
    ],
        id='container',
        style={
            'height': '100vh',
            'backgroundImage': 'url({})'.format(get_asset_url('imgs/login_background.png')),
            'backgroundRepeat': 'no-repeat',
            'backgroundSize': 'cover'
        }
    )

    return doc_content



from server import app
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash import set_props
import json
from api.apis import (login_api, get_current_user_info_api, get_bill_dict_code_list_api, get_current_user_theme_infos_api, get_market_theme_infos_api)

from dash import dcc
from flask import session


app.clientside_callback(
    ClientsideFunction(namespace="Login", function_name="checkCaptcha"),
    [Output('login-formitem-captcha', 'validateStatus'),
     Output('login-formitem-captcha', 'help'),
     Output('login-store-checkCaptcha', 'data')],
    Input('login-input-captcha', 'value'),
    State('login-captcha-image', 'captcha'),
    prevent_initial_call=True
)


@app.callback(
    [Output('login-button-submit', 'loading'),
    Output('token-store', 'data'),
    Output('redirect-container', 'children', allow_duplicate=True),
    Output('global-message-container', 'children', allow_duplicate=True)],
    Input('login-button-submit', 'nClicks'),
    [State('login-input-username', 'value'),
     State('login-input-password', 'value'),
     State('login-store-checkCaptcha', 'data')],
    prevent_initial_call=True
)
def user_login(nClicks, username, password, checkCaptcha):
    if nClicks:
        if not checkCaptcha:
            return [False, None, None, fuc.FefferyFancyMessage("验证码错误", type='error')]
        
        if all([username, password]):
     
            login_res = login_api(page_obj=dict(username=username, password=password))

            if login_res.get('code') != 200:
                return [False, None, None, fuc.FefferyFancyMessage("登录" + login_res.get('message'), type='error')]
                
            ## 登录成功获取用户Token    
            token = login_res.get('data').get('access_token')
            session['Authorization'] = token

            ## 根据token获取用户信息
            get_user_res = get_current_user_info_api()
            
            if get_user_res['code'] != 200 :
                return  [False, None, None, fuc.FefferyFancyMessage("获取用户信息" + get_user_res.get('message'), type='error')]
            
            for ky, vl in get_user_res["data"].items():
                session[ky] = vl
            
            
            ## 获取用户已关联和未关联的账单主题信息
            get_current_theme_infos_res =  get_current_user_theme_infos_api()   
            get_market_theme_infos_res = get_market_theme_infos_api()          
            theme_market_data = {
                'SELF':get_current_theme_infos_res['data'] if get_current_theme_infos_res['code'] == 200 else [], 
                'OTHER':get_market_theme_infos_res['data'] if get_market_theme_infos_res['code'] == 200 else [],
                }
            
            set_props(
                'bill-theme-market-info',
                {'data':theme_market_data}
            )

            ## 获取账单字典数据
            get_bill_code_list_res = get_bill_dict_code_list_api(theme_id=session['theme_id'] )
            bill_dict_data = get_bill_code_list_res['data'] if get_bill_code_list_res["code"] == 200 else []
            set_props(
                'bill-dict-data-store',
                {'data': bill_dict_data}               
            )

            
            return [False, token, dcc.Location(pathname='/', id='login-redirect'),
                    fuc.FefferyFancyMessage('登录成功', type='success')]
                

    return [False, None, None, None]

