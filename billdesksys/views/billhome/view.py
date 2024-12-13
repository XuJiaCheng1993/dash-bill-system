#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:10    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:10 


from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_antd_charts as fact
import uuid
import datetime

def render_content(bill_calendar_data=[]):
    doc_content = fuc.FefferyDiv([
        
        fac.Fragment(id='billAnalysis-message-container'),

        fac.Fragment([
            dcc.Store(id='billAnalyze-store-lastBillCalendar', data=None),
            dcc.Store(id='billAnalyze-store-isNeedUpdateBillCalendar', data=False, storage_type='session')
        ]),

        ## 分析条件
        fac.AntdCenter(
            fac.AntdSpace([
                fac.AntdForm([
                        fac.AntdFormItem(
                            fac.AntdDateRangePicker(
                                id='billAnalyze-dateRangePicker-billDate',
                                # placeholder='请选择查询的账单日期范围',
                                allowClear=True,
                                style={'width': '20vw'}
                            ),
                            label=fac.AntdText('日期范围', style={'fontFamily': 'DingTalkTi'}),
                            style={'paddingBottom': '10px'},
                        ),


                        fac.AntdFormItem(
                            fac.AntdButton(
                                '开始分析',
                                id='billAnalyze-button-startAnalyze',
                                type='primary',
                                icon=fac.AntdIcon(icon='bi-analyse'),
                                style={'fontFamily': 'DingTalkTi'}
                            ),
                            style={'paddingBottom': '10px'},
                        ),

                        fac.AntdFormItem(
                            fac.AntdButton(
                                '查看账单日历',
                                id='billAnalyze-button-viewBillCalendar',
                                type='primary',
                                icon=fac.AntdIcon(icon='antd-search'),
                                style={'fontFamily': 'DingTalkTi'}
                            ),
                            style={'paddingBottom': '10px'},
                        ),


                ],
                    id='billAnalyze-form-analyzeConditions',
                    layout='inline',
                    enableBatchControl=True,
                ),            
            ],
                wrap=True,
                style={'padding': '2vh 0'},
            ),
        ),
        
        
        ## 分析结果容器
        fac.AntdCenter(
            fac.AntdSpin(
                fuc.FefferyDiv(
                    id=f'billAnalyze-div-analyzeResultContainer',
                    style={'width': '70vw'}
                ),
            ),
        ),


        ## 注入弹出账单日历的modal
        fac.AntdModal(
            children=fac.AntdSpin(
                fac.AntdCalendar(
                    size='large',
                    customCells=bill_calendar_data,
                    value=f"{datetime.datetime.today():%Y-%m-%d}",
                    id='billAnalyze-calendar-billCalendar'
                    ),
                text='数据加载中...'
                ),
            title=html.Span([fac.AntdIcon(icon='antd-calendar', style={'marginRight': '4px'}), '账单日历']),
            width=1200,
            id='billAnalyze-modal-billCalendar',
            visible=False,
            # loading=True,
        ),
        


        ## 注入弹出修改表格参数的modal
        fac.AntdDrawer(
            children=render_setting_analyze_table_params(), 
            id='billAnalyze-drawer-analyzeTableParams',
            title=html.Span([fac.AntdIcon(icon='antd-setting', style={'marginRight': '4px'}), '分析表格参数设置']),
            placement='bottom',
            width='20vh',
            closable=False,
            visible=False,
            extra=fac.AntdButton('设置参数', type='primary', id='billAnalyze-button-confirmAnalyzeTableParams'),     
        ),

     


    ],
    
        style={'padding': '0 2vw'}
    )

    return doc_content


# def render_bill_calendar(today):
#     """ 渲染账单日历"""
#     return fac.AntdCalendar(
#         size='large',
#         customCells=[],
#         value=today,
#         id='billAnalyze-calendar-billCalendar'
#     )  


