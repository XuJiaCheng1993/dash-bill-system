#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import pandas as pd
import feffery_antd_components as fac
from dash import html



def get_bill_form_options_from_bill_dict_data(bill_dict_data_list):
    ''' 根据账单字典列表转换成各组件的OPTIONS'''

    def get_select_component_option(bill_dict, dict_id):
        options = [
            {
                'label': html.Span([
                    fac.AntdTag(content=f.get('code_key'), color=f.get('icon_color')),
                    f.get('code_value')
                ]),
                'value': f.get('code_key')}
            for f in bill_dict.get(dict_id)
        ]
        default = [
            f.get('code_key')
            for f in bill_dict.get(dict_id)
            if f.get('is_default') == '1'
        ]
        return {'options': options, 'default': default[0]}

    def get_treeselector_component_option(bill_dict, dict_id):
        options = [
            {
                'key': f.get('code_key'),
                'value': f.get('code_key'),
                'title': f.get('code_value'),
                'children': [
                    {
                        'key': c.get('code_key'),
                        'value': c.get('code_key'),
                        'title': c.get('code_value')
                    }
                    for c in f.get('children')
                ]
            }
            for f in bill_dict.get(dict_id)
        ]

        options_extra = dict(
            {
                g.get('code_key') : html.Span([
                    fac.AntdTag(content=g.get('code_key'), color=g.get('icon_color')),
                    g.get('code_value')
                ])
                for f in bill_dict.get(dict_id) for g in f.get('children')
            },
            **{
                f.get('code_key'): html.Span([
                    fac.AntdTag(content=f.get('code_key'), color=f.get('icon_color')),
                    f.get('code_value')
                ])
                for f in bill_dict.get(dict_id)
            }
        )

        default = [
            g.get('code_key')
            for f in bill_dict.get(dict_id)
            for g in f.get('children')
            if g.get('is_default') == '1'
        ]

        return {'options': options, 'options_extra': options_extra, 'default': default[0] if default else ''}

    def get_radiogroup_component_option(bill_dict, dict_id):
        options = [
            {
                'label': f.get('code_value'),
                'value': f.get('code_key')
            }
            for f in bill_dict.get(dict_id)
        ]

        default = [
            f.get('code_key')
            for f in bill_dict.get(dict_id)
            if f.get('is_default') == '1'
        ]
        return {'options': options, 'default': default[0] if default else ''}


    def get_switch_component_option(bill_dict, dict_id):
        check = [
            {
                'icon': 'custom-icon custom-icon-' + f.get('icon'),
                'color': f.get('icon_color')
            }
            for f in bill_dict.get(dict_id) if f.get('is_default') == '1'
        ]

        uncheck = [
            {
                'icon': 'custom-icon custom-icon-' + f.get('icon'),
                'color': f.get('icon_color')}
            for f in  bill_dict.get(dict_id) if f.get('is_default') == '0'
        ]
        return {'check': check[0] if check else {}, 'uncheck': uncheck[0] if uncheck else {}}


    ## 账单字典列表转化成Dataframe
    data = pd.DataFrame(bill_dict_data_list)

    ## 转换成嵌套dict的形式
    bill_dict = {}
    for bdidx in data['dict_id_base'].unique():
        tmp = data[data['dict_id_base'] == bdidx].sort_values(by=['father_key', 'code_sort']).copy()

        max_level = tmp['level'].max()

        if max_level <= 1:
            options = tmp.to_dict('records')

        else:
            options = []
            for ky in tmp[tmp['level'] == 1]['code_key'].unique():
                parent = tmp[tmp['code_key'] == ky].to_dict('records')[0]
                children = tmp[tmp['father_key'] == ky].to_dict('records')
                parent.update({'children': children})
                options.append(parent)

        bill_dict.update({bdidx: options})

    ## 转换成各组件的options
    options = {
        'bill_type':get_select_component_option(bill_dict, 'BD001'),
        'bill_name':get_treeselector_component_option(bill_dict, 'BD001'),
        'pay_channel': get_treeselector_component_option(bill_dict, 'BD002'),
        'settle_channel': get_treeselector_component_option(bill_dict, 'BD003'),
        'bill_object': get_radiogroup_component_option(bill_dict, 'BD004'),
        'bill_scene': get_radiogroup_component_option(bill_dict, 'BD005'),
        'bill_status':get_switch_component_option(bill_dict, 'BD006'),
        'bill_status_select':get_select_component_option(bill_dict, 'BD006'),
    }
    return options


