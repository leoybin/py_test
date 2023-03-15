一、请求参数说明：
1.formid：业务对象表单Id，字符串类型（必录）
2.data：JSON格式数据（详情参考JSON格式数据）（必录）
     2.1.NeedUpDateFields：需要更新的字段，数组类型，格式：[key1,key2,...] （非必录）注（更新单据体字段得加上单据体key）
     2.2.NeedReturnFields：需返回结果的字段集合，数组类型，格式：[key,entitykey.key,...]（非必录） 注（返回单据体字段格式：entitykey.key）
     2.3.IsDeleteEntry：是否删除已存在的分录，布尔类型，默认true（非必录）
     2.4.SubSystemId：表单所在的子系统内码，字符串类型（非必录）
     2.5.IsVerifyBaseDataField：是否验证所有的基础资料有效性，布尔类，默认false（非必录）
     2.6.IsEntryBatchFill：是否批量填充分录，默认true（非必录）
     2.7.ValidateFlag：是否验证标志，布尔类型，默认true（非必录）
     2.8.NumberSearch：是否用编码搜索基础资料，布尔类型，默认true（非必录）
     2.9.IsAutoAdjustField：是否自动调整JSON字段顺序，布尔类型，默认false（非必录）
     2.10.InterationFlags：交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."（非必录） 例如（允许负库存标识：STK_InvCheckResult）
     2.11.IgnoreInterationFlag：是否允许忽略交互，布尔类型，默认true（非必录）
     2.12.IsControlPrecision：是否控制精度，为true时对金额、单价和数量字段进行精度验证，默认false
     2.13.Model：表单数据包，JSON类型（必录）
备注:
1.示例Model数据包中字段顺序不建议改变，否则可能会有相互影响，如果出现字段值被覆盖或丢失，则可以尝试把字段顺序向后调整一下。
2.示例Model数据包默认包含允许引入的字段，实际按需构建既可。
3.如需创建关联关系，可参考http://club.kingdee.com/forum.php?mod=viewthread&tid=1394265 。

二、返回结果：
{"Result":{"ResponseStatus":{"ErrorCode":"","IsSuccess":"false","Errors":[{"FieldName":"","Message":"","DIndex":0}],"SuccessEntitys":[{"Id":"","Number":"","DIndex":0}],"SuccessMessages":[{"FieldName":"","Message":"","DIndex":0}],"MsgCode":""},"Id":"","Number":"","NeedReturnData":[{}]}}

