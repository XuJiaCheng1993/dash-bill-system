#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import datetime
import dash
from dash import html, get_asset_url
import feffery_antd_components as fac
import feffery_utils_components as fuc
from flask import session

ROLECOLOR = {'A1': 'magenta', 'C1': 'gold', 'C2': 'geekblue'}
ROLE = {'A1': '管理员', 'C1': 'VIP用户', 'C2': '平台用户'}

def render_content():
    docs_content =  html.Div(
        [
            dcc.Store(id='index-store-passwordCheckStatus', data={'status': {'check_new_1':False, 'check_old':False, 'check_new_2':False}}),

            fac.AntdFlex([
                fuc.FefferyDiv(style={'width':'35%'}),
                fac.AntdMenu(
                    id=f'menu',
                    menuItems=[
                        {'component': 'SubMenu',
                         'props': {'key': f'billAdd', 'title': f'账单录入', 'icon': 'antd-app-store-add','href':'billadd'}},
                        {'component': 'SubMenu',
                         'props': {'key': f'billAnalysis', 'title': f'账单分析', 'icon':'antd-home','href':'billhome'}},
                        {'component': 'SubMenu',
                         'props': {'key': f'billManage', 'title': f'账单管理', 'icon': 'antd-app-store','href':'billmanage'}},
                    ],
                    currentKey='billAdd',
                    mode='horizontal',
                    style={'width':'360px'}
                ),
                fuc.FefferyDiv([
                    fac.AntdButton(
                        fac.AntdAvatar(
                            id='user-avatar',
                            size='small',
                            mode='image',
                            src='/assets/imgs/default_avatar.jpg'
                        ),
                        id='index-btn-show-dropdown-user-manage',
                        type='text'
                    ),
                    fuc.FefferyDiv(id='index-user-manage-menu')
                ],
                    style={'width':'30%',
                           'textAlign':'right',
                           'alignSelf':'center',
                           'marginRight':'3vw'}),


            ],
                justify='space-between',
                style={'Height':'100px'}
            ),

        ## 挂载页面信息
        fuc.FefferyDiv(id='docs-content'),


        # ## 挂载修改配置信息的modal
        # fac.AntdModal(id=f'index-modal-revise-config',
        #               title=html.Span(
        #                   [fac.AntdIcon(icon='md-settings', style={'marginRight': '4px'}), '修改配置信息']),
        #               width=800,
        #               children=modal_content_revise_config(),
        #               ),


        ## 挂载修改账户信息的modal
        fac.AntdModal(id=f'index-modal-revise-account-info',
                      title=html.Span(
                          [fac.AntdIcon(icon='md-people', style={'marginRight': '4px'}), '修改账户信息']),
                      width=800,
                      children=modal_content_revise_account_info(),
                      ),

        ## 挂载修改账户密码的modal
        fac.AntdModal(id=f'index-modal-revise-password',
                      title=html.Span(
                          [fac.AntdIcon(icon='md-extension', style={'marginRight': '4px'}), '重置账户密码']),
                      width=800,
                      children=modal_content_revise_password(),
                      ),


        ],

    )
    return docs_content


def modal_content_revise_config():
    return fuc.FefferyDiv([
        fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdAvatar(
                    id='user-avatar',
                    size=128,
                    mode='image',
                    src='/assets/imgs/default_avatar.jpg'),
                style={'textAlign':'center'},
            ),

            fac.AntdFormItem(
                fac.AntdText('王大春', style={'fontSize':'24px'}),
                style={'textAlign': 'center'},
            ),


            fac.AntdFormItem(
                fac.AntdSelect(
                    placeholder='请选择账单主题',
                    id='select-revise-config',
                    options=[f'选项{i}' for i in range(1, 6)]
                ),
            ),


            fac.AntdFormItem(
                fac.AntdButton(
                    '更新配置',
                    id='btn-revise-config-submit',
                    type='primary',
                    loadingChildren='配置更新中',
                    autoSpin=True,
                    block=True,
                    size='large',
                ),
                style={
                    'marginTop': '20px'
                }
            )
        ],
        layout='vertical',
        style={
            'width': '100%',
            'marginTop': '20px'
        }
    ),
    ])


