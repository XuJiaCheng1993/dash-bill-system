#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 18:41:59    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 18:41:59 

from waitress import serve
from app import app

serve(
    app.server,
    host='127.0.0.1',
    port=19880
)