三、代码示例：
// 使用webapi引用组件Kingdee.BOS.WebApi.Client.dll
K3CloudApiClient client = new K3CloudApiClient("http://cellprobio.gnway.cc/k3cloud/"); 
var loginResult = client.ValidateLogin("63310e555e38b1","Administrator","888888",2052);
var resultType = JObject.Parse(loginResult)["LoginResultType"].Value<int>();
//登录结果类型等于1，代表登录成功
if (resultType == 1)
{
	 client.Save("SAL_DELIVERYNOTICE","{"NeedUpDateFields":[],"NeedReturnFields":[],"IsDeleteEntry":"true","SubSystemId":"","IsVerifyBaseDataField":"false","IsEntryBatchFill":"true","ValidateFlag":"true","NumberSearch":"true","IsAutoAdjustField":"false","InterationFlags":"","IgnoreInterationFlag":"","IsControlPrecision":"false","Model":{"FID":0,"FBillTypeID":{"FNUMBER":""},"FBillNo":"","FDate":"1900-01-01","FSaleOrgId":{"FNumber":""},"FCustomerID":{"FNumber":""},"FSaleDeptID":{"FNumber":""},"FHeadDeliveryWay":{"FNumber":""},"FCorrespondOrgId":{"FNumber":""},"FCarrierID":{"FNumber":""},"FCarriageNO":"","FNote":"","FDeliveryOrgID":{"FNumber":""},"FDeliveryDeptID":{"FNumber":""},"FStockerGroupID":{"FNumber":""},"FStockerID":{"FNumber":""},"FSaleGroupID":{"FNumber":""},"FSalesManID":{"FNumber":""},"FReceiverID":{"FNumber":""},"FHeadLocId":{"FNumber":""},"FReceiverContactID":{"FNAME":""},"FReceiveAddress":"","FSettleID":{"FNumber":""},"FPayerID":{"FNumber":""},"FRECEIPTCONDITIONID":{"FNumber":""},"FOwnerTypeIdHead":"","FOwnerIdHead":{"FNumber":""},"FPlanRecAddress":"","FLinkMan":"","FLinkPhone":"","F_SZSP_XSLX":{"FNumber":""},"FCloseReason":"","F_SZSP_SHDZWB1":"","F_SZSP_LXRWB":"","F_SZSP_LXDHWB":"","FScanBox":"","F_SZSP_Remarks":"","SubHeadEntity":{"FEntryId":0,"FSettleOrgID":{"FNumber":""},"FSettleCurrID":{"FNumber":""},"FSettleTypeID":{"FNumber":""},"FLocalCurrID":{"FNumber":""},"FExchangeTypeID":{"FNumber":""},"FExchangeRate":0,"FCreChkDays":0,"FCreChkOverAmount":0,"FCreChkAmount":0,"FOverOrgTransDirect":"false","FAllDisCount":0},"FEntity":[{"FEntryID":0,"FRowType":"","FCustMatID":{"FNumber":""},"FMaterialID":{"FNumber":""},"FAuxpropID":{},"FParentMatId":{"FNUMBER":""},"FUnitID":{"FNumber":""},"FCurrentInventory":0,"FAwaitQty":0,"FQty":0,"FAvailableQty":0,"FDeliveryDate":"1900-01-01","FStockID":{"FNumber":""},"FStockLocID":{"FSTOCKLOCID__FF100001":{"FNumber":""},"FSTOCKLOCID__FF100002":{"FNumber":""},"FSTOCKLOCID__FF100004":{"FNumber":""},"FSTOCKLOCID__FF100005":{"FNumber":""},"FSTOCKLOCID__FF100006":{"FNumber":""},"FSTOCKLOCID__FF100007":{"FNumber":""},"FSTOCKLOCID__FF100008":{"FNumber":""}},"FBACKUPSTOCKID":{"FNumber":""},"FBACKUPSTOCKLOCID":{"FBACKUPSTOCKLOCID__FF100001":{"FNumber":""},"FBACKUPSTOCKLOCID__FF100002":{"FNumber":""},"FBACKUPSTOCKLOCID__FF100004":{"FNumber":""},"FBACKUPSTOCKLOCID__FF100005":{"FNumber":""},"FBACKUPSTOCKLOCID__FF100006":{"FNumber":""},"FBACKUPSTOCKLOCID__FF100007":{"FNumber":""},"FBACKUPSTOCKLOCID__FF100008":{"FNumber":""}},"FMtoNo":"","FNoteEntry":"","FBomID":{"FNumber":""},"FLot":{"FNumber":""},"FPRODUCEDATE":"1900-01-01","FEXPIRYDATE":"1900-01-01","FStockStatusId":{"FNumber":""},"FOutContROL":"false","FOutMaxQty":0,"FOutMinQty":0,"FPriceDiscount":0,"FBaseUnitID":{"FNumber":""},"FPriceBaseQty":0,"FPlanDeliveryDate":"1900-01-01","FDeliveryLoc":{"FNumber":""},"FDeliveryLAddress":"","FCarryLeadTime":0,"FJoinCheckQty":0,"FBaseJoinCheckQty":0,"FQualifiedQty":0,"FBaseQualifiedQty":0,"FUnqualifiedQty":0,"FBaseUnqualifiedQty":0,"FJunkedQty":0,"FBaseJunkedQty":0,"FStockUnitID":{"FNumber":""},"FStockQty":0,"FStockBaseQty":0,"FOwnerTypeID":"","FOwnerID":{"FNumber":""},"FBaseJoinQualifiedQty":0,"FJoinQualifiedQty":0,"FBaseJoinUnqualifiedQty":0,"FJoinUnqualifiedQty":0,"FBaseUQCanSaleQty":0,"FUQCanSaleQty":0,"FJoinDeliChkQty":0,"FBaseJoinDeliChkQty":0,"FJoinDeliChkUQQty":0,"FBaseJoinDeliChkUQQty":0,"FDeliChkTranOutQty":0,"FDeliChkTranOutUQQty":0,"FBaseDeliChkTranOutQty":0,"FSOEntryId":0,"FBaseDeliChkTranOutUQQty":0,"FOutLmtUnit":"","FOutLmtUnitID":{"FNumber":""},"FAllAmountExceptDisCount":0,"FCheckDelivery":"false","FBOMEntryId":0,"FAutoDEMidId":"","FLockStockFlag":"false","FLockStockBaseQty":0,"FLockStockLeftBaseQty":0,"FTaxDetailSubEntity":[{"FDetailID":0}],"FSerialSubEntity":[{"FDetailID":0,"FSerialNo":"","FSerialNote":""}]}],"FDeliNoticeTrace":[{"FEntryID":0,"FLogComId":{"FCODE":""},"FCarryBillNo":"","FPhoneNumber":"","FFrom":"","FTo":"","FDelTime":"1900-01-01","FTraceStatus":"","FReceiptTime":"1900-01-01","FDeliNoticeTraceDetail":[{"FDetailID":0,"FTraceTime":"","FTraceDetail":""}]}]}}");
 }