def modal_content_revise_account_info():
    return fuc.FefferyDiv([
        fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdAvatar(
                    id='index-avatar-userAvatar',
                    size=128,
                    mode='image',
                    src='/assets/imgs/default_avatar.jpg'),
                style={'textAlign':'center'},
            ),

            fac.AntdFormItem(
                fac.AntdSpace([
                    fac.AntdText(
                        session['user_name'],
                        id='index-text-username',
                        style={'fontSize': '24px'}),

                    fac.AntdTag(
                        content=ROLE.get(session['role'].rstrip()),
                        color=ROLECOLOR.get(session['role'].rstrip()),
                        bordered=False,
                        id='index-tag-userrole',
                        style={'fontSize': '10px'}
                    ),

                ],
                    size=0
                ),
                style={'textAlign': 'center'},
            ),

            # fac.AntdFormItem(
            #     fac.AntdInput(
            #         size='large',
            #         id='index-input-userId',
            #         prefix=fac.AntdIcon(icon='antd-user'),
            #         value=session['user_id'],
            #         disabled=True
            #     ),
            # ),

            fac.AntdRow([
                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInput(
                            value=session['user_nick'],
                            id='index-input-reviseUserNick',
                            size='large',
                            prefix=fac.AntdIcon(icon='antd-user'),
                        ),
                        help="请输入修改后的用户昵称",
                    ),

                    fac.AntdFormItem(
                        fac.AntdInput(
                            value=session['phone_number'],
                            id='index-input-revisePhoneNumber',
                            size='large',
                            prefix=fac.AntdIcon(icon='antd-mobile'),
                        ),
                        id='index-formItem-phoneNumber',
                        hasFeedback=True,
                        validateStatus='validating',
                        help="请输入修改后的手机号",
                    ),

                    fac.AntdFormItem(
                        fac.AntdInput(
                            value=session['email'],
                            id='index-input-reviseEmail',
                            size='large',
                            prefix=fac.AntdIcon(icon='md-email'),
                        ),
                        id='index-formItem-email',
                        hasFeedback=True,
                        validateStatus='validating',
                        help="请输入修改后的电子邮箱",
                    ),

                ],
                    span=14),

                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInput(
                            value=session['industry'],
                            id='index-input-reviseIndustry',
                            size='large',
                            prefix=fac.AntdIcon(icon='antd-schedule'),
                        ),
                        help="请输入修改后的所属行业",
                    ),

                    fac.AntdFormItem(
                        fac.AntdInput(
                            value=session['job'],
                            id='index-input-reviseJob',
                            size='large',
                            prefix=fac.AntdIcon(icon='antd-crown'),
                        ),
                        help="请输入修改后的职业",
                    ),

                ],
                    offset=2,
                    span=8),

            ]),


            fac.AntdFormItem(
                fac.AntdButton(
                    '修改信息',
                    id='index-button-submitReviseUserInfo',
                    type='primary',
                    loadingChildren='信息修改中',
                    autoSpin=True,
                    block=True,
                    size='large',
                ),
                style={
                    'marginTop': '20px'
                }
            )
        ],
        layout='vertical',
        style={
            'width': '100%',
            'marginTop': '20px'
        }
    ),
    ])


def modal_content_revise_password():
    return fuc.FefferyDiv(
        fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdAvatar(
                    id='index-avatar-userAvatar',
                    size=128,
                    mode='image',
                    src='/assets/imgs/default_avatar.jpg'),
                style={'textAlign':'center'},
            ),

            fac.AntdFormItem(
                fac.AntdSpace([
                    fac.AntdText(
                        session['user_nick'],
                        id='index-text-username',
                        style={'fontSize': '24px'}),

                    fac.AntdTag(
                        content=ROLE.get(session['role'].rstrip()),
                        color=ROLECOLOR.get(session['role'].rstrip()),
                        bordered=False,
                        id='index-tag-userrole',
                        style={'fontSize': '10px'}
                    ),

                ],
                    size=0
                ),
                style={'textAlign': 'center'},
            ),



            fac.AntdFormItem(
                fac.AntdInput(
                    placeholder='请输入旧密码',
                    id='index-input-resetPasswordOldPassword',
                    mode='password',
                    passwordUseMd5=True,
                    size='large',
                    prefix=fac.AntdIcon(
                        icon='antd-lock'
                    ),
                ),
                id='index-formItem-oldPassword',
                hasFeedback=True,
                validateStatus='error',
                help='未输入旧密码',

            ),
            fac.AntdFormItem(
                fac.AntdInput(
                    placeholder='请输入新密码',
                    id='index-input-resetPasswordNewPasswordFirst',
                    mode='password',
                    passwordUseMd5=True,
                    size='large',
                    prefix=fac.AntdIcon(
                        icon='antd-lock'
                    ),
                ),
                id='index-formItem-newPasswordFirst',
                hasFeedback=True,
                validateStatus='error',
                help='未输入新密码',
            ),
            fac.AntdFormItem(
                fac.AntdInput(
                    placeholder='请再次输入新密码',
                    id='index-input-resetPasswordNewPasswordAgain',
                    mode='password',
                    passwordUseMd5=True,
                    size='large',
                    prefix=fac.AntdIcon(
                        icon='antd-lock'
                    ),
                ),
                id='index-formItem-newPasswordAgain',
                hasFeedback=True,
                validateStatus='error',
                help='未输入新密码',
            ),
            fac.AntdFormItem(
                fac.AntdButton(
                    '重置密码',
                    id='index-button-submitResetPassword',
                    type='primary',
                    loadingChildren='密码重置中',
                    autoSpin=True,
                    block=True,
                    size='large',
                ),
                style={
                    'marginTop': '20px'
                }
            )
        ],
        layout='vertical',
        style={
            'width': '100%',
            'marginTop': '20px'
        }
    ),

    )



