#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 


import dash
import pandas as pd
from flask import session
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc


def render_content(bill_dict_options):
    if bill_dict_options is None:
        bill_dict_options = {
            'bill_name':{'options':[], 'options_extra':None, 'default':''},
            'pay_channel':{'options':[], 'options_extra':None, 'default':''},
            'settle_channel':{'options':[], 'options_extra':None, 'default':''},
            'bill_object':{'options':[], 'default':''},
            'bill_scene':{'options':[], 'default':''},
            'bill_status':{'check':{'icon':'', 'color':''},
                           'uncheck':{'icon':'', 'color':''},}
        }


    doc_content = fuc.FefferyDiv([
        dcc.Store(id='billManage-store-billDataChangeCountStore', data={"changeCounts":0}),

        ## 条件筛选
        fuc.FefferyDiv([fac.AntdForm([
                fac.AntdSpace([
                    fac.AntdFormItem(
                        fac.AntdDateRangePicker(
                            id='billManage-dateRangePicker-billDate',
                            # placeholder='请选择查询的账单日期范围',
                            allowClear=True,
                            style={'width': '15vw'}
                        ),
                        label=fac.AntdText('日期范围', style={'fontFamily': 'DingTalkTi'}),
                        style={'paddingBottom': '10px'},
                    ),

                    fac.AntdFormItem(
                        fac.AntdSelect(
                            id='billManage-select-billType',
                            options=bill_dict_options.get('bill_type').get('options'),
                            placeholder='请选择查询的账单类型',
                            allowClear=True,
                            style={'width': '15vw'}
                        ),
                        label=fac.AntdText('账单类型', style={'fontFamily': 'DingTalkTi'}),
                        style={'paddingBottom': '10px'},
                    ),

                    fac.AntdFormItem(
                        fac.AntdSelect(
                            id='billManage-select-billStatus',
                            options=bill_dict_options.get('bill_status_select').get('options'),
                            placeholder='请选择查询的账单状态',
                            allowClear=True,
                            style={'width': '15vw'}
                        ),
                        label=fac.AntdText('账单状态', style={'fontFamily': 'DingTalkTi'}),
                        style={'paddingBottom': '10px'},
                    ),

                    fac.AntdFormItem(
                        children=fac.AntdTreeSelect(
                            id='billManage-treeSelect-payChannel',
                            placeholder='请选择查询的支付渠道',
                            treeDefaultExpandAll=False,
                            treeData=bill_dict_options.get('pay_channel').get('options'),
                            treeNodeKeyToTitle=bill_dict_options.get('pay_channel').get('options_extra'),
                            allowClear=True,
                            style={'width': '15vw'}
                        ),
                        label=fac.AntdText('支付渠道',style={'fontFamily': 'DingTalkTi'}),
                        style={'paddingBottom': '10px'},
                    ),

                    fac.AntdFormItem(
                        children=fac.AntdTreeSelect(
                            id='billManage-treeSelect-settleChannel',
                            placeholder='请选择查询的结算渠道',
                            treeDefaultExpandAll=False,
                            treeData=bill_dict_options.get('settle_channel').get('options'),
                            treeNodeKeyToTitle=bill_dict_options.get('settle_channel').get('options_extra'),
                            allowClear=True,
                            style={'width': '15vw'}
                        ),
                        label=fac.AntdText('结算渠道', style={'fontFamily': 'DingTalkTi'}),
                        style={'paddingBottom': '10px'},
                    ),

                    fac.AntdFormItem(
                        fac.AntdButton(
                            '重置条件',
                            id='billManage-button-reset',
                            type='primary',
                            icon=fac.AntdIcon(icon='antd-sync'),
                            style={'fontFamily': 'DingTalkTi'}
                        ),
                        style={'paddingBottom': '10px'},
                    ),


                    fac.AntdFormItem(
                        fac.AntdButton(
                            '查询账单',
                            id='billManage-button-search',
                            type='primary',
                            icon=fac.AntdIcon(icon='antd-search'),
                            style={'fontFamily': 'DingTalkTi'}
                        ),
                        style={'paddingBottom': '10px'},
                    ),


                ],
                    wrap=True
                ),


            ],
                id='billManage-form-queryConditions',
                layout='inline',
                enableBatchControl=True,
            ),
        ]),


        ## 账单展示主题
        fuc.FefferyDiv([
            fac.AntdSpin(
                fac.AntdTable(
                    id='billManage-table-billDetailData',
                    # data=[],
                    columns=[
                        {'dataIndex': 'xh', 'title': '序号', 'width':'6vw', 'renderOptions': {'renderType': 'ellipsis'}, },
                        {'dataIndex': 'bill_name', 'title': '账单名称', 'width':'11vw', 'align':'left'},
                        {'dataIndex': 'bill_date', 'title': '账单日期', 'width': '10vw', 'renderOptions': {'renderType': 'ellipsis'}},
                        {'dataIndex': 'bill_amount', 'title': '账单金额', 'width':'10vw', 'renderOptions': {'renderType': 'ellipsis'}},
                        {'dataIndex': 'bill_status', 'title': '账单状态', 'width':'10vw','renderOptions': {'renderType': 'status-badge'},},
                        {'dataIndex': 'record_time', 'title': '录入时间', 'width':'18vw', 'renderOptions': {'renderType': 'ellipsis'}},
                        {'title': '操作', 'dataIndex': 'operation', 'width': '15vw','renderOptions': {'renderType': 'button'},}
                    ],

                    data=[],
                    bordered=True,
                    pagination={
                        'pageSize': 15,
                        'current': 1,
                        'showSizeChanger': False,
                        'pageSizeOptions': [10, 30, 50, 100],
                        'showQuickJumper': True,
                        'total': 0
                    },
                    mode='server-side',
                    style={'width': '100%',
                           'padding-top': '2vh'
                           },
                ),
                text='数据加载中'
            ),
        ]),

        ## 注入弹出记录更改modal
        fac.AntdModal(children=render_modal_content(options=bill_dict_options),
                      title=html.Span([fac.AntdIcon(icon='md-extension', style={'marginRight': '4px'}), '账单修改']),
                      width=600,
                      id=f'billManage-modal-reviseBillData',
                      visible=False,
                      # loading=True,
                      ),





    ],
    style={'paddingLeft':'10vw',
           'paddingRight':'10vw',
           'paddingTop': '2vh',
           }
    )

    return doc_content