四、JSON格式数据：
{
    "NeedUpDateFields": [],
    "NeedReturnFields": [],
    "IsDeleteEntry": "true",
    "SubSystemId": "",
    "IsVerifyBaseDataField": "false",
    "IsEntryBatchFill": "true",
    "ValidateFlag": "true",
    "NumberSearch": "true",
    "IsAutoAdjustField": "false",
    "InterationFlags": "",
    "IgnoreInterationFlag": "",
    "IsControlPrecision": "false",
    "Model": {
        "FID": 0,
        "FBillTypeID": {
            "FNUMBER": ""
        },
        "FBillNo": "",
        "FDate": "1900-01-01",
        "FSaleOrgId": {
            "FNumber": ""
        },
        "FCustomerID": {
            "FNumber": ""
        },
        "FSaleDeptID": {
            "FNumber": ""
        },
        "FHeadDeliveryWay": {
            "FNumber": ""
        },
        "FCorrespondOrgId": {
            "FNumber": ""
        },
        "FCarrierID": {
            "FNumber": ""
        },
        "FCarriageNO": "",
        "FNote": "",
        "FDeliveryOrgID": {
            "FNumber": ""
        },
        "FDeliveryDeptID": {
            "FNumber": ""
        },
        "FStockerGroupID": {
            "FNumber": ""
        },
        "FStockerID": {
            "FNumber": ""
        },
        "FSaleGroupID": {
            "FNumber": ""
        },
        "FSalesManID": {
            "FNumber": ""
        },
        "FReceiverID": {
            "FNumber": ""
        },
        "FHeadLocId": {
            "FNumber": ""
        },
        "FReceiverContactID": {
            "FNAME": ""
        },
        "FReceiveAddress": "",
        "FSettleID": {
            "FNumber": ""
        },
        "FPayerID": {
            "FNumber": ""
        },
        "FRECEIPTCONDITIONID": {
            "FNumber": ""
        },
        "FOwnerTypeIdHead": "",
        "FOwnerIdHead": {
            "FNumber": ""
        },
        "FPlanRecAddress": "",
        "FLinkMan": "",
        "FLinkPhone": "",
        "F_SZSP_XSLX": {
            "FNumber": ""
        },
        "FCloseReason": "",
        "F_SZSP_SHDZWB1": "",
        "F_SZSP_LXRWB": "",
        "F_SZSP_LXDHWB": "",
        "FScanBox": "",
        "F_SZSP_Remarks": "",
        "SubHeadEntity": {
            "FEntryId": 0,
            "FSettleOrgID": {
                "FNumber": ""
            },
            "FSettleCurrID": {
                "FNumber": ""
            },
            "FSettleTypeID": {
                "FNumber": ""
            },
            "FLocalCurrID": {
                "FNumber": ""
            },
            "FExchangeTypeID": {
                "FNumber": ""
            },
            "FExchangeRate": 0,
            "FCreChkDays": 0,
            "FCreChkOverAmount": 0,
            "FCreChkAmount": 0,
            "FOverOrgTransDirect": "false",
            "FAllDisCount": 0
        },
        "FEntity": [
            {
                "FEntryID": 0,
                "FRowType": "",
                "FCustMatID": {
                    "FNumber": ""
                },
                "FMaterialID": {
                    "FNumber": ""
                },
                "FAuxpropID": {},
                "FParentMatId": {
                    "FNUMBER": ""
                },
                "FUnitID": {
                    "FNumber": ""
                },
                "FCurrentInventory": 0,
                "FAwaitQty": 0,
                "FQty": 0,
                "FAvailableQty": 0,
                "FDeliveryDate": "1900-01-01",
                "FStockID": {
                    "FNumber": ""
                },
                "FStockLocID": {
                    "FSTOCKLOCID__FF100001": {
                        "FNumber": ""
                    },
                    "FSTOCKLOCID__FF100002": {
                        "FNumber": ""
                    },
                    "FSTOCKLOCID__FF100004": {
                        "FNumber": ""
                    },
                    "FSTOCKLOCID__FF100005": {
                        "FNumber": ""
                    },
                    "FSTOCKLOCID__FF100006": {
                        "FNumber": ""
                    },
                    "aa":"aaa",
                    "FSTOCKLOCID__FF100007": {
                        "FNumber": ""
                    },
                    "FSTOCKLOCID__FF100008": {
                        "FNumber": ""
                    }
                },
                "FBACKUPSTOCKID": {
                    "FNumber": ""
                },
                "FBACKUPSTOCKLOCID": {
                    "FBACKUPSTOCKLOCID__FF100001": {
                        "FNumber": ""
                    },
                    "FBACKUPSTOCKLOCID__FF100002": {
                        "FNumber": ""
                    },
                    "FBACKUPSTOCKLOCID__FF100004": {
                        "FNumber": ""
                    },
                    "FBACKUPSTOCKLOCID__FF100005": {
                        "FNumber": ""
                    },
                    "FBACKUPSTOCKLOCID__FF100006": {
                        "FNumber": ""
                    },
                    "FBACKUPSTOCKLOCID__FF100007": {
                        "FNumber": ""
                    },
                    "FBACKUPSTOCKLOCID__FF100008": {
                        "FNumber": ""
                    }
                },
                "FMtoNo": "",
                "FNoteEntry": "",
                "FBomID": {
                    "FNumber": ""
                },
                "FLot": {
                    "FNumber": ""
                },
                "FPRODUCEDATE": "1900-01-01",
                "FEXPIRYDATE": "1900-01-01",
                "FStockStatusId": {
                    "FNumber": ""
                },
                "FOutContROL": "false",
                "FOutMaxQty": 0,
                "FOutMinQty": 0,
                "FPriceDiscount": 0,
                "FBaseUnitID": {
                    "FNumber": ""
                },
                "FPriceBaseQty": 0,
                "FPlanDeliveryDate": "1900-01-01",
                "FDeliveryLoc": {
                    "FNumber": ""
                },
                "FDeliveryLAddress": "",
                "FCarryLeadTime": 0,
                "FJoinCheckQty": 0,
                "FBaseJoinCheckQty": 0,
                "FQualifiedQty": 0,
                "FBaseQualifiedQty": 0,
                "FUnqualifiedQty": 0,
                "FBaseUnqualifiedQty": 0,
                "FJunkedQty": 0,
                "FBaseJunkedQty": 0,
                "FStockUnitID": {
                    "FNumber": ""
                },
                "FStockQty": 0,
                "FStockBaseQty": 0,
                "FOwnerTypeID": "",
                "FOwnerID": {
                    "FNumber": ""
                },
                "FBaseJoinQualifiedQty": 0,
                "FJoinQualifiedQty": 0,
                "FBaseJoinUnqualifiedQty": 0,
                "FJoinUnqualifiedQty": 0,
                "FBaseUQCanSaleQty": 0,
                "FUQCanSaleQty": 0,
                "FJoinDeliChkQty": 0,
                "FBaseJoinDeliChkQty": 0,
                "FJoinDeliChkUQQty": 0,
                "FBaseJoinDeliChkUQQty": 0,
                "FDeliChkTranOutQty": 0,
                "FDeliChkTranOutUQQty": 0,
                "FBaseDeliChkTranOutQty": 0,
                "FSOEntryId": 0,
                "FBaseDeliChkTranOutUQQty": 0,
                "FOutLmtUnit": "",
                "FOutLmtUnitID": {
                    "FNumber": ""
                },
                "FAllAmountExceptDisCount": 0,
                "FCheckDelivery": "false",
                "FBOMEntryId": 0,
                "FAutoDEMidId": "",
                "FLockStockFlag": "false",
                "FLockStockBaseQty": 0,
                "FLockStockLeftBaseQty": 0,
                "FTaxDetailSubEntity": [
                    {
                        "FDetailID": 0
                    }
                ],
                "FSerialSubEntity": [
                    {
                        "FDetailID": 0,
                        "FSerialNo": "",
                        "FSerialNote": ""
                    }
                ]
            }
        ],
        "FDeliNoticeTrace": [
            {
                "FEntryID": 0,
                "FLogComId": {
                    "FCODE": ""
                },
                "FCarryBillNo": "",
                "FPhoneNumber": "",
                "FFrom": "",
                "FTo": "",
                "FDelTime": "1900-01-01",
                "FTraceStatus": "",
                "FReceiptTime": "1900-01-01",
                "FDeliNoticeTraceDetail": [
                    {
                        "FDetailID": 0,
                        "FTraceTime": "",
                        "FTraceDetail": ""
                    }
                ]
            }
        ]
    }
}

