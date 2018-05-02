# ALIPAY API: alipay.ebpp.bill.search request
#
# @author auto create
# @since 1.0, 2017-04-07 17:13:40
class AlipayEbppBillSearchRequest:
    # 账单流水
    billKey = None
    # 出账机构
    chargeInst = None
    # 销账机构
    chargeoffInst = None
    # 销账机构给出账机构分配的id
    companyId = None
    # 必须以key value形式定义，转为json为格式："key1":"value1","key2":"value2","key3":"value3","key4":"value4"
    # 后端会直接转换为MAP对象，转换异常会报参数格式错误
    extend = None
    # 业务类型
    orderType = None
    # 子业务类型
    subOrderType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBillKey(self, billKey):
        self.billKey = billKey
        self.apiParas["bill_key"] = billKey

    def getBillKey(self):
        return self.billKey

    def setChargeInst(self, chargeInst):
        self.chargeInst = chargeInst
        self.apiParas["charge_inst"] = chargeInst

    def getChargeInst(self):
        return self.chargeInst

    def setChargeoffInst(self, chargeoffInst):
        self.chargeoffInst = chargeoffInst
        self.apiParas["chargeoff_inst"] = chargeoffInst

    def getChargeoffInst(self):
        return self.chargeoffInst

    def setCompanyId(self, companyId):
        self.companyId = companyId
        self.apiParas["company_id"] = companyId

    def getCompanyId(self):
        return self.companyId

    def setExtend(self, extend):
        self.extend = extend
        self.apiParas["extend"] = extend

    def getExtend(self):
        return self.extend

    def setOrderType(self, orderType):
        self.orderType = orderType
        self.apiParas["order_type"] = orderType

    def getOrderType(self):
        return self.orderType

    def setSubOrderType(self, subOrderType):
        self.subOrderType = subOrderType
        self.apiParas["sub_order_type"] = subOrderType

    def getSubOrderType(self):
        return self.subOrderType

    def getApiMethodName(self):
        return "alipay.ebpp.bill.search"

    def setNotifyUrl(self, notifyUrl):
        self.notifyUrl = notifyUrl

    def getNotifyUrl(self):
        return self.notifyUrl

    def setReturnUrl(self, returnUrl):
        self.returnUrl = returnUrl

    def getReturnUrl(self):
        return self.returnUrl

    def getApiParas(self):
        return self.apiParas

    def getTerminalType(self):
        return self.terminalType

    def setTerminalType(self, terminalType):
        self.terminalType = terminalType

    def getTerminalInfo(self):
        return self.terminalInfo

    def setTerminalInfo(self, terminalInfo):
        self.terminalInfo = terminalInfo

    def getProdCode(self):
        return self.prodCode

    def setProdCode(self, prodCode):
        self.prodCode = prodCode

    def setApiVersion(self, apiVersion):
        self.apiVersion = apiVersion

    def getApiVersion(self):
        return self.apiVersion

    def setNeedEncrypt(self, needEncrypt):
        self.needEncrypt = needEncrypt

    def getNeedEncrypt(self):
        return self.needEncrypt
