<h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">Dash-Bill-System v0.2.0</h1>
<h4 align="center">基于Dash+FastAPI前后端分离的个人桌面/网页账单管理系统</h4>
<p align="center">
	<a href="https://gitee.com/xjcheng1993/dash-bill-system/tree/master"><img src="https://img.shields.io/badge/DashBillSystem-v0.2.0-brightgreen.svg"></a>
    <img src="https://img.shields.io/badge/python-3.9 | 3.10-blue">
</p>

## 平台简介

Dash-Bill-System是基于Dash-FastAPI-Admin开发的个人桌面/网页账单管理系统。

* 前端采用Dash、feffery-antd-components、feffery-utils-components。
* 后端采用FastAPI、sqlalchemy、MySQL、Redis、OAuth2 & Jwt。
* 特别鸣谢：<u>[feffery-antd-components](https://github.com/CNFeffery/feffery-antd-components)</u>，<u>[feffery-utils-components](https://github.com/CNFeffery/feffery-utils-components)</u>，<u>[feffery-antd-charts](https://github.com/CNFeffery/feffery-antd-charts)</u>，<u>[Dash-FastAPI-Admin](https://gitee.com/insistence2022/dash-fastapi-admin/tree/master)</u>。

## 内置功能

1.  用户管理模块：修改用户信息、修改用户密码；
2.  账单录入模块：录入账单信息、展示账单卡片；
3.  账单管理模块：自定义条件查询账单、查看账单、编辑账单、删除账单；
4.  账单分析模块：查看账单日历、分类汇总分析、账单趋势分析、账单类型分析、账单支付渠道分析、账单结算渠道分析、账单对象分析、账单场景分析；
5.  账单参数配置：增加账单主题、编辑账单主题、切换账单主题、增加账单字典、修改账单字典、删除账单字典。


## 演示图

<table>
    <tr>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/用户登录.png"/></td>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/修改用户信息.png"/></td>
    </tr>
    <tr>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/新增账单.png"/></td>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/账单卡片.png"/></td>
    </tr>
    <tr>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/账单分析.png"/></td>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/账单日历.png"/></td>
    </tr>
    <tr>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/账单管理.png"/></td>
        <td><img src="https://gitee.com/xjcheng1993/dash-bill-system/raw/master/demo-pictures/账单码表配置.png"/></td>
    </tr>	 
</table>


## 项目运行相关

### 后端
```bash
# 进入后端目录
cd billdesksysback

# 安装后端依赖环境
pip install -r requirements.txt

# 配置环境
1.在config/env.py的DataBaseConfig类中配置数据库环境
2.在config/env.py的RedisConfig类中配置redis环境

# 准备数据库
1.新建数据库 billwebsys 
2.使用命令或数据库连接工具运行sql文件夹下的billsys.sql

# 准备测试用的账单数据
python data_prepare.py

# 运行后端
python app.py
```


### 网页端使用
```bash
# 进入前端目录
cd billdesksys

# 安装前端依赖环境
pip install -r requirements.txt

# 注释以下代码 app.py Line 122-132
@app.callback(
    Output('platform-content', 'children', allow_duplicate=True), 
    Input('listen-unload', 'unloaded'),
    prevent_initial_call=True
)
def listen_unload_demo(unloaded):
    ''' 退出清理资源，如页面全部退出，自动停止服务'''
    if unloaded:
        os._exit(0)
    return dash.no_update

# 运行前端
python wsgi.py

# 浏览器访问
地址：http://127.0.0.1:19880
```

### 桌面端使用
```bash
# 进入前端目录
cd billdesksys

# 安装前端依赖环境
pip install -r requirements.txt

# pyinstall 打包程序
pyinstaller main.spec

# 等打包程序结束，找到打包文件路径 dist/main/main.exe
双击运行 main.exe
```

### 访问
```bash
# 默认账号密码
账号：admin
密码：123456
```