def render_modal_content(options=None):
    return fuc.FefferyDiv([
        fac.AntdForm([
            fac.AntdRow([
                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='billManage-input-billID',
                            disabled=True,
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('账单编号',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),
                ],
                    span=18
                ),

                fac.AntdCol([
                    fac.AntdFormItem(
                        children=fac.AntdSwitch(
                            id='billManage-switch-billStatus',
                            checked=True
                        ),
                        hidden=True
                    ),


                    fac.AntdButton(
                        html.I(className=options.get('bill_status').get('check').get('icon'),
                               style={'color': options.get('bill_status').get('check').get('color'), 'font-size': '24px'},
                               id='billManage-I-billStatusIcon'),
                        type='text',
                        shape='circle',
                        id='billManage-button-billStatus',
                    ),


                ],
                    offset=4,
                    span=2
                ),


                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdDatePicker(
                            id='billManage-dataPicker-billDate',
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('账单日期',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),

                    fac.AntdFormItem(
                        fac.AntdSelect(
                            id='billManage-select-billType',
                            options=options.get('bill_type').get('options'),
                            style={'width': '100%'},
                            disabled=True,
                        ),
                        label=fac.AntdText('账单类型',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),

                    fac.AntdFormItem(
                        fac.AntdTreeSelect(
                            id='billManage-treeSelect-payChannel',
                            treeData=options.get('pay_channel').get('options'),
                            treeNodeKeyToTitle=options.get('pay_channel').get('options_extra'),
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('支付渠道',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),

                    fac.AntdFormItem(
                        fac.AntdRadioGroup(
                            id='billManage-radioGroup-billObject',
                            options=options.get('bill_object').get('options'),
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('消费对象',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),


                ],
                    span=11,
                ),


                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInputNumber(
                            id='billManage-inputNumber-billAmount',
                            addonAfter='¥',
                            min=0,
                            precision=2,
                            # controls=True,
                            step=0.01,
                            style={'width': '100%'},
                        ),
                        label=fac.AntdText('账单金额',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),


                    fac.AntdFormItem(
                        fac.AntdTreeSelect(
                            id='billManage-treeSelect-billName',
                            treeData=options.get('bill_name').get('options'),
                            treeNodeKeyToTitle=options.get('bill_name').get('options_extra'),
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('账单名称',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),

                    fac.AntdFormItem(
                        fac.AntdTreeSelect(
                            id='billManage-treeSelect-settleChannel',
                            treeData=options.get('settle_channel').get('options'),
                            treeNodeKeyToTitle=options.get('settle_channel').get('options_extra'),
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('结算渠道',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),

                    fac.AntdFormItem(
                        fac.AntdRadioGroup(
                            id='billManage-radioGroup-billScene',
                            options=options.get('bill_scene').get('options'),
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('消费场景',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),


                ],
                    span=11,
                    offset=2,
                ),


                # fac.AntdCol([
                #     fac.AntdFormItem(
                #         fac.AntdFormItem(
                #             fac.AntdRadioGroup(
                #                 id='billManage-radioGroup-billObject',
                #                 options=options.get('bill_object').get('options'),
                #                 style={'width': '100%'}
                #             ),
                #             label=fac.AntdText('消费对象',
                #                                style={'fontFamily': 'DingTalkTi',
                #                                       'fontSize': '16px'}),
                #         ),
                #     ),
                # ],
                #     span=16,
                # ),



                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='billManage-input-billRemark',
                            mode='text-area',
                            autoSize={'minRows': 5, 'maxRows': 5},
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('备注',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),
                ],
                    span=24
                ),

                fac.AntdCol([
                    fac.AntdSpace([
                        fac.AntdPopconfirm(
                            fac.AntdButton('删除记录',
                                           type='default', danger=True,
                                           icon=fac.AntdIcon(icon='antd-delete'),
                                           style={'fontFamily': 'DingTalkTi'}
                                           ),
                            title='确认删除？',
                            id='billManage-button-deleteBill',
                        ),
                        fac.AntdButton('修改记录',
                                       id='billManage-button-reviseBill',
                                       type='primary',
                                       icon=fac.AntdIcon(icon='antd-edit'),
                                       style={'fontFamily': 'DingTalkTi'},
                                       ),
                    ],
                        size=36),
                ],
                    style={'textAlign': 'center'},
                    span=24,
                ),



            ]),



        ],



            # layout='vertical',
            id='billManage-form-billInfos',
            enableBatchControl=True,
            style={'width': '100%','marginTop': '20px'},
        )
    ])




from server import app
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash import set_props, ctx
from datetime import datetime
from api.apis import get_bills_api, get_bill_by_id_api, edit_bill_api, del_bill_api




## 切换账单状态的图标
app.clientside_callback(
    ClientsideFunction(namespace="BillManage", function_name="switchBillStatusIcon"),
    Input('billManage-switch-billStatus', 'checked'),
    State('bill-dict-options-config', 'data'),
    prevent_initial_call = True
)


## 切换账单状态的Switch组件
app.clientside_callback(
    ClientsideFunction(namespace="BillManage", function_name="switchBillStatusCheck"),
    Output('billManage-switch-billStatus', 'checked', allow_duplicate=True),
    Input('billManage-button-billStatus', 'nClicks'),
    State('billManage-switch-billStatus', 'checked'),
    prevent_initial_call = True
)

## 重置账单查询条件
app.clientside_callback(
    ClientsideFunction(namespace="BillManage", function_name="resetQueryBillConditions"),
    Output('billManage-form-queryConditions', 'values', allow_duplicate=True),
    Input('billManage-button-reset', 'nClicks'),
    prevent_initial_call = True
)

## 账单修改的MODAL中根据账单名称自适应更改账单类型
# app.clientside_callback(
#     ClientsideFunction(namespace="BillManage", function_name="syncBillTypeAccordBillNameInReviseBillModal"),
#     Output('billManage-select-billType', 'value', allow_duplicate=True),
#     Input('billManage-treeSelect-billName', 'value'),
#     prevent_initial_call = True
# )


# @app.callback(
#     Output('billManage-form-billInfos', 'values'),
#     Input('billManage-form-billInfos', 'values'),
#     prevent_initial_call=True
# )
# def abc(values):
#     print(ctx.triggered_id)
#     return values


@app.callback(
    [Output('billManage-table-billDetailData', 'data'),
     Output('global-message-container', 'children', allow_duplicate=True)],
    [Input('billManage-button-search', 'nClicks'),
     Input('billManage-store-billDataChangeCountStore', 'data')],
    [State('billManage-form-queryConditions', 'values'),
     State('bill-dict-options-config', 'data')],
    prevent_initial_call=True
)
def query_bill_data_and_show_in_table(nClicks, changeCounts, conditions, bill_dict):
    if any([nClicks, changeCounts]):
        query_info = {'user_id':session['user_id'], 'theme_id':session['theme_id'], 'n_limit':20}

        if conditions:
            if conditions.get('billManage-dateRangePicker-billDate'):
                query_info.update({'bill_date_start':conditions.get('billManage-dateRangePicker-billDate')[0],
                                   'bill_date_end':conditions.get('billManage-dateRangePicker-billDate')[1]})

            if conditions.get('billManage-select-billType'):
                query_info.update({'bill_type': conditions.get('billManage-select-billType')})

            if conditions.get('billManage-select-billStatus'):
                query_info.update({'bill_status': conditions.get('billManage-select-billStatus')})

            if conditions.get('billManage-treeSelect-payChannel'):
                query_info.update({'pay_channel': conditions.get('billManage-treeSelect-payChannel')})

            if conditions.get('billManage-treeSelect-settleChannel'):
                query_info.update({'settle_channel': conditions.get('billManage-treeSelect-settleChannel')})


        get_bills_res = get_bills_api(page_obj=query_info)

        if get_bills_res['code'] != 200:
             return [ [], fuc.FefferyFancyMessage("按条件查询账单信息" + get_bills_res["message"], type='error') ]           

        data = get_bills_res['data']
        data = [{'xh':i + 1,
                'bill_name':bill_dict.get('bill_name').get('options_extra').get(dt.get("bill_name_code")) if bill_dict else dt.get("bill_name"),
                'bill_date':dt.get("bill_date"),
                'bill_amount':dt.get("bill_amount"),
                'bill_status':{'status':'success' if dt.get("bill_status") == '正常' else 'warning', 'text':dt.get("bill_status")},
                'record_time':f'{datetime.fromtimestamp(dt.get("into_unix_time")):%Y-%m-%d %H:%M:%S}',
                'operation':{'content': f'查看详情', 'type': 'primary', 'custom': dt.get("bill_id"), 'icon':'antd-search', 'style':{'fontFamily': 'DingTalkTi'}}
                }
                for i, dt in enumerate(data)
                ]

        return [data, None]

    return [dash.no_update, None]


@app.callback(
    [Output('billManage-modal-reviseBillData', 'visible'),
     Output('billManage-form-billInfos', 'values', allow_duplicate=True),
     Output('billManage-switch-billStatus', 'checked', allow_duplicate=True),
     Output('global-message-container', 'children', allow_duplicate=True)],
    Input('billManage-table-billDetailData', 'nClicksButton'),
    State('billManage-table-billDetailData', 'clickedCustom'),
    prevent_initial_call=True
)
def show_revise_modal(nClick, bill_id):
    bill_info = {
        'billManage-input-billID': None,
        'billManage-dataPicker-billDate': None,
        'billManage-inputNumber-billAmount': None,
        'billManage-select-billType': None,
        'billManage-treeSelect-billName': None,
        'billManage-treeSelect-payChannel': None,
        'billManage-treeSelect-settleChannel': None,
        'billManage-radioGroup-billScene': None,
        'billManage-radioGroup-billObject': None,
        'billManage-input-billRemark': None,
    }

    if nClick:
 
        get_bill_res = get_bill_by_id_api(bill_id=bill_id)
        if get_bill_res['code'] != 200:
            return [
                True,
                bill_info,
                True ,
                fuc.FefferyFancyMessage("获取账单信息" + get_bill_res['message'], type='error')
            ]
        

        bill = get_bill_res['data']

        bill_info = {
            'billManage-input-billID':bill_id,
            'billManage-dataPicker-billDate': pd.to_datetime(bill.get('bill_date')).strftime('%Y-%m-%d'),
            'billManage-inputNumber-billAmount': bill.get('bill_amount'),
            'billManage-select-billType': bill.get('bill_type'),
            'billManage-treeSelect-billName': bill.get('bill_name'),
            'billManage-treeSelect-payChannel': bill.get('pay_channel'),
            'billManage-treeSelect-settleChannel': bill.get('settle_channel'),
            'billManage-radioGroup-billScene': bill.get('bill_scene'),
            'billManage-radioGroup-billObject': bill.get('consume_object'),
            'billManage-input-billRemark': bill.get('remark'),
        }

        return [
            True,
            bill_info,
            True if bill.get('bill_status') == '00' else False,
            None
        ]
        


    return [False, dash.no_update, True, None]



@app.callback(
    [Output('billManage-modal-reviseBillData', 'visible', allow_duplicate=True),
     Output('billManage-store-billDataChangeCountStore', 'data', allow_duplicate=True),
     Output('global-message-container', 'children', allow_duplicate=True)],
    Input('billManage-button-reviseBill', 'nClicks'),
    [State('billManage-form-billInfos', 'values'),
     State('billManage-switch-billStatus', 'checked'),
     State('billManage-store-billDataChangeCountStore', 'data'),
     ],
    prevent_initial_call=True
)
def edit_bill(nClicks, bill_info, bill_status, dataChange):
    if nClicks:

        get_bill_res = get_bill_by_id_api(bill_id=bill_info.get('billManage-input-billID'))

        if get_bill_res['code'] != 200:
            return [
                True,
                {"changeCounts": dataChange.get("changeCounts") + 1},
                fuc.FefferyFancyMessage("获取账单信息" +  get_bill_res['message'], type='error')
            ]

        bill = get_bill_res['data']
        bill.update({
            'bill_id': bill_info.get('billManage-input-billID'),
            'bill_type': bill_info.get('billManage-treeSelect-billName')[0],
            'bill_name': bill_info.get('billManage-treeSelect-billName'),
            'pay_channel': bill_info.get('billManage-treeSelect-payChannel'),
            'settle_channel': bill_info.get('billManage-treeSelect-settleChannel'),
            'consume_object': bill_info.get('billManage-radioGroup-billObject'),
            'bill_scene': bill_info.get('billManage-radioGroup-billScene'),
            'bill_status': '00' if bill_status else '01',
            'bill_amount': bill_info.get('billManage-inputNumber-billAmount'),
            'bill_date': bill_info.get('billManage-dataPicker-billDate'),
            'remark': bill_info.get('billManage-input-billRemark'),
        })


        edit_bill_res = edit_bill_api(page_obj=bill)
        if edit_bill_res['code'] != 200:
            return [
                True,
                {"changeCounts": dataChange.get("changeCounts") + 1},
                fuc.FefferyFancyMessage("编辑账单" + edit_bill_res['message'], type='error')
            ]

        return [
            False,
            {"changeCounts": dataChange.get("changeCounts") + 1},
            fuc.FefferyFancyMessage('账单修改成功',  type='success')
        ]


    return [False, dash.no_update, None]


@app.callback(
    [Output('billManage-modal-reviseBillData', 'visible', allow_duplicate=True),
     Output('billManage-store-billDataChangeCountStore', 'data', allow_duplicate=True),
     Output('global-message-container', 'children', allow_duplicate=True)],
    Input('billManage-button-deleteBill', 'confirmCounts'),
    [State('billManage-form-billInfos', 'values'),
     State('billManage-store-billDataChangeCountStore', 'data'),],
    prevent_initial_call=True
)
def delete_bill(nClicks, bill_info, dataChange):
    if nClicks:

        del_bill_res = del_bill_api(bill_id=bill_info.get('billManage-input-billID'))

        if del_bill_res['code'] != 200:
            return [
                True,
                {"changeCounts": dataChange.get("changeCounts") + 1},
                fuc.FefferyFancyMessage("删除账单" + del_bill_res['message'], type='error')
            ]

        return [
            False,
            {"changeCounts": dataChange.get("changeCounts") + 1},
            fuc.FefferyFancyMessage('账单删除成功', type='success')
        ]
    
    return [False, dash.no_update, None]