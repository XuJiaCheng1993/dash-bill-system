#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: uu    
# @Date: 2024-12-12 10:21:26    
# @Last Modified by:   uu    
# @Last Modified time: 2024-12-12 10:21:26 

import pandas as pd
from sqlalchemy.orm import Session
from module.entity import (
    QueryBillModel,
    CrudRSModel,
    EditBillModel,
    AddBillModel,
    CrudDataRSModel,
    BillModel,
    AnalyzeBillModel,
)
from module.dao import BillDetDao, BillDictDataDao
from utils.utils import query_to_dict
import time
from utils.log import logger
import traceback


class BillBaseService:

    @classmethod
    def get_bill_dict(cls, result_db: Session, theme_id: int):
        bill_dict = pd.DataFrame(
            [
                query_to_dict(f)
                for f in BillDictDataDao.query_dict_list_by_theme_id(
                    result_db, theme_id=theme_id
                )
            ]
        )

        dict_map = {}

        ## 账单类型码值映射
        tmp = bill_dict[
            (bill_dict["dict_id_base"] == "BD001") & (bill_dict["level"] == 1)
        ]
        dict_map.update(
            {"bill_type": {k: v for k, v in zip(tmp["code_key"], tmp["code_value"])}}
        )

        ## 账单名称码值映射
        tmp = bill_dict[
            (bill_dict["dict_id_base"] == "BD001") & (bill_dict["level"] == 2)
        ]
        dict_map.update(
            {"bill_name": {k: v for k, v in zip(tmp["code_key"], tmp["code_value"])}}
        )

        ## 支付渠道码值映射
        tmp = bill_dict[bill_dict["dict_id_base"] == "BD002"]
        dict_map.update(
            {"pay_channel": {k: v for k, v in zip(tmp["code_key"], tmp["code_value"])}}
        )

        ## 结算渠道码值映射
        tmp = bill_dict[bill_dict["dict_id_base"] == "BD003"]
        dict_map.update(
            {
                "settle_channel": {
                    k: v for k, v in zip(tmp["code_key"], tmp["code_value"])
                }
            }
        )

        ## 消费对象码值映射
        tmp = bill_dict[bill_dict["dict_id_base"] == "BD004"]
        dict_map.update(
            {
                "consume_object": {
                    k: v for k, v in zip(tmp["code_key"], tmp["code_value"])
                }
            }
        )

        ## 账单场景码值映射
        tmp = bill_dict[bill_dict["dict_id_base"] == "BD005"]
        dict_map.update(
            {"bill_scene": {k: v for k, v in zip(tmp["code_key"], tmp["code_value"])}}
        )

        ## 账单状态码值映射
        tmp = bill_dict[bill_dict["dict_id_base"] == "BD006"]
        dict_map.update(
            {"bill_status": {k: v for k, v in zip(tmp["code_key"], tmp["code_value"])}}
        )

        return dict_map