五、字段说明：
基本信息：FBillHead 
	 实体主键：FID 
	 单据编号：FBillNo 
	 单据状态：FDocumentStatus 
	 销售组织：FSaleOrgId  (必填项)
	 日期：FDate  (必填项)
	 客户：FCustomerID  (必填项)
	 发货组织：FDeliveryOrgID  (必填项)
	 发货部门：FDeliveryDeptID 
	 库存组：FStockerGroupID 
	 仓管员：FStockerID 
	 销售部门：FSaleDeptID 
	 销售组：FSaleGroupID 
	 销售员：FSalesManID 
	 承运商：FCarrierID 
	 运输单号：FCarriageNO 
	 收货方：FReceiverID 
	 结算方：FSettleID 
	 付款方：FPayerID 
	 创建人：FCreatorId 
	 创建日期：FCreateDate 
	 最后修改日期：FModifyDate 
	 审核日期：FApproveDate 
	 作废日期：FCancelDate 
	 最后修改人：FModifierId 
	 单据类型：FBillTypeID  (必填项)
	 审核人：FApproverID 
	 作废人：FCancellerID 
	 作废状态：FCancelStatus 
	 货主类型：FOwnerTypeIdHead 
	 货主：FOwnerIdHead 
	 关闭状态：FCLOSESTATUS 
	 关闭人：FCLOSERID 
	 关闭日期：FCLOSEDATE 
	 收款条件：FRECEIPTCONDITIONID 
	 交货方式：FHeadDeliveryWay 
	 出库即关闭：FIsSysClose 
	 业务类型：FBussinessType 
	 收货方地址：FReceiveAddress 
	 交货地点：FHeadLocId 
	 信用检查结果：FCreditCheckResult 
	 对应组织：FCorrespondOrgId 
	 收货方联系人：FReceiverContactID 
	 发货备注：FNote 
	 交货明细执行地址(后台用)：FPlanRecAddress 
	 手工关闭：FIsManualClose 
	 收货人姓名：FLinkMan 
	 联系电话：FLinkPhone 
	 关闭原因：FCloseReason 
	 序列号上传：FScanBox 
	 销售类型：F_SZSP_XSLX 
	 送货地址：F_SZSP_SHDZ 
	 送货联系人：F_SZSP_LXR 
	 送货地址(外贸)：F_SZSP_SHDZWB1 
	 送货联系人(外贸)：F_SZSP_LXRWB 
	 联系电话(外贸)：F_SZSP_LXDHWB 
	 联系电话：F_SZSP_LXDH 
	 特殊开票说明：F_SZSP_Remarks 