from server import app
from dash.dependencies import Input, Output, State, ClientsideFunction
import uuid
from dash import dcc
from flask import session
from api.apis import reset_password_api, edit_user_info_api, get_current_user_info_api


## 弹出修改用户信息和重置密码的modal
app.clientside_callback(
    ClientsideFunction(namespace="PlatformManage", function_name="showReviseResetUserInfoModal"),
    [Output('index-modal-revise-account-info', 'visible', allow_duplicate=True),
     Output('index-modal-revise-password', 'visible'),],
    [Input('index-dropdown-user-manage-menu', 'clickedKey'),
     Input('index-dropdown-user-manage-menu', 'nClicks')],
    prevent_initial_call=True
)


## 检验旧密码是否符合规范
app.clientside_callback(
    ClientsideFunction(namespace="PlatformManage", function_name="checkPasswordRule"),
    [Output('index-formItem-oldPassword', 'validateStatus'),
     Output('index-formItem-oldPassword', 'help')],
    Input('index-input-resetPasswordOldPassword', 'value'),
    prevent_initial_call=True
)

## 检验新设置的密码是否符合规范
app.clientside_callback(
    ClientsideFunction(namespace="PlatformManage", function_name="checkPasswordRule"),
    [Output('index-formItem-newPasswordFirst', 'validateStatus'),
     Output('index-formItem-newPasswordFirst', 'help')],
    Input('index-input-resetPasswordNewPasswordFirst', 'value'),
    prevent_initial_call=True
)


## 检验两次输入的密码是否一致
app.clientside_callback(
    ClientsideFunction(namespace="PlatformManage", function_name="checkPassword1and2"),
    [Output('index-formItem-newPasswordAgain', 'validateStatus'),
     Output('index-formItem-newPasswordAgain', 'help'),],
    [Input('index-input-resetPasswordNewPasswordAgain', 'value'),
    Input('index-input-resetPasswordNewPasswordFirst', 'value'),],
    prevent_initial_call=True
)

## 检验是否是中国大陆手机号
app.clientside_callback(
    ClientsideFunction(namespace="PlatformManage", function_name="checkPhoneNumberRule"),
    [Output('index-formItem-phoneNumber', 'validateStatus'),
     Output('index-formItem-phoneNumber', 'help'),],
    Input('index-input-revisePhoneNumber', 'value'),
    prevent_initial_call=True
)


## 检验是否是中国大陆手机号
app.clientside_callback(
    ClientsideFunction(namespace="PlatformManage", function_name="checkEmailRule"),
    [Output('index-formItem-email', 'validateStatus'),
     Output('index-formItem-email', 'help'),],
    Input('index-input-reviseEmail', 'value'),
    prevent_initial_call=True
)



# 退出登录回调
@app.callback(
    [Output('redirect-container', 'children', allow_duplicate=True),
     Output('token-store', 'data', allow_duplicate=True)],
    [Input('index-dropdown-user-manage-menu', 'nClicks'),
     Input('index-dropdown-user-manage-menu', 'clickedKey')],
    prevent_initial_call=True
)
def logout_confirm(nClicks, clickedKey):
    if nClicks:
        if clickedKey == 'log-out':
            session.clear()
            return [
                dcc.Location(
                    pathname='/login',
                    id='index-redirect'
                ),
                None
            ]

    return [dash.no_update] * 2