def render_setting_analyze_table_params():
    return fac.AntdCenter(
        fuc.FefferyDiv([
            fac.AntdCheckCardGroup(
                children=[
                    fac.AntdCheckCard('※1 账单日期', value='bill_date', id={'type':'billAnalyze-checkCard', 'index':'billDate'}, style={'width':'200px'}),
                    fac.AntdCheckCard('※2 账单类型', value='bill_type', id={'type':'billAnalyze-checkCard', 'index':'billType'}, style={'width':'200px'}),
                    fac.AntdCheckCard('消费对象', value='consume_object', id={'type':'billAnalyze-checkCard', 'index':'consumeObject'}, style={'width':'200px'}),
                    fac.AntdCheckCard('支付渠道', value='pay_channel', id={'type':'billAnalyze-checkCard', 'index':'payChannel'}, style={'width':'200px'}),
                    fac.AntdCheckCard('结算渠道', value='settle_channel', id={'type':'billAnalyze-checkCard', 'index':'settleChannel'}, style={'width':'200px'}),
                    fac.AntdCheckCard('支出场景', value='bill_scene', id={'type':'billAnalyze-checkCard', 'index':'billScene'}, style={'width':'200px'}),
                    ],
            id='billAnalyze-checkCardGroup-analyzeDimChoice',
            # size="small",
            multiple=True,
            defaultValue=['bill_date', 'bill_type'],
            ),
        ],
            style={'width': '70vw'},
        )
    )



def render_chart(chart_data, chart_name, chart_index, chart_type='rose', key='', fig_height=300):
    ''' 生成图表 '''
    chart_content = []
    if chart_type == 'rose':
        chart_content = fuc.FefferyDiv([
            fac.AntdText(f'图表分析-{chart_name}',
                style={'fontSize': '16px', 'fontFamily': 'DingTalkTi', 'marginBottom': '12px'}),
            fuc.FefferyDiv(
                fact.AntdRose(
                    data=chart_data,
                    xField='type',
                    yField='value',
                    innerRadius=0.4,
                    seriesField='type',
                    key=key,
                    id={'type':'billAnalyze-chart', 'index':f'{chart_type}-{chart_index}'}
                ),
                style={
                    'margin': f'0px 36px 0px 0px',
                    'borderRadius': '6px',
                    'padding': '8px 8px 8px 8px',
                    'width': '95%',
                    'height': f'{fig_height}px'
                }
            )
        ],
            style={'width':'100%'}
        )

    elif chart_type == 'area':
        chart_content = fuc.FefferyDiv([
            fac.AntdText(f'图表分析-{chart_name}',
                style={'fontSize': '16px', 'fontFamily': 'DingTalkTi', 'marginBottom': '12px'}),
            fuc.FefferyDiv(
                fact.AntdArea(
                    id={'type':'billAnalyze-chart', 'index':f'{chart_type}-{chart_index}'},
                    xField='dt', yField='val', seriesField='ser',
                    smooth=True,
                    key=key,
                    areaStyle={'fill': 'l(270) 0:#ffffff 0.3:#1792ff 1:#1177bb'},
                    data=chart_data
                ),
                style={
                    'margin': '0px 36px 36px 0px',
                    'borderRadius': '6px',
                    'padding': '8px 8px 8px 8px',
                    'width': '95%',
                    'height': f'{fig_height}px'
                }
            )
        ],
            style={'width':'100%'}
        )

    elif chart_type == 'sunburst':
         chart_content = fuc.FefferyDiv([
            fac.AntdText(f'图表分析-{chart_name}',
                style={'fontSize': '16px', 'fontFamily': 'DingTalkTi', 'marginBottom': '12px'}),
            fuc.FefferyDiv(
                fact.AntdSunburst(
                    id={'type':'billAnalyze-chart', 'index':f'{chart_type}-{chart_index}'},
                    key=key,
                    label=True,
                    innerRadius = 0.4,
                    data=chart_data
                ),
                style={
                    'margin': '0px 36px 36px 0px',
                    'borderRadius': '6px',
                    'padding': '8px 8px 8px 8px',
                    'width': '95%',
                    'height': f'{fig_height}px'
                }
            )
        ],
            style={'width':'100%'}
        )       
    

    return chart_content


