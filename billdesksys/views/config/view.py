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
from flask import session

from views.view_utils import ICON_LIST


def render_content(code_items_data=[], theme_market_data=None):

    doc_content = fuc.FefferyDiv([
        
        fac.Fragment(id='config-message-container1'),
        fac.Fragment(id='config-message-container2'),       
        # 注入页面消息提示容器
        html.Div(id='config-page-message-container'),
        # 注入页面通知信息容器
        html.Div(id='config-page-notification-container'),


        
        # 注入缓存
        fac.Fragment([
            dcc.Store(id='config-store-billThemeChangeFlag', storage_type='session', data=False),
            dcc.Store(id='config-store-billDictCodeItemChangeFlag', storage_type='session', data=False),
        ]),
        
        
        fuc.FefferyDiv([
            ## 配置按钮
            fuc.FefferyDiv([
                fac.AntdSpace([
                    fac.AntdButton(
                        [fac.AntdIcon(icon='antd-plus'),'新增主题',],
                        id={'type': 'config-button-showThemeEditAddModal', 'index': 'add'},
                        style={
                            'color': '#1890ff',
                            'background': '#e8f4ff',
                            'border-color': '#a3d3ff'
                        }
                    ),

                    fac.AntdButton(
                        [fac.AntdIcon(icon='antd-edit'), '编辑主题', ],
                        id={'type': 'config-button-showThemeEditAddModal', 'index': 'edit'},
                        style={
                            'color': '#1890ff',
                            'background': '#e8f4ff',
                            'border-color': '#a3d3ff'
                        }
                    ),

                    fuc.FefferyDiv([
                        fac.AntdPopover(
                            fac.AntdButton(
                                [fac.AntdIcon(icon='md-swap-horiz'), '切换主题', ],
                                id = "config-button-showThemeMarket",
                                style={
                                    'color': '#1890ff',
                                    'background': '#e8f4ff',
                                    'border-color': '#a3d3ff'
                                }
                            ),
                            content=render_switch_theme_tabitems(theme_market_data) ,
                            placement='bottom',
                            trigger='click',
                            # fresh = True,
                            id=f'confog-popover-themeMarket'
                        ),

                    ]),

                    # fac.AntdButton(
                    #     [fac.AntdIcon( icon='md-swap-vert'), '展开/折叠'],
                    #     id='menu-fold',
                    #     style={
                    #         'color': '#909399',
                    #         'background': '#f4f4f5',
                    #         'border-color': '#d3d4d6'
                    #     }
                    # ),



                ],
                    wrap=True,
                    size=28,
                ),
            ]),

            ## 配置内容显示
            fuc.FefferyDiv([
                fac.AntdSpin(
                    fac.AntdTable(
                        id='config-table-billDictData',
                        columns=[
                            {'dataIndex': 'dict_id_base',
                             'title': '字典编号',
                             'renderOptions': {'renderType': 'ellipsis'},
                             'hidden': True},

                            {'dataIndex': 'dict_cn_name',
                             'title': '字典名称',
                             'width': '20%',
                             'renderOptions': {'renderType': 'ellipsis'},},

                            {'dataIndex': 'code_key',
                             'title': '码键',
                             'width': '10%',
                             'renderOptions': {'renderType': 'ellipsis'}, },

                            {'dataIndex': 'code_value',
                             'title': '码值',
                             'width': '30%',
                             'renderOptions': {'renderType': 'ellipsis'}, },


                            {'dataIndex': 'code_sort',
                             'title': '排序',
                             'width': '10%',
                             'renderOptions': {'renderType': 'ellipsis'}, },

                            {'dataIndex': 'is_default',
                             'title': '是否默认',
                             'width': '10%',
                             'renderOptions': {'renderType': 'ellipsis'}, },

                            {'title': '操作',
                             'dataIndex': 'operation',
                             'width': '20%',
                             'renderOptions': {'renderType': 'button'},
                             'align':'left'}
                        ],
                        # expandedRowKeys=['A01'],

                        data=code_items_data,
                        bordered=True,
                        pagination={
                            'hideOnSinglePage': True
                        },
                        style={
                            'width': '100%',
                            'padding-right': '10px',
                            'padding-bottom': '20px'
                        }
                    ),
                    text='数据加载中'
                ),

            ],
                style={'marginTop':'16px','width': '90vw',}
            ),
        ],
            style={'margin': '16px 5vw 16px 5vw'}
        ),


        ## 注入新增主题的MODAL
        fac.AntdModal(children=render_modal_theme_add_or_edit(add_mode=True),
                      title=html.Span([fac.AntdIcon(icon='md-add-box', style={'marginRight': '4px'}), '新增主题']),
                      width=500,
                      id=f'config-modal-addTheme',
                      # visible=True,
                      # loading=True,
                      ),

        ## 注入修改主题的MODAL
        fac.AntdModal(children=render_modal_theme_add_or_edit(add_mode=False),
                      title=html.Span([fac.AntdIcon(icon='md-extension', style={'marginRight': '4px'}), '编辑主题']),
                      width=500,
                      id=f'config-modal-editTheme',
                      # visible=True,
                      # loading=True,
                      ),




        ## 注入新增/修改码值的MODAL
        # fac.AntdModal(id='config-modal-addOrEditCodeItem',
        #               width=700,
        #               ),

        
        fac.AntdModal(children=render_add_code_item_modal(),
                      title=html.Span([fac.AntdIcon(icon='md-add-box', style={'marginRight': '4px'}), '新增字典']),
                      width=700,
                      id='config-modal-addDict',
                      # visible=True,
                      # loading=True,
                      ),

        fac.AntdModal(children=render_edit_code_item_modal(),
                      title=html.Span([fac.AntdIcon(icon='md-extension', style={'marginRight': '4px'}), '编辑字典']),
                      width=700,
                      id='config-modal-editDict',
                      # visible=True,
                      # loading=True,
                      ),

    ],
        style={'width': '100%',},
    )
    return doc_content