明细信息：FEntity 
	 实体主键：FEntryID 
	 物料编码：FMaterialID  (必填项)
	 物料名称：FMaterialName 
	 规格型号：FMateriaModel 
	 物料类别：FMateriaType 
	 销售单位：FUnitID  (必填项)
	 销售数量：FQty 
	 出货仓库：FStockID 
	 备注：FNoteEntry 
	 BOM版本 ：FBomID 
	 基本单位：FBaseUnitID  (必填项)
	 销售基本数量：FBaseUnitQty 
	 交货地点：FDeliveryLoc 
	 交货地址：FDeliveryLAddress 
	 控制出库数量：FOutContROL 
	 出库上限：FOutMaxQty 
	 出库下限：FOutMinQty 
	 运输提前期：FCarryLeadTime 
	 关联出库数量：FJoinOutQty 
	 累计出库数量：FSumOutQty 
	 辅助属性：FAuxpropID 
	 订单单号：FOrderNo 
	 订单行号：FOrderSeq 
	 源单类型：FSrcType 
	 客户物料编码：FCustMatID 
	 出货仓位：FStockLocID 
	 WIP仓位集：FF100001
	 产成品仓位集：FF100002
	 原料仓位集：FF100004
	 客供仓位集：FF100005
	 废料仓位集：FF100006
	 办公列管仓位集：FF100007
	 外购仓位集：FF100008
	 备货仓位：FBACKUPSTOCKLOCID 
	 WIP仓位集：FF100001
	 产成品仓位集：FF100002
	 原料仓位集：FF100004
	 客供仓位集：FF100005
	 废料仓位集：FF100006
	 办公列管仓位集：FF100007
	 外购仓位集：FF100008
	 备货仓库：FBACKUPSTOCKID 
	 关联调拨数量（销售基本）：FBASETRANSFERQTY 
	 关联调拨数量：FTRANSFERQTY 
	 关联出库数量（销售基本）：FBASEJOINOUTQTY 
	 累计出库数量(销售基本)：FBASESUMOUTQTY 
	 生产日期：FPRODUCEDATE 
	 保质期：FEXPPERIOD 
	 有效期至：FEXPIRYDATE 
	 保质期单位：FEXPUNIT 
	 批号：FLot 
	 是否赠品：FIsFree 
	 行关闭状态：FCLOSESTATUS_MX 
	 客户物料名称：FCustMatName 
	 未出库数量：FRemainOutQty 
	 库存状态：FStockStatusId 
	 计价单位：FPriceUnitId 
	 计价数量：FPriceUnitQty 
	 单价：FPrice 
	 含税单价：FTaxPrice 
	 税组合：FTaxCombination 
	 税率%：FEntryTaxRate 
	 价格系数：FPriceCoefficient 
	 系统定价：FSysPrice 
	 最低限价：FLimitDownPrice 
	 折前金额：FBefDisAmt 
	 折前价税合计：FBefDisAllAmt 
	 折扣率%：FDiscountRate 
	 金额：FAmount 
	 金额（本位币）：FAmount_LC 
	 税额：FEntryTaxAmount 
	 税额（本位币）：FTaxAmount_LC 
	 价税合计：FAllAmount 
	 折扣额：FDiscount 
	 价税合计（本位币）：FAllAmount_LC 
	 净价：FTaxNetPrice 
	 要货日期：FDeliveryDate 
	 计划发货日期：FPlanDeliveryDate 
	 出库上限数量（基本单位）：FBaseOutMaxQty 
	 出库下限数量（基本单位）：FBaseOutMinQty 
	 当前库存：FInventoryQty 
	 业务流程：FBFLowId 
	 源单编号：FSrcBillNo 
	 计划跟踪号：FMtoNo 
	 待发数量：FAwaitQty 
	 可发库存：FAvailableQty 
	 终止状态：FTerminationStatus 
	 终止人：FTerminaterId 
	 业务终止日期：FTerminateDate 
	 计价基本数量：FPriceBaseQty 
	 请检关联数量：FJoinCheckQty 
	 请检关联数量(基本单位)：FBaseJoinCheckQty 
	 合格数量：FQualifiedQty 
	 合格数量(基本单位)：FBaseQualifiedQty 
	 不合格数量：FUnqualifiedQty 
	 不合格数量(基本单位)：FBaseUnqualifiedQty 
	 报废数量：FJunkedQty 
	 报废数量(基本单位)：FBaseJunkedQty 
	 库存数量：FStockQty 
	 库存单位：FStockUnitID 
	 库存基本数量：FStockBaseQty 
	 关联出库数量（库存基本）：FStockBaseJoinOutQty 
	 累计出库数量（库存基本）：FStockBaseSumOutQty 
	 销售基本分子：FSalBaseNum 
	 库存基本分母：FStockBaseDen 
	 携带的主业务单位：FSRCBIZUNITID 
	 服务上下文：FServiceContext 
	 关联调拨数量（库存基本）：FStockBaseTransQty 
	 货主类型：FOwnerTypeID 
	 货主：FOwnerID 
	 出库关联合格数量(基本单位)：FBaseJoinQualifiedQty 
	 出库关联合格数量：FJoinQualifiedQty 
	 出库关联不合格数量(基本单位)：FBaseJoinUnqualifiedQty 
	 出库关联不合格数量：FJoinUnqualifiedQty 
	 不合格可销售数量(基本单位)：FBaseUQCanSaleQty 
	 不合格可销售数量：FUQCanSaleQty 
	 关联合格调拨数量：FJoinDeliChkQty 
	 关联合格调拨数量(基本单位)：FBaseJoinDeliChkQty 
	 关联不合格调拨数量：FJoinDeliChkUQQty 
	 关联不合格调拨数量(基本单位)：FBaseJoinDeliChkUQQty 
	 发货检验合格调拨出库：FDeliChkTranOutQty 
	 发货检验不合格调拨出库：FDeliChkTranOutUQQty 
	 发货检验合格调拨出库(基本)：FBaseDeliChkTranOutQty 
	 发货检验不合格调拨出库(基本)：FBaseDeliChkTranOutUQQty 
	 超发控制单位类型：FOutLmtUnit  (必填项)
	 超发控制单位：FOutLmtUnitID 
	 销售订单EntryId：FSOEntryId 
	 累计调拨退货数量：FTRANSRETURNQTY 
	 累计调拨退货数量（销售基本）：FTRANSRETURNBASEQTY 
	 寄售结算数量：FCONSIGNSETTQTY 
	 寄售结算数量（销售基本）：FCONSIGNSETTBASEQTY 
	 锁库拆分分录ID：FSplitLockEntryId 
	 可用库存：FCurrentInventory 
	 产品类型：FRowType 
	 父项产品：FParentMatId 
	 行标识：FRowId 
	 父行标识：FParentRowId 
	 变更数量（库存）：FSTOCKCHANGEQTY 
	 变更数量（库存基本）：FSTOCKCHANGEBASEQTY 
	 发货检验：FCheckDelivery 
	 单价折扣：FPriceDiscount 
	 尾差处理标识：FTailDiffFlag 
	 BOM分录内码：FBOMEntryId 
	 自动发货中间结果来源ID：FAutoDEMidId 
	 价税合计（折前）：FAllAmountExceptDisCount 
	 行价目表：FPriceListEntry 
	 锁库标识：FLockStockFlag 
	 锁库基本数量：FLockStockBaseQty 
	 待锁库基本数量：FLockStockLeftBaseQty 
	 序列号单位：FSNUnitID 
	 序列号数量：FSNQty 
	 旧物料编码：F_SZSP_OldItemNumber 
