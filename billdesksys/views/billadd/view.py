#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 09:49:22    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 09:49:22 


import random

import dash
from dash import  html, get_asset_url, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
import datetime
import uuid
import time

def render_content(options_add_modal, bill_card_datas):
    doc_content = fuc.FefferyDiv([
        
        dcc.Store(id='billAdd-store-billCardDataChangeFlag', storage_type='session', data=False),
        
        fac.AntdSpace(
            [
                fuc.FefferyDiv([
                    fac.AntdButton(
                        fac.AntdText('+ 新增账单', strong=True,
                                     style={'font-size': '28px', 'color': 'white', 'font-family': 'HeiTi'}),
                        type='text',
                        id='billAdd-button-addNewBill'
                    ),
                ],
                    shadow="hover-shadow",
                    style={
                        'width': '300px',
                        'height': '132px',
                        'backgroundImage': 'url({})'.format(get_asset_url(f'imgs/banner01.png')),
                        'backgroundRepeat': 'no-repeat',
                        'backgroundSize': 'cover',
                        'border-radius': '25px',
                        'padding': '8px 8px 8px 8px',
                        'justify-content': 'center',
                        'align-items': 'center',
                        'display': 'flex'
                    })

            ] +
            ([
                render_bill_card_content(bill_data=bill_data) for bill_data in bill_card_datas
             ]
                if bill_card_datas else []
            ),
            id='billAdd-billCard-container',
            wrap=True,
            size=28,
        ),


        ## 注入弹出记录更改modal
        fac.AntdModal(children=render_bill_add_modal_content(options=options_add_modal),
                      title=html.Span([fac.AntdIcon(icon='md-extension', style={'marginRight': '4px'}), '新增账单']),
                      width=800,
                      id=f'billAdd-modal-addBillData',
                      visible=False,
                      # loading=True,
                      ),


    ],
        # shadow="hover-shadow-light",
        style={'paddingLeft':'10vw',
               'paddingRight':'10vw',
               'paddingTop': '2vh',
               }
    )

    return doc_content


def render_bill_card_content(bill_data):
    if bill_data is None:
        bill_data = {'banner_id':1, 'bill_name':'测试', 'pay_channel':'测试', 'settle_channel':'测试','bill_status':'正常',
                     'bill_amount':1.2,'bill_date':'2024.8.1'}

    icon_class_name = 'custom-icon custom-icon-billstatus-zhengchang' if bill_data.get('bill_status') == '正常' else 'custom-icon custom-icon-billstatus-tuikuan'

    return fuc.FefferyDiv([    
        fac.AntdRow([
            fac.AntdCol([
                html.I(className=icon_class_name,
                        style={'color': 'white', 'font-size': '24px', 'padding':'4px 0px 0px 4px'}),
                fac.AntdText(f'￥ {bill_data.get("bill_amount"):.02f}',
                                style={'font-family': 'DingTalkTi', 'font-size': '24px', 'color': 'white',
                                    'textAlign': 'center', 'margin-top':'4px' }),
                fac.AntdText(bill_data.get('bill_name')[:5], strong=True,
                                style={'font-family': 'HeiTi', 'font-size': '32px', 'color': 'white',
                                    'textAlign': 'center', 'margin-top':'0px'})
            ],
                span=14,
                style={'display': 'flex', 'flex-direction': 'column', },
            ),

            fac.AntdCol([
                fac.AntdText('账单日期', style={'font-family': 'DingTalkTi', 'color': 'white'}),
                fac.AntdText(bill_data.get('bill_date'), style={'color': 'white', 'padding-left':'24px'}),
                fac.AntdText('支付渠道', style={'font-family': 'DingTalkTi', 'color': 'white'}),
                fac.AntdText(bill_data.get('pay_channel'), style={'color': 'white', 'padding-left':'24px'}),
                fac.AntdText('结算渠道', style={'font-family': 'DingTalkTi', 'color': 'white'}),
                fac.AntdText(bill_data.get('settle_channel'), style={'color': 'white', 'padding-left':'24px'}),
            ],
                span=10,
                style={'display': 'flex', 'flex-direction': 'column', },
            ),
        ])

        ],
        shadow="hover-shadow",
        style={
            'width':'300px',
            'backgroundImage': 'url({})'.format(get_asset_url(f'imgs/banner{bill_data.get("banner_id"):02d}.png')),
            'backgroundRepeat': 'no-repeat',
            'backgroundSize': 'cover',
            'border-radius': '25px',
            'padding':'8px 8px 8px 8px',
        }
    )