def render_modal_theme_add_or_edit(add_mode=True):
    doc_content = fuc.FefferyDiv([
        fac.AntdForm([
            fac.AntdRow([
                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id={'index':'config-input-themeId', 'type': 'add' if add_mode else 'edit'},
                            disabled=True,
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('主题编号',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                        hidden= add_mode
                    ),
                ],
                    span=24
                ),

                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id={'index': 'config-input-themeName', 'type': 'add' if add_mode else 'edit'},
                            placeholder='请输入主题名称',
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('主题名称',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),

                    ),
                ],
                    span=18
                ),

                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdSwitch(
                            id='config-switch-themeStatus',
                            checkedChildren=fac.AntdText('正常', strong=True, style={'color': 'white'}),
                            unCheckedChildren=fac.AntdText('禁用', strong=True, style={'color': 'white'}),
                            checked=True,
                            style={'width': '80px'}
                        ),
                        hidden=True if add_mode else False,
                    ),
                ],
                    offset=2,
                    span=4
                ),

                fac.AntdCol([
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id={'index': 'config-input-themeDescribe', 'type': 'add' if add_mode else 'edit'},
                            placeholder='请输入主题描述',
                            mode='text-area',
                            style={'width': '100%'}
                        ),
                        label=fac.AntdText('主题描述',
                                           style={'fontFamily': 'DingTalkTi',
                                                  'fontSize': '16px'}),
                    ),
                ],
                    span=24
                ),

                *([
                      fac.AntdCol([
                          fac.AntdSpace([
                              fac.AntdPopconfirm(
                                  fac.AntdButton('删除主题',
                                                 type='default', danger=True,
                                                 icon=fac.AntdIcon(icon='antd-delete'),
                                                 style={'fontFamily': 'DingTalkTi'}
                                                 ),
                                  title='确认删除？',
                                  id='config-button-deleteBillTheme',
                              ),
                              fac.AntdButton('修改主题',
                                             id='config-button-editBillTheme',
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

                  ] if not add_mode else []),

                *([
                      fac.AntdCol([
                          fac.AntdButton('提交新主题',
                                         id='config-button-addBillTheme',
                                         type='primary',
                                         icon=fac.AntdIcon(icon='md-launch'),
                                         style={'fontFamily': 'DingTalkTi'},
                                         ),

                      ],
                          style={'textAlign': 'right', 'margin-right':'2vw'},
                          span=24,
                      ),
                  ] if add_mode else []),




            ])
        ])

    ])
    return doc_content