def render_analyze_result(table_data=None, trend_data=None, type_data=None, pay_data=None, settle_data=None, object_data=None, scene_data=None):
    """ 渲染分析结果 """    
    # area_data = [{'dt':'2024-11-01', 'val':100}, {'dt':'2024-11-02', 'val':200}, {'dt':'2024-11-03', 'val':300}]
    # rose_data = [{'type':'A1', 'value':15}, {'type':'A2', 'value':25}, {'type':'A3', 'value':35}]
    # sunburst_data = {'name':'root', 'children':[
    #     {'name': 'A', 'value': 10, 'children': [
    #         {'name': 'A1', 'value': 10}, 
    #         {'name': 'A2', 'value': 20}, 
    #         {'name': 'A3', 'value': 30}]
    #     },
    #     {'name': 'B', 'value': 10, 'children': [
    #         {'name': 'B1', 'value': 10}, 
    #         {'name': 'B2', 'value': 20}]
    #     },       
    # ]}
    # table_data =  [
    #     {'main': {'content': "A", 'rowSpan': 3}, 'sub': "A1", 'val': 45}, 
    #     {'main': {'content': "A", 'rowSpan': 0}, 'sub': "A2", 'val': 40}, 
    #     {'main': {'content': "A", 'rowSpan': 0}, 'sub': "A3", 'val': 35}, 
    #     {'main': {'content': "B", 'rowSpan': 2}, 'sub': "B2", 'val': 40}, 
    #     {'main': {'content': "B", 'rowSpan': 0}, 'sub': "B3", 'val': 35},         
    #     ]

    doc = [
        fac.AntdSpace([
            fac.AntdText('表格分析-分类汇总',
                        style={'fontSize': '16px', 'fontFamily': 'DingTalkTi', 'marginBottom': '12px'}),  
            fac.AntdButton(
                fac.AntdIcon(icon='md-settings', style={'font-size': '20px', 'color': '#16b998'}), 
                type='text',
                shape='circle',
                id = 'billAnalyze-button-setAnalyzeTableParams'
            ),          
        ]),
        
        fac.AntdTable(id='billAnalyze-table-summary',
                        columns=[{'dataIndex': 'main', 'title': '主维', 'renderOptions': {'renderType': 'row-merge'}},
                                {'dataIndex': 'sub', 'title': '次维'},
                                {'dataIndex': 'val', 'title': '合计(元)', },
                                ],
                        bordered=True,
                        pagination={'pageSize':200, 'disabled':True},
                        style={'width': '95%'},
                        data=table_data,
                        ),

  
        fac.AntdRow([
            fac.AntdCol([
                render_chart(chart_data=type_data, chart_name='账单类型', chart_index='zdlx', chart_type='sunburst',key=str(uuid.uuid4().hex),
                             fig_height=500),
            ],
                span=8,
            ),

             fac.AntdCol([
                render_chart(chart_data=trend_data, chart_name='消费趋势', chart_index='xfrq', chart_type='area', key=str(uuid.uuid4().hex),
                             fig_height=500), 
            ],
                span=16, 
            ),           

            
            fac.AntdCol([
                render_chart(chart_data=pay_data, chart_name='支付渠道', chart_index='zdlx2', chart_type='rose',key=str(uuid.uuid4().hex)),
                render_chart(chart_data=object_data, chart_name='消费对象', chart_index='zdlx1', chart_type='rose',key=str(uuid.uuid4().hex)),                   
            ], 
                span=11
            ),

            fac.AntdCol([
                render_chart(chart_data=settle_data, chart_name='结算渠道', chart_index='zdlx3', chart_type='rose',key=str(uuid.uuid4().hex)),       
                render_chart(chart_data=scene_data, chart_name='支出场景', chart_index='zdlx4', chart_type='rose',key=str(uuid.uuid4().hex)), 
            ], 
                offset=1,
                span=11
            ),
            
            
        ]),
           
    ]
    return doc





import dash
from server import app
from dash.dependencies import Input, Output, State, ClientsideFunction, ALL
from dash import set_props, ctx
import datetime
import pandas as pd
from flask import session
import random
from api.apis import get_bill_analysis

TAGCOLORS = [
    'magenta',
    'red',
    'volcano',
    'orange',
    'gold',
    'lime',
    'green',
    'cyan',
    'blue',
    'geekblue',
    'purple',
]

