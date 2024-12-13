#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 09:49:59    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 09:49:59 

import os
import webview
import subprocess
from app import app


def get_empty_port(start_port, end_port):
    def is_empty_port(port):
        pipe = subprocess.Popen('netstat -an|findstr LIST|findstr "\<127.0.0.1:{}\>"'.format(port),
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        (stdoutput, erroutput) = pipe.communicate()
        return False if stdoutput.decode('gbk') else True

    for i in range(start_port, end_port + 1):
        if is_empty_port(i):
            return i


def start_app(port):
    app.run_server(port=port,
                   # debug=True,
                   # host='0.0.0.0'
                   )

def on_closed():
    ''' 退出dash服务'''
    os._exit(0)


if __name__ == '__main__':
    ## 查询空端口
    empty_port = get_empty_port(18080, 18130)


    window = webview.create_window(
        title='账单系统 ver0.2.0',
        url=f'http://127.0.0.1:{empty_port}/',
        confirm_close=True,		# 退出时提示
        width=1400,	# 自定义窗口大小
        height=1000,
        resizable=False
    )
    window.events.closed += on_closed

    # 自定义退出提示的中文内容
    cn = {
        'global.quitConfirmation': u'确定关闭?'
    }

    webview.start(start_app, (empty_port, ), localization=cn)