def render_bill_add_modal_content(options=None):
    if options is None:
        options = {
            'bill_name':{'options':[], 'options_extra':None, 'default':''},
            'pay_channel':{'options':[], 'options_extra':None, 'default':''},
            'settle_channel':{'options':[], 'options_extra':None, 'default':''},
            'bill_object':{'options':[], 'default':''},
            'bill_scene':{'options':[], 'default':''},
            'bill_status':{'check':{'icon':'', 'color':''},
                           'uncheck':{'icon':'', 'color':''},}
        }


    return fac.AntdForm([
            fac.AntdRow([
                fac.AntdCol([

                    fac.AntdFormItem(
                        children=fac.AntdSwitch(
                            id='billadd-switch-bill-status',
                            checked=True
                        ),
                        hidden=True
                    ),


                    fac.AntdButton(
                        html.I(className=options.get('bill_status').get('check').get('icon'),
                               style={'color':options.get('bill_status').get('check').get('color'), 'font-size':'24px'},
                               id='billAdd-I-billStatusIcon'),
                        type='text',
                        shape='circle',
                        id='billadd-button-bill-status',
                    ),

                ],

                    span=24,
                    style={'textAlign':'right'}
                ),

                fac.AntdCol([
                        fac.AntdFormItem(
                            fac.AntdCalendar(
                                id='billadd-calendar-bill-date',
                                defaultValue=f'{datetime.datetime.now():%Y-%m-%d}',
                                style={'width': '80%' }
                            ),
                            id='billadd-formitem-bill-date',
                            label=fac.AntdText('账单日期',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            required=True,

                        ),

                        fac.AntdFormItem(
                            children=fac.AntdTreeSelect(
                                id='billadd-treeselect-bill-name',
                                placeholder='请选择账单',
                                treeDefaultExpandAll=True,
                                treeNodeFilterMode='regex',
                                treeData=options.get('bill_name').get('options'),
                                treeNodeKeyToTitle=options.get('bill_name').get('options_extra'),
                                defaultValue=options.get('bill_name').get('default'),
                                # treeData=[
                                #     {'key': 'Ch1', 'value': 'Ch1', 'title': '类型A',
                                #      'children': [
                                #          {'key': 'Ch1-1', 'value': 'Ch1-1', 'title': '账单A1'},
                                #          {'key': 'Ch1-2', 'value': 'Ch1-2', 'title': '账单A2'},
                                #      ]},
                                #     {'key': 'Ch2', 'value': 'Ch2', 'title': '类型B',
                                #      'children': [
                                #          {'key': 'Ch2-1', 'value': 'Ch2-1', 'title': '账单B1'},
                                #          {'key': 'Ch2-2', 'value': 'Ch2-2', 'title': '账单B2'},
                                #          {'key': 'Ch2-3', 'value': 'Ch2-3', 'title': '账单B3'},
                                #      ]},
                                #
                                # ],
                                style={'width': '80%'},
                            ),
                            id='billadd-formitem-bill-name',
                            label=fac.AntdText('账单类型',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            wrapperCol={'offset': 2, 'span': 20},
                            required=True,
                            # validateStatus='error',
                        ),

                        fac.AntdFormItem(
                            fac.AntdInputNumber(
                                id='billadd-inputnumber-bill-amount',
                                addonAfter='¥',
                                min=0,
                                precision=2,
                                # controls=True,
                                step=0.01,
                                style={'width': '80%'},
                            ),
                            id='billadd-formitem-bill-amount',
                            label=fac.AntdText('账单金额',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            wrapperCol={'offset':2, 'span':20},
                            required=True
                        ),

                ],
                span=12,
                ),

                fac.AntdCol([
                        fac.AntdFormItem(
                            children=fac.AntdTreeSelect(
                                id='billadd-treeselect-pay-channel',
                                placeholder='请选择支付渠道',
                                treeDefaultExpandAll=True,
                                treeData=options.get('pay_channel').get('options'),
                                treeNodeKeyToTitle=options.get('pay_channel').get('options_extra'),
                                defaultValue=options.get('pay_channel').get('default'),
                                # treeData=[
                                #     {'key': 'Ch1', 'value': 'Ch1', 'title': '渠道1',
                                #      'children': [
                                #          {'key': 'Ch1-1', 'value': 'Ch1-1', 'title': '渠道1-1'},
                                #          {'key': 'Ch1-2', 'value': 'Ch1-2', 'title': '渠道1-2'},
                                #      ]},
                                #     {'key': 'Ch2', 'value': 'Ch2', 'title': '渠道2',
                                #      'children': [
                                #          {'key': 'Ch2-1', 'value': 'Ch2-1', 'title': '渠道2-1'},
                                #          {'key': 'Ch2-2', 'value': 'Ch2-2', 'title': '渠道2-2'},
                                #          {'key': 'Ch2-3', 'value': 'Ch2-3', 'title': '渠道2-3'},
                                #      ]},
                                #
                                # ],
                                style={'width': '80%'},
                            ),
                            id='billadd-formitem-pay-channel',
                            label=fac.AntdText('支付渠道',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            wrapperCol={'offset': 2, 'span': 20},
                            required=True
                        ),

                        fac.AntdFormItem(
                            children=fac.AntdTreeSelect(
                                id='billadd-treeselect-settle-channel',
                                placeholder='请选择结算渠道',
                                treeDefaultExpandAll=True,
                                treeData=options.get('settle_channel').get('options'),
                                treeNodeKeyToTitle=options.get('settle_channel').get('options_extra'),
                                defaultValue=options.get('settle_channel').get('default'),
                                # treeData=[
                                #     {'key': 'Ch1', 'value': 'Ch1', 'title': '渠道1',
                                #      'children': [
                                #          {'key': 'Ch1-1', 'value': 'Ch1-1', 'title': '渠道1-1'},
                                #          {'key': 'Ch1-2', 'value': 'Ch1-2', 'title': '渠道1-2'},
                                #      ]},
                                #     {'key': 'Ch2', 'value': 'Ch2', 'title': '渠道2',
                                #      'children': [
                                #          {'key': 'Ch2-1', 'value': 'Ch2-1', 'title': '渠道2-1'},
                                #          {'key': 'Ch2-2', 'value': 'Ch2-2', 'title': '渠道2-2'},
                                #          {'key': 'Ch2-3', 'value': 'Ch2-3', 'title': '渠道2-3'},
                                #      ]},
                                #
                                # ],
                                style={'width': '80%'},
                            ),
                            id='billadd-formitem-settle-channel',
                            label=fac.AntdText('结算渠道',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            wrapperCol={'offset': 2, 'span': 20},
                            required=True
                        ),



                        fac.AntdFormItem(
                            children=fac.AntdRadioGroup(
                                id='billadd-radiogroup-bill-object',
                                options=options.get('bill_object').get('options'),
                                defaultValue=options.get('bill_object').get('default'),
                                # options=[{'label':f'obj{i}', 'value':f'对象{i}'} for i in range(6)],
                                style={'width': '80%'},
                            ),
                            id='billadd-formitem-bill-object',
                            label=fac.AntdText('消费对象',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            wrapperCol={'offset': 2, 'span': 20},
                            required=True
                        ),

                        fac.AntdFormItem(
                            children=fac.AntdRadioGroup(
                                id='billadd-radiogroup-bill-scene',
                                options=options.get('bill_scene').get('options'),
                                defaultValue=options.get('bill_scene').get('default'),
                                # defaultValue='工作',
                                # options=[{'label': f'obj{i}', 'value': f'obj{i}'} for i in range(2)],
                                style={'width': '80%'},
                            ),
                            id='billadd-formitem-bill-scene',
                            label=fac.AntdText('消费场景',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            wrapperCol={'offset': 2, 'span': 20},
                            required=True
                        ),

                        fac.AntdFormItem(
                            children=fac.AntdInput(
                                id='billadd-input-remark',
                                mode='text-area',
                                autoSize={'minRows': 5, 'maxRows': 5},
                                style={'width': '100%'},

                            ),
                            id='billadd-formitem-remark',
                            label=fac.AntdText('备注',
                                               style={'fontFamily': 'DingTalkTi',
                                                      'fontSize': '16px'}),
                            wrapperCol={'offset': 2, 'span': 20},
                            # required=True
                        ),

                ],
                span=12,
                ),

                fac.AntdCol([
                    fac.AntdSpace([
                        fac.AntdButton('重置',
                                       id='billadd-button-reset',
                                       type='dashed', danger=True,
                                       icon=fac.AntdIcon(icon='md-highlight-off'),
                                       style={'fontFamily': 'DingTalkTi'}
                                       ),
                        fac.AntdButton('提交',
                                       id='billadd-button-submit',
                                       type='primary',
                                       icon=fac.AntdIcon(icon='md-launch'),
                                       style={'background':'black', 'fontFamily': 'DingTalkTi'},
                                       ),
                    ],
                    size=30),
                ],
                    style={'textAlign': 'right', 'paddingRight':'4.2%'},
                    span=24,
                ),


            ],

            ),

        ],
            id='billAdd-form-billInfo',
            layout='vertical',
            enableBatchControl=True,
            style={'width': '100%', 'marginTop': '20px'},
        )





from server import app
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash import set_props
import json
from flask import session


from api.apis import add_bill_api, get_bills_api
from views.view_utils import transform_bill_card_data


# ## ======== JS 设置各表单组件中的选择项 ========
# app.clientside_callback(
#     '''( nClicks, configData ) => {
#     if ( nClicks ) {
#         if (configData){
#             return [configData.bill_name, configData.pay_channel, configData.settle_channel, configData.bill_object, configData.bill_scene];
#         }
#     }
#     return [[], [], [], [], []];
#
#     }''',
#     [Output('billadd-treeselect-bill-name', 'treeData'),
#      Output('billadd-treeselect-pay-channel', 'treeData'),
#      Output('billadd-treeselect-settle-channel', 'treeData'),
#      Output('billadd-radiogroup-bill-object', 'options'),
#      Output('billadd-radiogroup-bill-scene', 'options')
#      ],
#     Input('billAdd-button-addNewBill', 'nClicks'),
#     State('bill-dict-data-config', 'data'),
#     prevent_initial_call=True,
# )




# ##======== PY 设置各表单组件中的选择项 ========
# @app.callback(
#     [Output('billadd-treeselect-bill-name', 'treeData'),
#      Output('billadd-treeselect-pay-channel', 'treeData'),
#      Output('billadd-treeselect-settle-channel', 'treeData'),
#      Output('billadd-radiogroup-bill-object', 'options'),
#      Output('billadd-radiogroup-bill-scene', 'options'),
#      ],
#     Input('billAdd-button-addNewBill', 'nClicks'),
#     State('bill-dict-data-config', 'data'),
#     prevent_initial_call=True,
# )
# def change_form_options(nClicks, configData):
#     if nClicks:
#         if configData:
#             return [configData.get('bill_name'), configData.get('pay_channel'), configData.get('settle_channel'),
#                     configData.get('bill_object'), configData.get('bill_scene'),]
#     return [[], [], [], [], []]


@app.callback(
    [Output('billAdd-billCard-container', 'children', allow_duplicate=True),
     Output('billAdd-store-billCardDataChangeFlag', 'data', allow_duplicate=True),],
    Input('billAdd-store-billCardDataChangeFlag', 'data'),
    prevent_initial_call=True
)
def update_bill_cards(change_flag):
    if change_flag:
        get_bills_res = get_bills_api(page_obj={'user_id':session['user_id'], 'theme_id':session['theme_id'], 'n_limit':15})
        bill_card_datas = transform_bill_card_data(get_bills_res['data']) if get_bills_res['code'] == 200 else []
        
        return [
            [
                fuc.FefferyDiv([
                    fac.AntdButton(
                        fac.AntdText('+ 新增账单', strong=True,
                                     style={'font-size': '28px', 'color': 'white', 'font-family': 'HeiTi'}),
                        type='text',
                        id='billAdd-button-addNewBill'
                    ),
                ],
                    shadow="hover-shadow",
                    style={
                        'width': '300px',
                        'height': '132px',
                        'backgroundImage': 'url({})'.format(get_asset_url(f'imgs/banner01.png')),
                        'backgroundRepeat': 'no-repeat',
                        'backgroundSize': 'cover',
                        'border-radius': '25px',
                        'padding': '8px 8px 8px 8px',
                        'justify-content': 'center',
                        'align-items': 'center',
                        'display': 'flex'
                    }), ] +  [
                render_bill_card_content(bill_data=bill_data) for bill_data in bill_card_datas
             ],
             False
        ]

    return [dash.no_update, False]



## ======== JS 检查账单日期输入准确 ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="checkBillDateStatus"),
    Output('billadd-formitem-bill-date', 'validateStatus'),
    Input('billadd-calendar-bill-date', 'value'),
    prevent_initial_call = True
)


## ======== JS 检验账单金额的填写框是否符合规范 ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="checkBillAmountStatus"),
    [Output('billadd-formitem-bill-amount', 'validateStatus'),
     Output('billadd-formitem-bill-amount', 'help'),],
    Input('billadd-inputnumber-bill-amount', 'value'),
    prevent_initial_call = True
)

## ======== JS 检查账单名称输入准确 ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="checkBillNameStatus"),
    [Output('billadd-formitem-bill-name', 'validateStatus'),
     Output('billadd-formitem-bill-name', 'help'),],
    Input('billadd-treeselect-bill-name', 'value'),
    prevent_initial_call = True
)

## ======== JS 检查账单场景输入准确 ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="checkBillSceneStatus"),
    [Output('billadd-formitem-bill-scene', 'validateStatus'),
     Output('billadd-formitem-bill-scene', 'help'),],
    Input('billadd-radiogroup-bill-scene', 'value'),
    prevent_initial_call = True
)

## ======== JS 弹出添加账单的MODAL ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="showModalAddBill"),
    Input('billAdd-button-addNewBill', 'nClicks'),
    prevent_initial_call = True
)



## ======== JS 初始化添加账单对话框的数据 ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="initAddBillData"),
    [Output('billAdd-form-billInfo', 'values', allow_duplicate=True),
     Output('billadd-switch-bill-status', 'checked', allow_duplicate=True)],
    Input('billAdd-modal-addBillData', 'visible'),
    prevent_initial_call=True
)

## ======== JS 重置添加账单对话框的数据 ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="resetAddBillData"),
    [Output('billAdd-form-billInfo', 'values', allow_duplicate=True),
     Output('billadd-switch-bill-status', 'checked', allow_duplicate=True)],
    Input('billadd-button-reset', 'nClicks'),
    prevent_initial_call=True
)