def transfrom_apidata_chartdata(data, mode, dim1, dim2=None):
    """ 将数据转换为前端表格和图表需要的数据 """
    if len(data) <= 0:
        return {} if mode == "SunburstChart" else []
    if mode == 'RowMergeTable':
        data = pd.DataFrame(data)
        table_data = []
        for md in data[dim1].unique():
            n = len(data[data[dim1] == md])
            for i, rcd in enumerate(data[data[dim1] == md].to_dict('records')):
                if i <= 0:
                    tmp = [{'main': {'content': md, 'rowSpan': n}, 'sub': rcd.get(dim2), 'val': rcd.get('amt')}, ]
                else:
                    tmp = [{'main': {'rowSpan': 0}, 'sub': rcd.get(dim2), 'val': rcd.get('amt')}, ]

                table_data += tmp
        return table_data
    
    elif mode == "AreaChart":
        return [{"dt":per.get(dim1), "val":per.get("amt")} for per in data]
    
    elif mode == "SunburstChart":
        data = pd.DataFrame(data)
        children = []
        for bt in data[dim1].unique():
            btmp = data[data[dim1] == bt]
            tmp = {
                'name':bt,
                "value":btmp['amt'].sum(),
                "children": btmp[[dim2, "amt"]].rename(columns={dim2:"name", "amt":"value"}).to_dict("records")
            }
            children.append(tmp )
        return {"name":"summary", "children":children}
    
    elif mode == "RoseChart":
        return [{"type":per.get(dim1), "value":per.get("amt")} for per in data]
    
    else:
        return []
        



## 渲染账单分析维度选择卡
app.clientside_callback(
    ClientsideFunction(namespace="BillAnalyze", function_name="checkAndUpdateAnalyzeDimCard"),
    [Output({'type':'billAnalyze-checkCard', 'index':ALL}, 'disabled'),
    Output({'type':'billAnalyze-checkCard', 'index':ALL}, 'children'),],
    Input('billAnalyze-checkCardGroup-analyzeDimChoice', 'value'),
    State({'type':'billAnalyze-checkCard', 'index':ALL}, 'value'),
    prevent_initial_call = True      
)