财务信息：SubHeadEntity 
	 实体主键：FEntryId 
	 结算组织：FSettleOrgID  (必填项)
	 本位币：FLocalCurrID 
	 汇率类型：FExchangeTypeID 
	 汇率：FExchangeRate 
	 结算方式：FSettleTypeID 
	 结算币别：FSettleCurrID  (必填项)
	 价目表：FPriceListId 
	 折扣表：FDiscountListId 
	 税额：FBillTaxAmount 
	 金额：FBillAmount 
	 价税合计：FBillAllAmount 
	 是否含税：FIsIncludedTax 
	 价税合计（本位币）：FBillAllAmount_LC 
	 金额（本位币）：FBillAmount_LC 
	 税额（本位币）：FBillTaxAmount_LC 
	 工作流信用超标天数：FCreChkDays 
	 工作流信用检查状态：FCreChkStatus 
	 工作流信用超标金额：FCreChkAmount 
	 审批流信用压批月结检查：FCrePreBatAndMonStatus 
	 信用压批超标：FCrePreBatchOver 
	 信用月结超标：FCreMonControlOver 
	 价外税：FIsPriceExcludeTax 
	 工作流信用逾期超标额度：FCreChkOverAmount 
	 寄售生成跨组织调拨：FOverOrgTransDirect 
	 整单折扣额：FAllDisCount 