## ======== PY 提交账单填写的数据 ========
@app.callback(
    [Output('billAdd-modal-addBillData', 'visible', allow_duplicate=True),
     Output('billAdd-modal-addBillData', 'key', allow_duplicate=True),
     Output('billAdd-store-billCardDataChangeFlag', 'data'),
     Output('global-message-container', 'children', allow_duplicate=True)],
    Input('billadd-button-submit', 'nClicks'),
    [State('billAdd-form-billInfo', 'values'),
     State('billadd-switch-bill-status', 'checked'),
     State('billAdd-store-billCardDataChangeFlag', 'data')],
    prevent_initial_call=True
)
def submit_form_values(nClicks, values, checked, add_flag):
    if nClicks:

        record = {
            'bill_id': uuid.uuid4().hex,
            'bill_type': values.get('billadd-treeselect-bill-name')[0],
            'bill_name': values.get('billadd-treeselect-bill-name'),
            'pay_channel': values.get('billadd-treeselect-pay-channel'),
            'settle_channel': values.get('billadd-treeselect-settle-channel'),
            'consume_object': values.get('billadd-radiogroup-bill-object'),
            'bill_scene': values.get('billadd-radiogroup-bill-scene'),
            'bill_status': '00' if checked else '01',
            'bill_amount': values.get('billadd-inputnumber-bill-amount'),
            'bill_date': values.get('billadd-calendar-bill-date') if values.get('billadd-calendar-bill-date') else f"{datetime.datetime.today():%Y-%m-%d}",
            'remark': values.get('billadd-input-remark') if values.get('billadd-input-remark') else '',
            'user_id': session['user_id'],
            'theme_id': session['theme_id'],
            'into_unix_time':int(time.time()) ,
        }


        add_bill_res = add_bill_api(page_obj=record)

        if add_bill_res['code'] != 200:
                return [
                    True,
                    dash.no_update,
                    False,
                    fuc.FefferyFancyMessage('新增账单' + add_bill_res['message'], type='error')
                ]

        return [
            False,
            uuid.uuid4().hex ,
            True,                
            fuc.FefferyFancyMessage(add_bill_res['message'], type='success')
        ]


    return [dash.no_update, dash.no_update, False, dash.no_update]