def render_edit_code_item_modal():
    return fuc.FefferyDiv([
        fac.AntdForm([

            fac.AntdCenter([
                fac.AntdText('No.1',
                             id='config-text-editCodeThemeID',
                             style={'fontFamily': 'DingTalkTi',
                                    'fontSize': '20px',
                                    'color': 'gray',
                                    'marginRight':'4px'},
                             ),

                fac.AntdSpace([
                    fac.AntdText('账单类型',
                                 id='config-text-editCodeBillCnName', 
                                 style={'fontFamily': 'DingTalkTi',
                                        'fontSize': '32px'}
                                 ),
                    fac.AntdTag(content='BD001', color='gold',
                                id='config-tag-editCodeBillIDBase', 
                                ),
                ],
                    align='start',
                )
            ]),

            fac.AntdCenter(
                fac.AntdText('billdict_bill_type',
                             id='config-text-editCodeBillEnName', 
                             style={'fontFamily': 'DingTalkTi',
                                    'fontSize': '12px',
                                    'color':'gray'}
                             ),
                style={'marginBottom':'24px'}
            ),

            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdInput(
                        id= 'config-input-editCodeCodeKey', 
                        style={'width': '100%'}
                    ),
                    id='config-formItem-editCodeCodeKey',
                    label=fac.AntdText('码键',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                    required=True,
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-editCodeCodeValue', 
                        style={'width': '100%'}
                    ),
                    id='config-formItem-editCodeCodeValue', 
                    label=fac.AntdText('码值',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                    required=True,
                ),
            ],
                justify='space-between',
            ),




            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-editCodeCodeSort', 
                    ),
                    id='config-formItem-editCodeCodeSort',
                    label=fac.AntdText('显示排序',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-editCodeFatherKey', 
                        disabled=True,
                    ),
                    id='config-formItem-editCodeFatherKey', 
                    label=fac.AntdText('父键',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-editCodeLevel', 
                        disabled=True,
                    ),
                    id='config-formItem-editCodeLevel', 
                    label=fac.AntdText('所处层级',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

            ],
                justify='space-between',
                gap='8px',
            ),


            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdPopover(
                        fac.AntdInput(
                            id='config-input-editCodeIcon',
                            placeholder='点击此处选择图标',
                            readOnly=True,
                            # prefix=fac.AntdIcon(icon='antd-carry-out'),
                            # value='antd-carry-out',
                        ),
                        content=render_icon('editCode'),
                        trigger='click',
                        placement='bottom'
                    ),
                    id='config-formItem-editCodeIcon',
                    label=fac.AntdText('显示图标',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdColorPicker(
                        id='config-input-editCodeIconColor', 
                    ),
                    id='config-formItem-editCodeIconColor', 
                    label=fac.AntdText('显示颜色',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

            ],
                justify='space-between',
            ),


            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdRadioGroup(
                        id='config-radioGroup-editCodeIsDefault', 
                        options=[{'label': '是', 'value': '1'}, {'label': '否', 'value': '0'}],
                        defaultValue='0',
                        style={'width': '100%'}
                    ),
                    id='config-formItem-editCodeIsDefault', 
                    label=fac.AntdText('是否默认',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdRadioGroup(
                        id= 'config-radioGroup-editCodeStatus',
                        options=[{'label': '正常', 'value': '1'}, {'label': '禁用', 'value': '2'}],
                        defaultValue='1',
                        style={'width': '100%'}
                    ),
                    id='config-formItem-editCodeStatus',
                    label=fac.AntdText('码键状态',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),
            ],
                justify='space-between',
            ),

            fac.AntdFormItem(
                fac.AntdInput(
                    id='config-input-editCodeCssStyle', 
                    mode='text-area',
                    autoSize={'minRows': 3, 'maxRows': 3},
                    style={'width': '100%'}
                ),
                id='config-formItem-editCodeCssStyle', 
                label=fac.AntdText('显示样式',
                                   style={'fontFamily': 'DingTalkTi',
                                          'fontSize': '16px'}),
            ),

            fac.AntdFormItem(
                fac.AntdInput(
                    id='config-input-editCodeDictId', 
                ),
                id='config-formItem-editCodeDictId', 
                hidden=True,
            ),

            
            fac.AntdDivider(),

            html.Div(
                fac.AntdSpace([
                    fac.AntdFormItem(
                        fac.AntdButton('取消',
                                       id='config-button-cancelEditDictInfo',
                                       type='default', danger=True,
                                       icon=fac.AntdIcon(icon='antd-close-circle'),
                                       style={'fontFamily': 'DingTalkTi'}
                                       ),
                        hidden=False 
                    ),

                    fac.AntdFormItem(
                        fac.AntdButton('修改',
                                       id='config-button-submitEditDictInfo',
                                       type='primary',
                                       icon=fac.AntdIcon(icon='antd-edit'),
                                       style={'fontFamily': 'DingTalkTi'},
                                       ),
                        hidden=False
                    ),

                ],
                    size='large',
                ),
                style={'textAlign': 'right'}
            ),


        ],
            style={'margin':'0px 10% 0px 10%'},
        )
    ])