class BillService(BillBaseService):
    """
    账单记录服务
    """

    @classmethod
    def get_bill_by_id(cls, result_db: Session, bill_id: str):
        """
        根据账单编号查询账单记录
        """
        try:
            bill = BillDetDao.query_bill_by_id(result_db, bill_id=bill_id)
            if bill:
                result = dict(
                    is_success=True, message="查询成功", data=query_to_dict(bill)
                )
            else:
                result = dict(is_success=False, message="未查询到账单", data={})
        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, message="数据库查询失败", data={})

        return CrudDataRSModel(**result)

    @classmethod
    async def add_bill(cls, result_db: Session, page_object: AddBillModel):
        """
        新增单条账单记录
        """
        record = BillDetDao.query_bill_by_id(result_db, bill_id=page_object.bill_id)
        ## 判断账单是否已经存在
        if record:
            return CrudRSModel(is_success=False, message="该条账单记录已经存在")

        ## 补充 时间戳
        page_object.into_unix_time = int(time.time())

        ## 执行数据库操作
        try:
            BillDetDao.insert_bill(result_db, page_object)
            result_db.commit()
            result = dict(is_success=True, message="账单新增成功")
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message="数据库录入失败")

        return CrudRSModel(**result)

    @classmethod
    async def edit_bill(cls, result_db: Session, page_object: EditBillModel):
        """
        编辑单条账单记录
        """
        ## 账单编号不能为空
        if page_object.bill_id is None:
            return CrudRSModel(is_success=False, message="账单编号不能为空")

        ## 查询是否存在该条记录
        exist = BillDetDao.query_bill_by_id(result_db, bill_id=page_object.bill_id)
        if not exist:
            return CrudRSModel(is_success=False, message="账单记录不存在")

        ## 创建需要更新的信息
        exist.bill_date = pd.to_datetime(exist.bill_date).strftime("%Y-%m-%d")
        edit_data = query_to_dict(exist)
        for ky, vl in page_object.dict(exclude_unset=True).items():
            edit_data.update({ky: vl})

        ## 执行数据库操作
        try:
            BillDetDao.update_bill(result_db, BillModel(**edit_data))
            result_db.commit()
            result = dict(is_success=True, message="账单记录更新成功")
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message="数据库操作异常")

        return CrudRSModel(**result)

    @classmethod
    async def delete_bill(cls, result_db: Session, bill_id: str):
        """
        删除单条账单记录
        """
        ## 查询是否存在该条记录
        if not BillDetDao.query_bill_by_id(result_db, bill_id=bill_id):
            return CrudRSModel(is_success=False, message="账单记录不存在")

        ## 执行数据库操作
        try:
            BillDetDao.delete_bill(result_db, bill_id=bill_id)
            result_db.commit()
            result = dict(is_success=True, message="删除成功")
        except:
            logger.error(traceback.format_exc())
            result_db.rollback()
            result = dict(is_success=False, message="接口异常")
        return CrudRSModel(**result)

    @classmethod
    def get_bills(cls, result_db: Session, query_object: QueryBillModel):
        """
        根据筛选条件，查询多条账单记录
        """
        ## 数据库查询操作
        data = pd.DataFrame(
            [
                query_to_dict(f)
                for f in BillDetDao.query_bills_by_condition(result_db, query_object)
            ]
        )

        ## 如果未查询到账单记录
        if len(data) <= 0:
            return CrudDataRSModel(
                is_success=True, message="未查询到账单", data=data.to_dict("records")
            )

        ## 账单字典码值映射
        try:
            dict_map = cls.get_bill_dict(result_db, theme_id=query_object.theme_id)

            data = data.assign(
                bill_type=lambda df: df["bill_type"].map(dict_map.get("bill_type")),
                bill_name_code=lambda df: df["bill_name"].copy(),
                bill_name=lambda df: df["bill_name"].map(dict_map.get("bill_name")),
                pay_channel=lambda df: df["pay_channel"].map(
                    dict_map.get("pay_channel")
                ),
                settle_channel=lambda df: df["settle_channel"].map(
                    dict_map.get("settle_channel")
                ),
                consume_object=lambda df: df["consume_object"].map(
                    dict_map.get("consume_object")
                ),
                bill_scene=lambda df: df["bill_scene"].map(dict_map.get("bill_scene")),
                bill_status=lambda df: df["bill_status"].map(
                    dict_map.get("bill_status")
                ),
                remark=lambda df: df["remark"].fillna(""),
                bill_date=lambda df: pd.to_datetime(df["bill_date"]).dt.strftime(
                    "%Y-%m-%d"
                ),
            ).to_dict("records")
            result = dict(is_success=True, message="账单查询成功", data=data)

        except:
            logger.error(traceback.format_exc())
            result = dict(is_success=False, message="账单字典码值映射异常", data=[])

        return CrudDataRSModel(**result)