def get_bill_config_table_data_from_bill_dict_data(bill_dict_data_list):


    for per in bill_dict_data_list:
        if per.get('level') <= 1 and per.get('dict_id_base') in ['BD001', 'BD002', 'BD003']:
            per.update({
                'operation':[
                    {'content': f'编辑', 'type': 'link', 'icon': 'antd-edit', 'custom': f'{per.get("dict_id_base")}-{per.get("code_key")}'},
                    {'content': f'新增', 'type': 'link', 'icon': 'antd-plus-circle', 'custom': f'{per.get("dict_id_base")}-{per.get("code_key")}'},
                    {'content': f'删除', 'type': 'link', 'icon': 'antd-delete', 'custom': f'{per.get("dict_id_base")}-{per.get("code_key")}'},
                ]
            })
        else:
            per.update({
                'operation':[
                    {'content': f'编辑', 'type': 'link', 'icon': 'antd-edit', 'custom': f'{per.get("dict_id_base")}-{per.get("code_key")}'},
                    {'content': f'删除', 'type': 'link', 'icon': 'antd-delete', 'custom': f'{per.get("dict_id_base")}-{per.get("code_key")}'},
                ]
            })

    data = pd.DataFrame(bill_dict_data_list)
    data = data[data['dict_id_base'] != 'BD006'].copy()

    table_data = []
    need_cols = ['code_key', 'code_value', 'code_sort', 'is_default', 'operation']
    for bdidx in data['dict_id_base'].unique():
        tmp = data[data['dict_id_base'] == bdidx].sort_values(by=['father_key', 'code_sort']).copy()

        max_level = tmp['level'].max()

        if max_level <= 1:
            options = tmp[need_cols].to_dict('records')

        else:
            options = []
            for ky in tmp[tmp['level'] == 1]['code_key'].unique():
                parent = tmp[tmp['code_key'] == ky][need_cols].to_dict('records')[0]
                children = tmp[tmp['father_key'] == ky][need_cols].to_dict('records')
                parent.update({'children': children})
                options.append(parent)

        table_data.append({
            'dict_id_base':bdidx,
            'dict_cn_name':tmp['dict_cn_name'].values[0],
            'operation':[
                # {'content': f'编辑', 'type': 'link', 'icon': 'antd-edit', 'custom': bdidx},
                {'content': f'新增', 'type': 'link', 'icon': 'antd-plus-circle', 'custom': bdidx},
            ],

            'children': options
        })

    return table_data


def transform_bill_card_data(bill_data):
    if not bill_data:
        return []
    
    bill_card_data = (
        pd.DataFrame(bill_data)
        .assign(xh = lambda df : df.index + 1,
                banner_id = lambda df: df.index % 5 + 1, )
        [['xh', 'banner_id', 'bill_name', 'pay_channel', 'settle_channel','bill_status', 'bill_amount','bill_date']]
        .to_dict('records')
    )
    return bill_card_data