def render_add_code_item_modal():
    return fuc.FefferyDiv([
        fac.AntdForm([

            fac.AntdCenter([
                fac.AntdText('No.1',
                             id='config-text-addCodeThemeID',
                             style={'fontFamily': 'DingTalkTi',
                                    'fontSize': '20px',
                                    'color': 'gray',
                                    'marginRight':'4px'},
                             ),

                fac.AntdSpace([
                    fac.AntdText('账单类型',
                                 id='config-text-addCodeBillCnName',
                                 style={'fontFamily': 'DingTalkTi',
                                        'fontSize': '32px'}
                                 ),
                    fac.AntdTag(content='BD001', color='gold',
                                id='config-tag-addCodeBillIDBase',
                                ),
                ],
                    align='start',
                )
            ]),

            fac.AntdCenter(
                fac.AntdText('billdict_bill_type',
                             id='config-text-addCodeBillEnName',
                             style={'fontFamily': 'DingTalkTi',
                                    'fontSize': '12px',
                                    'color':'gray'}
                             ),
                style={'marginBottom':'24px'}
            ),

            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-addCodeCodeKey',
                        style={'width': '100%'}
                    ),
                    id='config-formItem-addCodeCodeKey',
                    label=fac.AntdText('码键',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                    required=True,
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-addCodeCodeValue',
                        style={'width': '100%'}
                    ),
                    id='config-formItem-addCodeCodeValue',
                    label=fac.AntdText('码值',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                    required=True,
                ),
            ],
                justify='space-between',
            ),




            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-addCodeCodeSort',
                    ),
                    id='config-formItem-addCodeCodeSort',
                    label=fac.AntdText('显示排序',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-addCodeFatherKey',
                        disabled=True,
                    ),
                    id='config-formItem-addCodeFatherKey',
                    label=fac.AntdText('父键',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdInput(
                        id='config-input-addCodeLevel',
                        disabled=True,
                    ),
                    id='config-formItem-addCodeLevel',
                    label=fac.AntdText('所处层级',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

            ],
                justify='space-between',
                gap='8px',
            ),


            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdPopover(
                        fac.AntdInput(
                            id='config-input-addCodeIcon',
                            placeholder='点击此处选择图标',
                            readOnly=True,
                            # prefix=fac.AntdIcon(icon='antd-carry-out'),
                            # value='antd-carry-out',
                        ),
                        content=render_icon('addCode'),
                        trigger='click',
                        placement='bottom'
                    ),
                    id='config-formItem-addCodeIcon',
                    label=fac.AntdText('显示图标',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdColorPicker(
                        id='config-input-addCodeIconColor',
                    ),
                    id='config-formItem-addCodeIconColor', 
                    label=fac.AntdText('显示颜色',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

            ],
                justify='space-between',
            ),


            fac.AntdFlex([
                fac.AntdFormItem(
                    fac.AntdRadioGroup(
                        id= 'config-radioGroup-addCodeIsDefault',
                        options=[{'label': '是', 'value': '1'}, {'label': '否', 'value': '0'}],
                        defaultValue='0',
                        style={'width': '100%'}
                    ),
                    id='config-formItem-addCodeIsDefault',
                    label=fac.AntdText('是否默认',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),

                fac.AntdFormItem(
                    fac.AntdRadioGroup(
                        id='config-radioGroup-addCodeStatus', 
                        options=[{'label': '正常', 'value': '1'}, {'label': '禁用', 'value': '2'}],
                        defaultValue='1',
                        style={'width': '100%'}
                    ),
                    id='config-formItem-addCodeStatus', 
                    label=fac.AntdText('码键状态',
                                       style={'fontFamily': 'DingTalkTi',
                                              'fontSize': '16px'}),
                ),
            ],
                justify='space-between',
            ),

            fac.AntdFormItem(
                fac.AntdInput(
                    id='config-input-addCodeCssStyle',
                    mode='text-area',
                    autoSize={'minRows': 3, 'maxRows': 3},
                    style={'width': '100%'}
                ),
                id='config-formItem-addCodeCssStyle',
                label=fac.AntdText('显示样式',
                                   style={'fontFamily': 'DingTalkTi',
                                          'fontSize': '16px'}),
            ),

            fac.AntdDivider(),

            html.Div(
                fac.AntdSpace([
                    fac.AntdFormItem(
                        fac.AntdButton('重置',
                                       id='config-button-resetDictInfo',
                                       type='default', danger=True,
                                       icon=fac.AntdIcon(icon='antd-sync'),
                                       style={'fontFamily': 'DingTalkTi'}
                                       ),
                        hidden=False
                    ),

                    fac.AntdFormItem(
                        fac.AntdButton('提交',
                                       id='config-button-submitAddDictInfo',
                                       type='primary',
                                       icon=fac.AntdIcon(icon='antd-send'),
                                       style={'fontFamily': 'DingTalkTi'},
                                       ),
                        hidden=False 
                    ),

                ],
                    size='large',
                ),
                style={'textAlign': 'right'}
            ),


        ],
            style={'margin':'0px 10% 0px 10%'},
        )
    ])




def render_icon(obj):
    return html.Div(
        [
            fac.AntdRadioGroup(
                id=f'config-radioGroup-iconList-{obj}',
                options=[
                    {
                        'label': fac.AntdIcon(
                            icon=icon,
                        ),
                        'value': icon
                    }
                    for icon in ICON_LIST
                ],
                style={
                    'width': 450,
                    'paddingLeft': '10px'
                }
            ),
        ],
        style={
            'maxHeight': '135px',
            'overflow': 'auto'
        }
    )




def render_switch_theme_tabitems(theme_market_data=None):
    if theme_market_data is None:
        theme_market_data = {'SELF':[], 'OTHER':[]}
    return fac.AntdTabs(
                items=[
                    {'key':'self', 'label':'我的主题', 'children':[
                        fac.AntdCenter(
                            fac.AntdSpace([
                                fac.AntdButton(
                                    children=fac.AntdTag(content=f'{theme_info["theme_label"]}',
                                                        color="red" if theme_info["theme_id"] == session["theme_id"] else "gray"),
                                    id={'index':'config-button-tag-switchTheme', 'type':f'{theme_info["theme_id"]}'},
                                    type='text'
                                ) for theme_info in theme_market_data['SELF']
                            ],
                                id='config-space-selfTheme',
                                direction='vertical',
                            ),
                        ),
                    ]},
                    {'key':'market', 'label':'主题超市', 'children':[
                        fac.AntdCenter(
                            fac.AntdSpace([
                                fac.AntdButton(
                                    children=fac.AntdTag(content=f'{theme_info["theme_label"]}'),
                                    id={'index':'config-button-tag-switchTheme', 'type':f'{theme_info["theme_id"]}'},
                                    type='text'
                                ) for theme_info in theme_market_data['OTHER']
                            ],
                                id='config-space-marketTheme',
                                direction='vertical',
                            ),
                        ),
                    ]},
                ],
            )


from server import app
from dash.dependencies import Input, Output, State, MATCH, ALL, ClientsideFunction
from dash import set_props, ctx
from flask import session
import re

from api.apis import (get_bill_theme_by_id_api, edit_bill_dict_code_api, get_bill_dict_code_by_key_api, init_bill_theme_api, edit_bill_theme_api,
                      get_current_user_info_api, add_bill_dict_code_api, del_bill_dict_codes_api, switch_bill_theme_api, add_user_theme_relation_api,
                      get_current_user_theme_infos_api, get_market_theme_infos_api, get_bill_dict_code_list_api, check_dict_code_has_bill_api)

