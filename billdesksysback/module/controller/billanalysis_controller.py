#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import datetime

from fastapi import APIRouter, Depends, Request
from module.service import get_current_user, BillAnalysisService
from module.entity import CrudRSModel, CurrentUserInfoServiceRSModel, QueryBillModel, AnalyzeBillModel

from sqlalchemy.orm import Session
from config.get_db import get_db
from utils.response import response_200, response_400, response_500
from module.decorators.log_decorators import log_decorator

from utils.log import logger
import traceback

billAnalysisController = APIRouter(dependencies=[Depends(get_current_user)])


@billAnalysisController.post("/analyzeBill", response_model=CrudRSModel)
@log_decorator(title="账单分析", business_type=4, log_type='operation')
async def analyze_bill(request: Request, query_bill: QueryBillModel,  analysis_params:AnalyzeBillModel, query_db: Session = Depends(get_db)):
    try:
        result = BillAnalysisService.analyze_bills(query_db, query_object=query_bill, analyze_object=analysis_params)
        if result.is_success:
            return response_200(data=result.data, message=result.message)
        else:
            return response_400(data=[], message=result.message)
    except Exception as e:
        logger.error(traceback.format_exc())
        return response_500(data=[], message=str(e))