@app.callback(
    Output('index-user-manage-menu', 'children'),
    Input('index-btn-show-dropdown-user-manage', 'nClicks'),
    State('global-mouse-position', 'position'),
    prevent_initial_call=True
)
def show_drop(nClicks, position):
    if nClicks:
        return fac.AntdDropdown(
            id='index-dropdown-user-manage-menu',
            key=str(uuid.uuid4()),
            visible=True,
            freePosition=True,
            freePositionStyle={
                'left': position['clientX'],
                'top': position['clientY']
            },
            menuItems=[
                {'title': f'注销用户', 'key': f'log-out', 'icon': 'md-exit-to-app'},
                {'isDivider': True},
                {'title': f'更改配置', 'key': f'revise-config', 'icon':'md-settings', 'href':'/config'},
                {'isDivider': True},
                {'title': f'修改信息','key': f'revise-account', 'icon':'md-people'},
                {'isDivider':True},
                {'title':'重置密码', 'key':'revise-password', 'icon':'md-extension'}
            ],
            trigger='click'
        )

    return dash.no_update





## 重置密码
@app.callback(
    [Output('index-button-submitResetPassword', 'loading'),
     Output('redirect-container', 'children', allow_duplicate=True),
     Output('token-store', 'data', allow_duplicate=True),
     Output('global-message-container', 'children', allow_duplicate=True)],
    Input('index-button-submitResetPassword', 'nClicks'),
    [State('index-input-resetPasswordOldPassword', 'value'),
     State('index-input-resetPasswordNewPasswordFirst', 'value'),
     State('index-formItem-oldPassword', 'validateStatus'),
     State('index-formItem-newPasswordFirst', 'validateStatus'),
     State('index-formItem-newPasswordAgain', 'validateStatus'),],
    prevent_initial_call=True
)
def reset_user_password(nClicks, old_password, new_password, check_old, check_new_1, check_new_2):
    if all([nClicks, old_password, new_password, check_old, check_new_1, check_new_2]):
        if check_old == 'success' and check_new_1 == 'success' and check_new_2 == 'success':
            try:
                reset_password_res = reset_password_api(page_obj=dict(user_id=session['user_id'], old_password=old_password, new_password=new_password) )
                if reset_password_res['code'] == 200 :
                    session.clear()
                    return [
                        False,
                        dcc.Location(
                            pathname='/login',
                            id='index-redirect'
                        ),
                        None,
                        fuc.FefferyFancyMessage('密码修改成功，已登出请重新登录', type='success')
                    ]
                else:
                    return [False, dash.no_update, dash.no_update, fuc.FefferyFancyMessage(reset_password_res['message'], type='error')]

            except:
                return [False, dash.no_update, dash.no_update, fuc.FefferyFancyMessage('接口异常！', type='error')]

        return [False, dash.no_update, dash.no_update, fuc.FefferyFancyMessage('密码长度应至少大于6位，且不能包含特殊字符！', type='error')]

    return [False, dash.no_update, dash.no_update, None]


## 修改用户信息
@app.callback(
    [Output('index-button-submitReviseUserInfo', 'loading'),
     Output('index-modal-revise-account-info', 'visible', allow_duplicate=True),
     Output('global-message-container', 'children', allow_duplicate=True)],
    Input('index-button-submitReviseUserInfo', 'nClicks'),
    [State('index-input-reviseUserNick', 'value'),
     State('index-input-revisePhoneNumber', 'value'),
     State('index-input-reviseEmail', 'value'),
     State('index-input-reviseIndustry', 'value'),
     State('index-input-reviseJob', 'value'),
     State('index-formItem-phoneNumber', 'validateStatus'),
     State('index-formItem-email', 'validateStatus')],
    prevent_initial_call=True
)
def edit_user_info(nClicks, user_nick, phone_number, email, industry, job, check_phone, check_email):
    if nClicks:
        if check_email == 'error' or check_phone == 'error':
            return [False, True, fuc.FefferyFancyMessage('请填写正确的手机号和电子邮件地址', type='error')]

        user_info = {'user_id':session['user_id']}
        [user_info.update({k:v})
         for k, v in zip(['user_nick', 'phone_number', 'email', 'industry', 'job'], [user_nick, phone_number, email, industry, job])
         if v ]

        try:
            edit_res = edit_user_info_api(page_obj=user_info)
            if edit_res['code'] != 200:       
                return [False, True, fuc.FefferyFancyMessage(edit_res['message'], type='error')]
            
            if edit_res['code'] == 200:

                ## 在session 中更新最新的用户信息
                get_user_res = get_current_user_info_api()
                if get_user_res['code'] == 200 :
                    for ky, vl in get_user_res["data"].items():
                        session[ky] = vl
                
                return [
                    False,
                    False,
                    fuc.FefferyFancyMessage("用户信息修改成功", type='success')
                ]
            
        except:
            return [False, True, fuc.FefferyFancyMessage("接口异常", type='error')]


    return [False, False, None]