class BillAnalysisService(BillBaseService):
    """账单分析服务"""

    @classmethod
    def analyze_bills(
        cls,
        result_db: Session,
        query_object: QueryBillModel,
        analyze_object: AnalyzeBillModel,
    ):
        """
        根据筛选条件和分析条件，进行账单分析
        """
        ## 检验日期分析字段参数
        if analyze_object.is_contain_date_field:
            if analyze_object.date_field is None or analyze_object.date_dim is None:
                return CrudDataRSModel(
                    is_success=False, message="请指定日期字段和日期维度", data=[]
                )

            if analyze_object.date_dim not in ["Y", "M", "D"]:
                return CrudDataRSModel(
                    is_success=False,
                    message="日期维度参数错误，应从`Y`、`M`、`D`中选择",
                    data=[],
                )

            if isinstance(analyze_object.analyze_by, list):
                if analyze_object.date_field not in analyze_object.analyze_by:
                    return CrudDataRSModel(
                        is_success=False,
                        message="日期字段参数错误，应包含在分析字段中",
                        data=[],
                    )
            else:
                if analyze_object.date_field != analyze_object.analyze_by:
                    return CrudDataRSModel(
                        is_success=False,
                        message="日期字段参数错误，应包含在分析字段中",
                        data=[],
                    )

        ## 检验退款账单的分析参数
        if analyze_object.refund_method not in ["default", "ignore"]:
            return CrudDataRSModel(
                is_success=False,
                message="处理退款账单参数错误，应从`default`、`ignore`中选择",
                data=[],
            )

        ## 查询符合条件的账单
        try:
            bills = pd.DataFrame(
                [
                    query_to_dict(f)
                    for f in BillDetDao.query_bills_by_condition(
                        result_db, query_object
                    )
                ]
            )
        except:
            logger.error(traceback.format_exc())
            return CrudDataRSModel(is_success=False, message="数据库操作异常", data=[])

        ## 如果没有符合条件的账单
        if len(bills) <= 0:
            return CrudDataRSModel(
                is_success=False, message="没有符合条件的账单", data=[]
            )

        ## 检验日期字段
        if analyze_object.is_contain_date_field:
            if analyze_object.date_field not in bills.columns:
                return CrudDataRSModel(
                    is_success=False, message="错误的日期字段", data=[]
                )

        ## 计算新的日期分析字段
        if analyze_object.is_contain_date_field:
            fmt_dict = {"Y": "%Y", "M": "%Y-%m", "D": "%Y-%m-%d"}
            bills[analyze_object.date_field] = pd.to_datetime(
                bills[analyze_object.date_field]
            ).dt.strftime(fmt_dict[analyze_object.date_dim])

        ## 处理退款账单
        if analyze_object.refund_method == "default":
            bills.loc[bills["bill_status"] == "01", "bill_amount"] = -bills[
                bills["bill_status"] == "01"
            ]["bill_amount"]

        ## 进行统计分析
        group_obj = analyze_object.analyze_by
        dims = 1 if isinstance(group_obj, str) else len(group_obj)
        data = bills.groupby(by=group_obj, as_index=False).apply(
            lambda df: pd.Series(
                {
                    "amt": df["bill_amount"].sum(),
                    "cnt": df[df["bill_amount"] > 0]["bill_id"].count(),
                }
            )
        )

        ## 是否需要将码键转化成码值
        if not analyze_object.is_return_code:
            try:
                dict_map = cls.get_bill_dict(result_db, theme_id=query_object.theme_id)
                group_obj = (
                    [
                        group_obj,
                    ]
                    if dims <= 1
                    else group_obj
                )

                for k in group_obj:
                    if k in dict_map.keys():
                        data[k] = data[k].map(dict_map.get(k))
            except:
                logger.error(traceback.format_exc())
                return CrudDataRSModel(
                    is_success=False, message="账单字典码值映射异常", data=[]
                )

        ## 如果需要汇总则进行汇总
        if analyze_object.is_summary:
            data.loc[len(data), :] = [
                "合计",
            ] * dims + [data["amt"].sum(), data["cnt"].sum()]

        return CrudDataRSModel(
            is_success=True, message="账单分析成功", data=data.to_dict("records")
        )