@app.callback(
    [Output('billAnalyze-drawer-analyzeTableParams', 'visible', allow_duplicate=True),
    Output('billAnalyze-table-summary', 'data')],
    Input('billAnalyze-button-confirmAnalyzeTableParams', 'nClicks'),
    State('billAnalyze-checkCardGroup-analyzeDimChoice', 'value'),
    State('billAnalyze-dateRangePicker-billDate', 'value'),
    prevent_initial_call = True      
)
def set_table_analyze_dim(nClicks, choice, dateRange):

    if nClicks:
        if len(choice) >= 2:
            [bg_date, ed_date] = dateRange if dateRange else [(datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%Y-%m-%d")]
            
            
            get_table_data_res =  get_bill_analysis(
                query_obj={
                    "user_id": session['user_id'],
                    "theme_id": session['theme_id'],
                    # "bill_status": "00",
                    "bill_date_start":  bg_date ,
                    "bill_date_end": ed_date,
                }, 
                analysis_obj={
                    'analyze_by': choice,
                    'is_contain_date_field': True if "bill_date" in choice else False,
                    'date_field': 'bill_date',
                    'date_dim': 'M',
                    'is_return_code': False,
                    'is_summary': True,
                }
            )

            table_data = transfrom_apidata_chartdata(
                data=get_table_data_res['data'],
                mode='RowMergeTable',
                dim1=choice[0],
                dim2=choice[1]
            )
            
            return False, table_data
    return dash.no_update, dash.no_update
    


## 展示账单日历的Modal
app.clientside_callback(
    '''( nClicks ) => {
    if ( nClicks ) {
        window.dash_clientside.set_props(
            "billAnalyze-store-isNeedUpdateBillCalendar",
            {
                "data": true
            }
        );
        return true;
    }
    else {
        return false;
    }
    }''',
    Output('billAnalyze-modal-billCalendar', 'visible'),
    Input('billAnalyze-button-viewBillCalendar', 'nClicks'),
    prevent_initial_call = True
)

## 展示分析表格分析参数的drawer
app.clientside_callback(
    '''( nClicks ) => {
    if ( nClicks ) {
        return true;
    }
    else {
        return false;
    }
    }''',
    Output('billAnalyze-drawer-analyzeTableParams', 'visible'),
    Input('billAnalyze-button-setAnalyzeTableParams', 'nClicks'),
    prevent_initial_call = True
)


@app.callback(
    Output('billAnalyze-div-analyzeResultContainer', 'children'),
    Input('billAnalyze-button-startAnalyze', 'nClicks'),
    State('billAnalyze-dateRangePicker-billDate', 'value'),
    prevent_initial_call=True
)
def show_analyze_result(nClicks, dateRange):
    if nClicks:

        [bg_date, ed_date] = dateRange if dateRange else [(datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%Y-%m-%d")]


        
        ## 表格分析
        get_table_data_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                # "bill_status": "00",
                "bill_date_start":  bg_date ,
                "bill_date_end": ed_date,
            }, 
            analysis_obj={
                'analyze_by': ['bill_date', 'bill_type'],
                'is_contain_date_field': True,
                'date_field': 'bill_date',
                'date_dim': 'M',
                'is_return_code': False,
                'is_summary': True,
            }
        )

        table_data = transfrom_apidata_chartdata(
            data=get_table_data_res['data'],
            mode='RowMergeTable',
            dim1='bill_date',
            dim2='bill_type'
        )
        
        ## 时间趋势分析
        get_trend_data_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                # "bill_status": "00",
                "bill_date_start":  bg_date ,
                "bill_date_end": ed_date,
            }, 
            analysis_obj={
                'analyze_by': 'bill_date',
                'is_contain_date_field': True,
                'date_field': 'bill_date',
                'date_dim': 'D',
                'is_return_code': False,
                'is_summary': False,
            }
        )
        
        bill_trend_data = transfrom_apidata_chartdata(
            data=get_trend_data_res['data'],
            mode='AreaChart',
            dim1='bill_date'
        )

        
        ## 账单类别sunburst分析
        get_bill_type_data_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                # "bill_status": "00",
                "bill_date_start":  bg_date ,
                "bill_date_end": ed_date,
            }, 
            analysis_obj={
                'analyze_by': ['bill_type', "bill_name"],
                'is_contain_date_field': False,
                'date_field': 'bill_date',
                'is_return_code': False,
                'is_summary': False,
            }
        )
        
        data_sunburst_bill_type = transfrom_apidata_chartdata(
            data=get_bill_type_data_res['data'],
            mode='SunburstChart',
            dim1='bill_type',
            dim2='bill_name'
        )
        
        ## 支付渠道rose分析
        get_pay_channel_data_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                # "bill_status": "00",
                "bill_date_start":  bg_date ,
                "bill_date_end": ed_date,
            }, 
            analysis_obj={
                'analyze_by': "pay_channel",
                'is_contain_date_field': False,
                'date_field': 'bill_date',
                'is_return_code': False,
                'is_summary': False,
            }
        )
        data_rose_pay_channel = transfrom_apidata_chartdata(
            data=get_pay_channel_data_res['data'],
            mode='RoseChart',
            dim1='pay_channel'
        )

        ## 结算渠道rose分析
        get_settle_channel_data_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                # "bill_status": "00",
                "bill_date_start":  bg_date ,
                "bill_date_end": ed_date,
            },
            analysis_obj={
                'analyze_by': "settle_channel",
                'is_contain_date_field': False,
                'date_field': 'bill_date',
                'is_return_code': False,
                'is_summary': False,
            }
        )
        data_rose_settle_channel = transfrom_apidata_chartdata(
            data=get_settle_channel_data_res['data'],
            mode='RoseChart',
            dim1='settle_channel'
        )

        ## 消费对象rose分析
        get_consume_object_data_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                # "bill_status": "00",
                "bill_date_start":  bg_date ,
                "bill_date_end": ed_date,
            },
            analysis_obj={
                'analyze_by': "consume_object",
                'is_contain_date_field': False,
                'date_field': 'consume_object',
                'is_return_code': False,
                'is_summary': False,
            }
        )
        data_rose_consume_object = transfrom_apidata_chartdata(
            data=get_consume_object_data_res['data'],
            mode='RoseChart',
            dim1='consume_object'           
        )

        ## 账单场景rose分析
        get_bill_scene_data_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                # "bill_status": "00",
                "bill_date_start":  bg_date ,
                "bill_date_end": ed_date,
            },
            analysis_obj={
                'analyze_by': "bill_scene",
                'is_contain_date_field': False,
                'date_field': 'bill_scene',
                'is_return_code': False,
                'is_summary': False,
            }
        )
        data_rose_bill_scene = transfrom_apidata_chartdata(
            data=get_bill_scene_data_res['data'],
            mode='RoseChart',
            dim1='bill_scene'           
        )

        
        return render_analyze_result(
            table_data=table_data,
            trend_data=bill_trend_data, 
            type_data=data_sunburst_bill_type, 
            pay_data=data_rose_pay_channel, 
            settle_data=data_rose_settle_channel, 
            object_data=data_rose_consume_object, 
            scene_data=data_rose_bill_scene
        )
    
    return dash.no_update