## ======== JS 切换账单状态的图标 ========
app.clientside_callback(
    ClientsideFunction(namespace="billAdd", function_name="switchBillStatusIcon"),
    Output('billadd-switch-bill-status', 'checked'),
    Input('billadd-button-bill-status', 'nClicks'),
    [State('billadd-switch-bill-status', 'checked'),
     State('bill-dict-options-config', 'data')],
    prevent_initial_call = True
)

#
# app.clientside_callback(
#     '''( nClicks, checked ) => {
#     if ( nClicks ) {
#         checked = !checked
#
#         if ( checked ){
#             window.dash_clientside.set_props(
#                 "billAdd-I-billStatusIcon",
#                 {
#                     "class": 'custom-icon custom-icon-billstatus-zhengchang',
#                     "style" : {'color': 'green', 'font-size': '24px'}
#                 }
#             )
#         }
#         else {
#             window.dash_clientside.set_props(
#                 "billAdd-I-billStatusIcon",
#                 {
#                     "class": 'custom-icon custom-icon-billstatus-tuikuan',
#                     "style" : {'color': 'red', 'font-size': '24px'}
#                 }
#             )
#         }
#
#     }
#     return checked;
#     }''',
#     Output('billadd-switch-bill-status', 'checked'),
#     Input('billadd-button-bill-status', 'nClicks'),
#     State('billadd-switch-bill-status', 'checked'),
#     prevent_initial_call=True
# )

# ## ======== PY 切换账单状态的图标 ========
# @app.callback(
#     Output('billadd-switch-bill-status', 'checked'),
#     Input('billadd-button-bill-status', 'nClicks'),
#     State('billadd-switch-bill-status', 'checked'),
#     prevent_initial_call=True,
# )
# def check(nclicks, checked):
#     if nclicks:
#         checked = not checked
#
#         if checked:
#             set_props(
#                 'billadd-button-bill-status',
#                 {'children':html.I(className='custom-icon custom-icon-billstatus-zhengchang',
#                               style={'color': 'green', 'font-size': '24px'})}
#             )
#
#         else:
#             set_props(
#                 'billadd-button-bill-status',
#                 {'children':html.I(className='custom-icon custom-icon-billstatus-tuikuan',
#                               style={'color': 'red', 'font-size': '24px'})}
#             )
#
#
#     return checked