from views.view_utils import get_bill_config_table_data_from_bill_dict_data



def config_common_update_theme_market_cache():
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


### 展开新增主题/编辑主题的Modal
app.clientside_callback(
    ClientsideFunction(namespace="BillConfig", function_name="renderAddOrEditBillThemeModal"),
    Input({'type': 'config-button-showThemeEditAddModal', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True
)


@app.callback(
    [Output({'index':'config-input-themeId', 'type':'edit'}, 'value'),
    Output({'index':'config-input-themeName', 'type':'edit'}, 'value'),
    Output({'index':'config-input-themeDescribe', 'type':'edit'}, 'value'),
     Output('config-switch-themeStatus', 'checked')],
    Input("config-modal-editTheme", 'visible'),
    prevent_initial_call=True
)
def show_edit_modal_data(visible):
    if visible:
        get_res = get_bill_theme_by_id_api(theme_id=session['theme_id']) 
        if get_res["code"] == 200:
            theme = get_res["data"]
            return [
                str(theme.get('theme_id')),
                theme.get('theme_label'),
                theme.get('theme_desc'),
                True if theme.get('theme_status') == '1' else False,
            ]
    return [None, None, None, True]

@app.callback(
    [Output("config-modal-addTheme", "visible", allow_duplicate=True),
    Output('global-message-container', 'children', allow_duplicate=True),],
    Input('config-button-addBillTheme', 'nClicks'),
    State({'index': 'config-input-themeName', 'type': 'add' }, 'value'),
    State({'index': 'config-input-themeDescribe', 'type': 'add'}, 'value'),
    prevent_initial_call=True,
)
def add_new_theme(nClicks, themeName, themeDesc):
    if nClicks:

        init_bill_theme_res = init_bill_theme_api(page_obj={'theme_label':themeName, 'theme_desc':themeDesc})
        if init_bill_theme_res['code'] != 200:
            return [False, fuc.FefferyFancyMessage("新增账单主题及初始化" + init_bill_theme_res["message"], type='error')]
            
        get_user_res = get_current_user_info_api()
        if get_user_res['code'] != 200 :
            return  [False, None, None, fuc.FefferyFancyMessage("获取用户信息" + get_user_res.get('message'), type='error')]
        for ky, vl in get_user_res["data"].items():
            session[ky] = vl
        
        ## 更新关联信息
        config_common_update_theme_market_cache()
        
        ## 更新主题超市选项
        set_props(
            'config-store-billThemeChangeFlag',
            {'data':True}
        )
        
        return [False, fuc.FefferyFancyMessage("新增账单主题且初始化成功", type='success')]


    return [False, None]


@app.callback(
    Output('config-page-message-container', 'children', allow_duplicate=True),
    Input('config-button-editBillTheme', 'nClicks'),
    State({'index':'config-input-themeId', 'type': 'edit'}, 'value'),
    State({'index': 'config-input-themeName', 'type': 'edit' }, 'value'),
    State({'index': 'config-input-themeDescribe', 'type': 'edit'}, 'value'),
    State('config-switch-themeStatus', 'checked'),
    prevent_initial_call=True,
)
def edit_theme_info(nClicks, themeId, themeName, themeDesc, themeStatus):
    if nClicks:
        edit_res = edit_bill_theme_api(page_obj={'theme_id':themeId, 'theme_label':themeName, 'theme_desc':themeDesc,
                                                    'theme_status':'1' if themeStatus else '0'})
        if edit_res['code'] != 200:
            return fuc.FefferyFancyMessage("编辑账单主题信息" + edit_res["message"], type='error')
        
        ## 更新关联信息
        config_common_update_theme_market_cache()
        
        ## 更新主题超市选项
        set_props(
            'config-store-billThemeChangeFlag',
            {'data':True}
        )
        
        return fuc.FefferyFancyMessage("账单主题信息修改成功", type='success')

    return None








## 修改或删除账单主题后，关闭修改账单主题的Modal
app.clientside_callback(
    '''( nEditClicks, nDelClicks ) => {
    if ( nEditClicks  ||  nDelClicks ) {
        window.dash_clientside.set_props(
            "config-modal-editTheme",
            {
                "visible": false
            }
        )        
    }
    }''',
    [Input('config-button-editBillTheme', 'nClicks'),
     Input('config-button-deleteBillTheme', 'confirmCounts'),],
    prevent_initial_call = True
)


## 重置新增字典项的表单
app.clientside_callback(
    ClientsideFunction(namespace="BillConfig", function_name="resetAddCodeFormItem"),
    [Output('config-input-addCodeCodeKey', 'value'),
    Output('config-input-addCodeCodeValue', 'value'),
    Output('config-input-addCodeCodeSort', 'value'),
    Output('config-input-addCodeIcon', 'value'),
    Output('config-input-addCodeIconColor',  'value'),
    Output('config-radioGroup-addCodeIsDefault', 'value'),
    Output('config-radioGroup-addCodeStatus',  'value'),
    Output('config-input-addCodeCssStyle', 'value'),],
    Input('config-button-resetDictInfo', 'nClicks'),
    prevent_initial_call=True
)


## 渲染码值项中的图标选择
app.clientside_callback(
    ClientsideFunction(namespace="BillConfig", function_name="rederCodeItemIcon"),
    [Output('config-input-addCodeIcon', 'value', allow_duplicate=True),
     Output('config-input-addCodeIcon', 'prefix', allow_duplicate=True),
     Output('config-input-editCodeIcon', 'value', allow_duplicate=True,),
     Output('config-input-editCodeIcon', 'prefix', allow_duplicate=True,),],
    Input('config-radioGroup-iconList-addCode', 'value'),
    Input('config-radioGroup-iconList-editCode', 'value'),
    prevent_initial_call = True
)


## 关闭编辑编辑码值项的MODAL
app.clientside_callback(
    ClientsideFunction(namespace="BillConfig", function_name="cancelEditCodeItem"),
    Output('config-modal-editDict', 'visible', allow_duplicate=True),
    Input('config-button-cancelEditDictInfo', 'nClicks'),
    prevent_initial_call = True    
)


## 渲染新增账单字典的 modal
app.clientside_callback(
    ClientsideFunction(namespace="BillConfig", function_name="renderCodeItemAddModal"),
    [Output('config-modal-addDict', 'visible', allow_duplicate=True),
     Output('config-text-addCodeThemeID', 'children'),
     Output('config-text-addCodeBillCnName', 'children'),
     Output('config-tag-addCodeBillIDBase', 'content'),
     Output('config-text-addCodeBillEnName', 'children'),
     Output('config-input-addCodeFatherKey', 'value'),
     Output('config-input-addCodeLevel', 'value'),
     ],
    Input('config-table-billDictData', 'nClicksButton'),
    State('config-table-billDictData', 'clickedContent'),
    State('config-table-billDictData', 'clickedCustom'),
    State('bill-dict-data-store', 'data'),
    prevent_initial_call=True   
)


# @app.callback(
#     [Output('config-modal-addDict', 'visible', allow_duplicate=True),
#      Output('config-text-addCodeThemeID', 'children'),
#      Output('config-text-addCodeBillCnName', 'children'),
#      Output('config-tag-addCodeBillIDBase', 'content'),
#      Output('config-text-addCodeBillEnName', 'children'),
#      Output('config-input-addCodeFatherKey', 'value'),
#      Output('config-input-addCodeLevel', 'value'),
#      Output('config-message-container2', 'children', allow_duplicate=True),
#      ],
#     Input('config-table-billDictData', 'nClicksButton'),
#     State('config-table-billDictData', 'clickedContent'),
#     State('config-table-billDictData', 'clickedCustom'),
#     State('bill-dict-data-store', 'data'),
#     prevent_initial_call=True
# )
# def render_code_item_add_modal(nClicks, content, bill_id, old_codes):
#     if nClicks:
#         theme_id = session['theme_id']
#         dict_info = bill_id.split('-')
#         if len(dict_info) <= 1:
#             dict_id_base = dict_info[0]
#             code_key = ''
#             level = 1
#         else:
#             [dict_id_base, code_key] =  dict_info
#             level = 2


#         dict_cn_name, dict_en_name = '', ''
#         for ii in old_codes:
#             if ii.get('dict_id_base') == dict_id_base:
#                 dict_cn_name = ii.get('dict_cn_name')
#                 dict_en_name = ii.get('dict_en_name')
#                 break

#         if content == '新增':                
#             return [True, f"No.{theme_id}", dict_cn_name, dict_id_base, dict_en_name, code_key, str(level), None]
    
#     return [False, None, None, None, None, None, None, None]


@app.callback(
    [Output('config-modal-editDict', 'visible', allow_duplicate=True),
     Output('config-input-editCodeCodeKey', 'disabled'),
     Output('config-input-editCodeCodeValue', 'disabled'),
     Output('config-text-editCodeThemeID', 'children'),
     Output('config-text-editCodeBillCnName', 'children'),
     Output('config-tag-editCodeBillIDBase', 'content'),
     Output('config-text-editCodeBillEnName', 'children'),
     Output('config-input-editCodeCodeKey', 'value'),
     Output('config-input-editCodeCodeValue', 'value'),
     Output('config-input-editCodeCodeSort', 'value'),
     Output('config-input-editCodeFatherKey', 'value'),
     Output('config-input-editCodeLevel', 'value'),
     Output('config-input-editCodeIcon', 'value'),
     Output('config-input-editCodeIconColor', 'value'),
     Output('config-radioGroup-editCodeIsDefault', 'value'),
     Output('config-radioGroup-editCodeStatus', 'value'),
     Output('config-input-editCodeCssStyle', 'value'),
     Output('config-input-editCodeDictId', 'value'),
     Output('config-message-container1', 'children', allow_duplicate=True),
     ],
    Input('config-table-billDictData', 'nClicksButton'),
    State('config-table-billDictData', 'clickedContent'),
    State('config-table-billDictData', 'clickedCustom'),
    State('bill-dict-data-store', 'data'),
    prevent_initial_call=True
)
def render_code_item_edit_modal(nClicks, content, bill_id, old_codes):
    if nClicks:
        theme_id = session['theme_id']
        dict_info = bill_id.split('-')
        if len(dict_info) <= 1:
            dict_id_base = dict_info[0]
            code_key = ''
        else:
            [dict_id_base, code_key] =  dict_info

        dict_cn_name, dict_en_name = '', ''
        for ii in old_codes:
            if ii.get('dict_id_base') == dict_id_base:
                dict_cn_name = ii.get('dict_cn_name')
                dict_en_name = ii.get('dict_en_name')
                break 

        if content == '编辑':
            ## 查询码值是否存在
            get_code_res = get_bill_dict_code_by_key_api(theme_id=theme_id, dict_id=dict_id_base, code_key=code_key)
            if get_code_res["code"] != 200:
                return [ False, True, True, ] + [None, ] * 14 + [fuc.FefferyFancyMessage("查询账单码值" + get_code_res["message"], type='error'), ]
            
            ## 获取对应的码值下是否存在账单数据
            check_res = check_dict_code_has_bill_api(theme_id=theme_id, dict_id=dict_id_base, code_key=code_key)
            
            is_disable = True
            if check_res["code"] == 200:
                is_disable = True if check_res["data"] == 'Y' else False
                                   
            res = get_code_res['data']

            return [
                True, is_disable, is_disable, f"No.{theme_id}", dict_cn_name, dict_id_base, dict_en_name, 
                res.get('code_key'), res.get('code_value'), str(res.get('code_sort')), res.get('father_key'), str(res.get('level')),
                res.get('icon'), res.get('icon_color'), res.get('is_default'), res.get('status'), res.get('icon_css'), str(res.get('dict_id')),
                None
                ]
    
    return [False, True, True, ] + [None, ] * 16

@app.callback(
    Output('config-page-message-container', 'children', allow_duplicate=True),
    Input('config-table-billDictData', 'nClicksButton'),
    State('config-table-billDictData', 'clickedContent'),
    State('config-table-billDictData', 'clickedCustom'),
    prevent_initial_call=True
)
def del_code_item(nClicks, content, bill_id):
    """ 删除码值"""    
    if nClicks:
        theme_id = session['theme_id']
        dict_info = bill_id.split('-')
        if len(dict_info) <= 1:
            dict_id_base = dict_info[0]
            code_key = ''
            level = 1
        else:
            [dict_id_base, code_key] =  dict_info
            level = 2
                    
        if content == '删除': 
            page_obj = {
                "del_mode":"by_key",
                "theme_id":theme_id,
                "dict_id_base":dict_id_base,
                "code_key":None if level <= 1 else code_key,
                "is_multiple":True if level <= 1 else False
                }
            del_code_res = del_bill_dict_codes_api(page_obj)
            if del_code_res["code"] != 200:
                return fuc.FefferyFancyMessage("删除账单码值" + del_code_res["message"], type='error')

            set_props(
                'config-store-billDictCodeItemChangeFlag',
                {'data': True}
            )

            return fuc.FefferyFancyMessage("删除账单码值成功", type='success')
    
    return None


@app.callback(
    [Output('config-modal-editDict', 'visible',  allow_duplicate=True),
    Output('config-page-message-container', 'children', allow_duplicate=True),],
    Input('config-button-submitEditDictInfo', 'nClicks'),
    State('config-text-editCodeThemeID',  'children'),
    State('config-text-editCodeBillCnName', 'children'),
    State('config-tag-editCodeBillIDBase', 'content'),
    State('config-text-editCodeBillEnName', 'children'),
    State('config-input-editCodeCodeKey', 'value'),
    State('config-input-editCodeCodeValue', 'value'),
    State('config-input-editCodeCodeSort', 'value'),
    State('config-input-editCodeFatherKey', 'value'),
    State('config-input-editCodeLevel', 'value'),
    State('config-input-editCodeIcon', 'value'),
    State('config-input-editCodeIconColor',  'value'),
    State('config-radioGroup-editCodeIsDefault', 'value'),
    State('config-radioGroup-editCodeStatus',  'value'),
    State('config-input-editCodeCssStyle', 'value'),
    State('config-input-editCodeDictId', 'value'),
    prevent_initial_call=True
)
def submit_code_item_edit_content(nClicks, themeID, billCnName, billIDBase, billEnName, codeKey, codeValue, codeSort,
                             fatherKey, level, icon, iconColor, isDefault, status, cssStyle, dictId):
    ''' 修改账单字典码值信息 '''    
    if nClicks:
        page_obj = {
            'dict_id':dictId,
            'dict_id_base': billIDBase,
            'dict_cn_name': billCnName,
            'dict_en_name': billEnName,
            'code_key': codeKey,
            'father_key': fatherKey,
            'level': level,
            'code_sort': codeSort,
            'code_value': codeValue,
            'icon': icon,
            'icon_color': iconColor,
            'icon_css': cssStyle,
            'is_default': isDefault,
            'status': status,
            'update_by': session['user_id'],
            'theme_id': themeID.replace('No.', ''),
        }

        edit_code_res = edit_bill_dict_code_api(page_obj=page_obj)
        if edit_code_res["code"] == 200:
            set_props(
                'config-store-billDictCodeItemChangeFlag',
                {'data': True}
            )
            return [
                False,
                fuc.FefferyFancyMessage('账单字典码值编辑成功', type='success' )
                ]
        else:
            return [False, fuc.FefferyFancyMessage("编辑账单码值" + edit_code_res['message'], type='error')]
             
    return [False, None]



@app.callback(
    [Output('config-modal-addDict', 'visible',  allow_duplicate=True),
    Output('config-page-message-container', 'children', allow_duplicate=True),],
    Input('config-button-submitAddDictInfo', 'nClicks'),
    State('config-text-addCodeThemeID',  'children'),
    State('config-text-addCodeBillCnName', 'children'),
    State('config-tag-addCodeBillIDBase', 'content'),
    State('config-text-addCodeBillEnName', 'children'),
    State('config-input-addCodeCodeKey', 'value'),
    State('config-input-addCodeCodeValue', 'value'),
    State('config-input-addCodeCodeSort', 'value'),
    State('config-input-addCodeFatherKey', 'value'),
    State('config-input-addCodeLevel', 'value'),
    State('config-input-addCodeIcon', 'value'),
    State('config-input-addCodeIconColor',  'value'),
    State('config-radioGroup-addCodeIsDefault', 'value'),
    State('config-radioGroup-addCodeStatus',  'value'),
    State('config-input-addCodeCssStyle', 'value'),
    prevent_initial_call=True
)
def submit_code_item_add_content(nClicks, themeID, billCnName, billIDBase, billEnName, codeKey, codeValue, codeSort,
                                 fatherKey, level, icon, iconColor, isDefault, status, cssStyle):
    ''' 新增账单字典码值项'''
    if nClicks:
        page_obj = {
            'dict_id_base': billIDBase,
            'dict_cn_name': billCnName,
            'dict_en_name': billEnName,
            'code_key': codeKey,
            'father_key': fatherKey,
            'level': level,
            'code_sort': codeSort,
            'code_value': codeValue,
            'icon': icon,
            'icon_color': iconColor,
            'icon_css': cssStyle,
            'is_default': isDefault,
            'status': status,
            'update_by': session['user_id'],
            'theme_id': themeID.replace('No.', ''),
        }


        add_code_res = add_bill_dict_code_api(page_obj=page_obj)
        if add_code_res["code"] == 200:
            
            set_props(
                'config-store-billDictCodeItemChangeFlag',
                {'data': True}
            )
            
            return [
                False,
                fuc.FefferyFancyMessage('账单字典码值新增成功', type='success' )
                ]
        else:
            return [False, fuc.FefferyFancyMessage("新增账单码值" + add_code_res['message'], type='error')]
            
    return [False, None]


@app.callback(
    [Output('config-page-message-container', 'children', allow_duplicate=True),
     Output('config-store-billThemeChangeFlag', 'data', allow_duplicate=True),
     Output('config-store-billDictCodeItemChangeFlag', 'data', allow_duplicate=True),
     Output('confog-popover-themeMarket', 'open')],
    Input({'index':'config-button-tag-switchTheme', 'type':ALL}, 'nClicks'),
    State('bill-theme-market-info', 'data'),
    prevent_initial_call=True
)
def switch_bill_theme(nClicks, bill_theme_info):
    ''' 切换当前的账单主题'''

    if any(nClicks):
        theme_id=int(dash.ctx.triggered_id["type"])

        ## 切换
        switch_res =  switch_bill_theme_api(theme_id=theme_id )
        if switch_res["code"] != 200:
            return [fuc.FefferyFancyMessage("切换账单主题" + switch_res['message'], type='error'), False, False, False]

        ## 刷新用户信息
        get_user_res = get_current_user_info_api()
        if get_user_res['code'] != 200 :
            return  [fuc.FefferyFancyMessage("获取当前用户信息" + get_user_res['message'], type='error'), False, False, False]
        for ky, vl in get_user_res["data"].items():
            session[ky] = vl


        ## 增加关联信息
        market_ids = [f.get('theme_id') for f in bill_theme_info['OTHER']]
        if theme_id in market_ids:
            add_relation_res = add_user_theme_relation_api(theme_id=theme_id)
            
            if add_relation_res["code"] != 200:
                return [fuc.FefferyFancyMessage("关联用户主题" + add_relation_res['message'], type='error'), False, False, False]

            ## 更新关联信息
            config_common_update_theme_market_cache()
              
        return [None, True, True, False]
   
    return [None, False, False, False]



@app.callback(
    [Output('confog-popover-themeMarket', 'content'),
     Output('config-store-billThemeChangeFlag', 'data', allow_duplicate=True)],
    Input('config-store-billThemeChangeFlag', 'data'),
    State('bill-theme-market-info', 'data'),
    prevent_initial_call=True    
)
def update_switch_billtheme_tabitems(change_flag, theme_market_data):
    if change_flag:
        pop_content = render_switch_theme_tabitems(theme_market_data)

        return [pop_content, False] 

    return [dash.no_update, False]



@app.callback(
    [Output('config-table-billDictData', 'data'),
     Output('config-store-billDictCodeItemChangeFlag', 'data', allow_duplicate=True)],
    Input('config-store-billDictCodeItemChangeFlag', 'data'),
    prevent_initial_call=True      
)
def update_bill_code_items(change_flag):
    if change_flag:
        
        ## 获取账单字典数据
        get_bill_code_list_res = get_bill_dict_code_list_api(theme_id=session['theme_id'] )
        bill_dict_data = get_bill_code_list_res['data'] if get_bill_code_list_res["code"] == 200 else []
        
        set_props(
            'bill-dict-data-store',
            {'data': bill_dict_data}               
        )
        
        return [get_bill_config_table_data_from_bill_dict_data(bill_dict_data), False]
    return [dash.no_update, False]