税务明细：FTaxDetailSubEntity 
	 实体主键：FDetailID 
	 税率名称：FTaxRateId 
	 税率%：FTaxRate 
	 税额：FTaxAmount 
	 计入成本比例%：FCostPercent 
	 计入成本金额：FCostAmount 
	 增值税：FVAT 
	 卖方代扣代缴：FSellerWithholding 
	 买方代扣代缴：FBuyerWithholding 
物流跟踪明细：FDeliNoticeTrace 
	 实体主键：FEntryID 
	 物流公司：FLogComId 
	 物流单号：FCarryBillNo  (必填项)
	 物流状态：FTraceStatus 
	 发货时间：FDelTime 
	 寄件人手机号码：FPhoneNumber 
	 起始地点：FFrom 
	 终止地点：FTo 
	 签收时间：FReceiptTime 
物流详细信息：FDeliNoticeTraceDetail 
	 实体主键：FDetailID 
	 时间：FTraceTime 
	 物流详情：FTraceDetail 
序列号子单据体：FSerialSubEntity 
	 实体主键：FDetailID 
	 序列号：FSerialNo 
	 序列号：FSerialId 
	 备注：FSerialNote 
关联关系表：FEntity_Link 
	 实体主键：FLinkId 
	 业务流程图：FEntity_Link_FFlowId 
	 推进路线：FEntity_Link_FFlowLineId 
	 转换规则：FEntity_Link_FRuleId 
	 源单表内码：FEntity_Link_FSTableId 
	 源单表：FEntity_Link_FSTableName 
	 源单内码：FEntity_Link_FSBillId 
	 源单分录内码：FEntity_Link_FSId 
	 原始携带量：FEntity_Link_FBaseUnitQtyOld 
	 修改携带量：FEntity_Link_FBaseUnitQty 
	 原始携带量：FEntity_Link_FStockBaseQtyOld 
	 修改携带量：FEntity_Link_FStockBaseQty 

备注：错误代码MsgCode说明
           0：默认
           1：上下文丢失
           2：没有权限
           3：操作标识为空
           4：异常
           5：单据标识为空
           6：数据库操作失败
           7：许可错误
           8：参数错误
           9：指定字段/值不存在
           10：未找到对应数据
           11：验证失败
           12：不可操作
           13：网控冲突