## 账单日历是否需要更新
app.clientside_callback(
    ClientsideFunction(namespace="BillAnalyze", function_name="checkIsNeedUpdateBillCalendar"),
    [Output('billAnalyze-store-lastBillCalendar', 'data', allow_duplicate=True), 
     Output('billAnalyze-store-isNeedUpdateBillCalendar', 'data', allow_duplicate=True)],
    [Input('billAnalyze-calendar-billCalendar', 'value'),
     Input('billAnalyze-calendar-billCalendar', 'cellClickEvent'),],
    [State('billAnalyze-store-lastBillCalendar', 'data')],
    prevent_initial_call=True,      
)



@app.callback(
    [Output('billAnalyze-calendar-billCalendar', 'customCells'),
     Output('billAnalysis-message-container', 'children'),], 
    Input('billAnalyze-store-isNeedUpdateBillCalendar', 'data'),
    State('billAnalyze-calendar-billCalendar', 'value'),
    State('billAnalyze-calendar-billCalendar', 'cellClickEvent'),
    prevent_initial_call=True    
)
def update_calendar_bills(is_need_update, choice_date, event):
    # if not all([is_need_update, choice_date, event]):
    #     return [dash.no_update, None]
    # print(choice_date)
    if is_need_update:
        choice_date = f"{datetime.datetime.now():%Y-%m-%d}" if choice_date is None else choice_date
 

        get_analysis_day_res =  get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                "bill_status": "00",
                "bill_date_start":  f"{pd.to_datetime(choice_date[:8] + '01') - datetime.timedelta(days=6):%Y-%m-%d}" ,
                "bill_date_end": f"{pd.date_range(choice_date, periods=1, freq='ME')[-1] + datetime.timedelta(days=7):%Y-%m-%d}",
            }, 
            analysis_obj={
                'analyze_by': ['bill_date', 'bill_type'],
                'is_contain_date_field': True,
                'date_field': 'bill_date',
                'date_dim': 'D',
                'is_return_code': False,
                'is_summary': False,
            }
        )

        get_analysis_month_res = get_bill_analysis(
            query_obj={
                "user_id": session['user_id'],
                "theme_id": session['theme_id'],
                "bill_status": "00",               
                "bill_date_start":  choice_date[:4] + '-01-01' ,
                "bill_date_end": choice_date[:4] + '-12-31' ,               
            }, 
            analysis_obj={
                'analyze_by': 'bill_date',
                'is_contain_date_field': True,
                'date_field': 'bill_date',
                'date_dim': 'M',
                'is_return_code': False,
                'is_summary': False,
            }
        )
        
        ## 获取错误信息
        error_message = None
        if get_analysis_day_res["code"] != 200 or get_analysis_month_res["code"] != 200:
            error_message = "账单分析接口异常："
            if get_analysis_day_res["code"] != 200:
                error_message += get_analysis_day_res["message"] + '。'
            if get_analysis_month_res["code"] != 200:
                error_message += get_analysis_month_res["message"] + '。'
        
        

        ## 将分析结果转换
        data_day = pd.DataFrame(get_analysis_day_res['data'])
        data_month = get_analysis_month_res['data']
    
        calendar_data = []
        if len(data_day) >= 1:
            for dt in data_day['bill_date'].unique():
                tmpdata = data_day[data_day["bill_date"] == dt]
                dt_stamps = pd.to_datetime(dt)
                tmp = {
                    'type': 'date',
                    'year':dt_stamps.year,
                    'month': dt_stamps.month,
                    'date': dt_stamps.day,
                    'content': [
                        fac.AntdTag(content=f'{nm} ￥{val:.2f}', color=random.choice(TAGCOLORS))
                        for i, (nm, val) in enumerate(zip(tmpdata['bill_type'], tmpdata['amt']))
                        ],
                }
                calendar_data.append(tmp)
        
        if len(data_month) >= 1:
            for per in data_month:
                dt_stamps = pd.to_datetime(per.get("bill_date") + '-01')
                tmp ={
                    'type': 'month',
                    'year':dt_stamps.year,
                    'month': dt_stamps.month,
                    'content': [fac.AntdTag(content=f'合计 {per.get("cnt")}笔 ￥{per.get("amt"):.2f}', color='black')],
                }
                calendar_data.append(tmp)
        
        return [calendar_data, fuc.FefferyFancyMessage(error_message, type='error')  if error_message else None]

    return [dash.no_update, None]


