#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:39:24    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:39:24 


## 生成一些测试的账单数据

import time
import random
import pandas as pd

from module.dao import BillDetDao
from config.dbconfig import SessionLocal

bill_name_list = ['A01', 'A02', 'A03', 'A04', 'C01', 'C02', 'C03', 'C04', 'C05', 'E01', 'E02', 'E03', 'F01', 'F02', 'F03', 'F04', 'F05', 'G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'H01', 'H02', 'H03', 'H04', 'H05', 'I01', 'I02', 'I03', 'I04', 'Z01']
pay_channel_list = ['B001', 'B002', 'B003', 'B004', 'B005', 'B006', 'B007', 'B008', 'B999', 'C001', 'C002', 'H001', 'H002', 'H003', 'H004', 'H005', 'H999']
settle_channel_list =['HQ001', 'HQ002', 'HQ003', 'HQ004', 'HQ999', 'XQ001', 'YQ001', 'YQ002', 'YQ003', 'YQ004', 'YQ005', 'YQ006', 'YQ999']
bill_scene_list = ['W', 'S', 'Y']
bill_object_list = ['FR', 'HO', 'OT', 'SE',]
bill_status = {'00':0.95, '01':0.05}

bill_date_list = [f.strftime('%Y-%m-%d') for f in pd.date_range(start='2024-01-01', end='2024-12-31')]

bill_amont_range = {'01':[0, 50], '02':[50, 1000], '03':[1000, 10000], '04':[10000, 100000]}


user_id = 'SYS0001'
theme_id = 1
into_unix_time = int(time.time())
bills = []
for i in range(1000):
    bill_id = f'A{i + 1:06d}'
    bill_name = random.choice(bill_name_list)
    bill_type = bill_name[0]
    pay_channel = random.choice(pay_channel_list)
    settle_channel = random.choice(settle_channel_list)
    bill_object = random.choice(bill_object_list)
    bill_scene = random.choice(bill_scene_list)
    r = random.random()
    bill_status = '01' if r > 0.95 else '00' 
    r = random.random()
    if r <= 0.75:
        bill_amount = round(random.random() * 50, 2)
    elif r <= 0.9:
        bill_amount = 50 + round(random.random() * 950, 2)
    elif r <= 0.98:
        bill_amount = 1000 + round(random.random() * 9000, 2)
    else:
        bill_amount = 10000 + round(random.random() * 90000, 2)
    remark = ''
    bill_date = random.choice(bill_date_list)
    bill = [bill_id, bill_name,  bill_type, bill_amount, bill_date, pay_channel, settle_channel, bill_object, bill_scene, remark, bill_status, user_id, theme_id, into_unix_time ]
    bills.append(bill)
    

bills = pd.DataFrame(bills, columns=['bill_id', 'bill_name', 'bill_type', 'bill_amount', 'bill_date', 'pay_channel', 'settle_channel', 'consume_object', 'bill_scene', 'remark', 'bill_status', 'user_id', 'theme_id', 'into_unix_time'])


db = SessionLocal()
BillDetDao.batch_insert_bills(db, bills.to_dict('records'))
try:
    db.commit()
except:
    db.rollback()
db.close