ICON_LIST = [
    'antd-carry-out',
    'antd-car',
    'antd-bulb',
    'antd-build',
    'antd-bug',
    'antd-bar-code',
    'antd-branches',
    'antd-aim',
    'antd-issues-close',
    'antd-ellipsis',
    'antd-user',
    'antd-unlock',
    'antd-repair',
    'antd-team',
    'antd-sync',
    'antd-setting',
    'antd-send',
    'antd-schedule',
    'antd-save',
    'antd-rocket',
    'antd-reload',
    'antd-read',
    'antd-qrcode',
    'antd-power-off',
    'antd-number',
    'antd-notification',
    'antd-menu',
    'antd-mail',
    'antd-lock',
    'antd-loading',
    'antd-key',
    'antd-hourglass',
    'antd-global',
    'antd-function',
    'antd-import',
    'antd-export',
    'antd-dashboard',
    'antd-control',
    'antd-console-sql',
    'antd-compass',
    'antd-comment',
    'antd-code',
    'antd-cluster',
    'antd-clear',
    'antd-camera',
    'antd-book',
    'antd-catalog',
    'antd-api',
    'antd-alert',
    'antd-account-book',
    'antd-alipay',
    'antd-alipay-circle',
    'antd-weibo',
    'antd-github',
    'antd-fall',
    'antd-rise',
    'antd-stock',
    'antd-home',
    'antd-fund',
    'antd-area-chart',
    'antd-radar-chart',
    'antd-bar-chart',
    'antd-pie-chart',
    'antd-box-plot',
    'antd-dot-chart',
    'antd-line-chart',
    'antd-field-binary',
    'antd-field-number',
    'antd-field-string',
    'antd-field-time',
    'antd-file-add',
    'antd-file-done',
    'antd-file',
    'antd-file-image',
    'antd-file-markdown',
    'antd-file-pdf',
    'antd-file-protect',
    'antd-file-sync',
    'antd-file-text',
    'antd-file-word',
    'antd-file-zip',
    'antd-filter',
    'antd-fire',
    'antd-woman',
    'antd-arrow-up',
    'antd-arrow-down',
    'antd-arrow-left',
    'antd-arrow-right',
    'antd-flag',
    'antd-user-add',
    'antd-folder-add',
    'antd-man',
    'antd-tag',
    'antd-folder',
    'antd-user-delete',
    'antd-trophy',
    'antd-shopping-cart',
    'antd-folder-open',
    'antd-fork',
    'antd-select',
    'antd-tags',
    'antd-thunderbolt',
    'antd-sound',
    'antd-fund-projection-screen',
    'antd-funnel-plot',
    'antd-gift',
    'antd-robot',
    'antd-pushpin',
    'antd-printer',
    'antd-phone',
    'antd-picture',
    'antd-idcard',
    'antd-partition',
    'antd-monitor',
    'antd-more',
    'antd-apartment',
    'antd-money-collect',
    'antd-experiment',
    'antd-link',
    'antd-mobile',
    'antd-coffee',
    'antd-layout',
    'antd-eye',
    'antd-eye-invisible',
    'antd-exception',
    'antd-dollar',
    'antd-euro',
    'antd-download',
    'antd-environment',
    'antd-deployment-unit',
    'antd-crown',
    'antd-desktop',
    'antd-like',
    'antd-dislike',
    'antd-disconnect',
    'antd-app-store',
    'antd-app-store-add',
    'antd-bell',
    'antd-calculator',
    'antd-calendar',
    'antd-database',
    'antd-history',
    'antd-search',
    'antd-file-search',
    'antd-cloud',
    'antd-cloud-upload',
    'antd-cloud-download',
    'antd-cloud-server',
    'antd-cloud-sync',
    'antd-swap',
    'antd-rollback',
    'antd-login',
    'antd-logout',
    'antd-menu-fold',
    'antd-menu-unfold',
    'antd-full-screen',
    'antd-full-screen-exit',
    'antd-question-circle',
    'antd-plus-circle',
    'antd-minus-circle',
    'antd-info-circle',
    'antd-exclamation-circle',
    'antd-close-circle',
    'antd-check-circle',
    'antd-clock-circle',
    'antd-stop',
    'antd-edit',
    'antd-delete',
    'antd-highlight',
    'antd-redo',
    'antd-undo',
    'antd-zoom-in',
    'antd-zoom-out',
    'antd-sort-ascending',
    'antd-sort-descending',
    'antd-table',
    'antd-question',
    'antd-plus',
    'antd-minus',
    'antd-close',
    'antd-check',
    'antd-sketch',
    'antd-bank',
    'antd-block',
    'antd-insurance',
    'antd-smile',
    'antd-skin',
    'antd-star',
    'antd-right-circle-two-tone',
    'antd-left-circle-two-tone',
    'antd-up-circle-two-tone',
    'antd-down-circle-two-tone',
    'antd-up-square-two-tone',
    'antd-down-square-two-tone',
    'antd-left-square-two-tone',
    'antd-right-square-two-tone',
    'antd-question-circle-two-tone',
    'antd-plus-circle-two-tone',
    'antd-minus-circle-two-tone',
    'antd-plus-square-two-tone',
    'antd-minus-square-two-tone',
    'antd-info-circle-two-tone',
    'antd-exclamation-circle-two-tone',
    'antd-close-circle-two-tone',
    'antd-close-square-two-tone',
    'antd-check-circle-two-tone',
    'antd-check-square-two-tone',
    'antd-edit-two-tone',
    'antd-delete-two-tone',
    'antd-highlight-two-tone',
    'antd-pie-chart-two-tone',
    'antd-box-chart-two-tone',
    'antd-fund-two-tone',
    'antd-sliders-two-tone',
    'antd-api-two-tone',
    'antd-cloud-two-tone',
    'antd-hourglass-two-tone',
    'antd-notification-two-tone',
    'antd-tool-two-tone',
    'antd-down',
    'antd-up',
    'antd-left',
    'antd-right',
    'md-star-half',
    'md-star-border',
    'md-star',
    'md-people',
    'md-plus-one',
    'md-notifications',
    'md-pin-drop',
    'md-layers-clear',
    'md-layers',
    'md-edit-location',
    'md-tune',
    'md-transform',
    'md-timer-off',
    'md-timer',
    'md-file-upload',
    'md-file-download',
    'md-create-new-folder',
    'md-cloud-upload',
    'md-cloud-queue',
    'md-cloud-download',
    'md-cloud-done',
    'md-insert-chart',
    'md-functions',
    'md-format-quote',
    'md-attach-file',
    'md-storage',
    'md-save',
    'md-remove-circle-outline',
    'md-remove-circle',
    'md-remove',
    'md-low-priority',
    'md-link',
    'md-gesture',
    'md-forward',
    'md-flag',
    'md-drafts',
    'md-create',
    'md-content-paste',
    'md-content-cut',
    'md-content-copy',
    'md-clear',
    'md-block',
    'md-backspace',
    'md-add-box',
    'md-add',
    'md-add-circle-outline',
    'md-add-circle',
    'md-location-on',
    'md-mail-outline',
    'md-email',
    'md-not-interested',
    'md-library-books',
    'md-library-add',
    'md-equalizer',
    'md-add-alert',
    'md-visibility-off',
    'md-visibility',
    'md-verified-user',
    'md-update',
    'md-trending-up',
    'md-trending-flat',
    'md-trending-down',
    'md-translate',
    'md-toc',
    'md-timeline',
    'md-thumb-up',
    'md-thumb-down',
    'md-swap-vert',
    'md-swap-horiz',
    'md-supervisor-account',
    'md-subject',
    'md-settings',
    'md-search',
    'md-schedule',
    'md-restore',
    'md-query-builder',
    'md-power-settings-new',
    'md-opacity',
    'md-note-add',
    'md-lock-outline',
    'md-lock-open',
    'md-list',
    'md-lightbulb-outline',
    'md-launch',
    'md-label-outline',
    'md-label',
    'md-input',
    'md-info-outline',
    'md-info',
    'md-hourglass',
    'md-home',
    'md-history',
    'md-highlight-off',
    'md-help-outline',
    'md-help',
    'md-get-app',
    'md-translate',
    'md-fingerprint',
    'md-findIn-page',
    'md-favorite-border',
    'md-favorite',
    'md-extension',
    'md-explore',
    'md-exit-to-app',
    'md-event',
    'md-description',
    'md-delete-forever',
    'md-delete',
    'md-dashboard',
    'md-code',
    'md-build',
    'md-bug-report',
    'md-assignment',
    'md-assessment',
    'md-alarm-on',
    'md-alarm-off',
    'md-alarm-add',
    'md-alarm',
    'md-account-circle',
    'fc-vlc',
    'fc-view-details',
    'fc-upload',
    'fc-tree-structure',
    'fc-timeline',
    'fc-template',
    'fc-survey',
    'fc-signature',
    'fc-share',
    'fc-services',
    'fc-rules',
    'fc-questions',
    'fc-process',
    'fc-plus',
    'fc-overtime',
    'fc-organization',
    'fc-numerical-sorting21',
    'fc-numerical-sorting12',
    'fc-multiple-inputs',
    'fc-mind-map',
    'fc-menu',
    'fc-list',
    'fc-like',
    'fc-like-placeholder',
    'fc-info',
    'fc-import',
    'fc-image-file',
    'fc-idea',
    'fc-home',
    'fc-high-priority',
    'fc-low-priority',
    'fc-genealogy',
    'fc-full-trash',
    'fc-document-search',
    'fc-file',
    'fc-faq',
    'fc-export',
    'fc-empty-trash',
    'fc-download',
    'fc-document',
    'fc-deployment',
    'fc-delete-database',
    'fc-conference-call',
    'fc-database',
    'fc-data-protection',
    'fc-data-encryption',
    'fc-data-configuration',
    'fc-data-backup',
    'fc-checkmark',
    'fc-cancel',
    'fc-briefcase',
    'fc-binoculars',
    'fc-automatic',
    'fc-alphabetical-sorting-za',
    'fc-alphabetical-sorting-az',
    'fc-add-database',
    'fc-accept-database',
    'fc-about',
    'fc-radar-chart',
    'fc-scatter-chart',
    'fc-pie-chart',
    'fc-line-chart',
    'fc-flow-chart',
    'fc-doughnut-chart',
    'fc-bar-chart',
    'fc-area-chart',
    'fc-line-bar-chart',
    'fc-workflow',
    'fc-todo-list',
    'fc-synchronize',
    'fc-repair',
    'fc-statistics',
    'fc-settings',
    'fc-search',
    'fc-serial-tasks',
    'fc-safe',
    'fc-negative-dynamic',
    'fc-positive-dynamic',
    'fc-planner',
    'fc-parallel-tasks',
    'fc-org-unit',
    'fc-opened-folder',
    'fc-ok',
    'fc-inspection',
    'fc-globe',
    'fc-folder',
    'fc-electronics',
    'fc-data-sheet',
    'fc-command-line',
    'fc-calendar',
    'fc-calculator',
    'fc-bullish',
    'fc-bearish',
    'fc-bookmark',
    'fc-approval',
    'fc-advertising',
    'di-linux',
    'di-python',
    'di-chrome',
    'di-database',
    'di-firefox',
    'di-markdown',
    'di-postgresql',
    'di-terminal',
    'di-windows',
    'bi-table',
    'bi-analyse',
    'bi-layer',
    'bi-layer-minus',
    'bi-layer-plus',
    'bs-list-task',
    'bs-list-check',
    'bs-link',
    'bs-link-45-deg',
    'bs-envelope-open',
    'bs-envelope',
    'bs-alarm',
    'gi-mesh-network',
    'im-earth',
    'im-sphere'
]
