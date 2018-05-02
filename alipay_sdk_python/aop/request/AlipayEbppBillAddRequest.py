# ALIPAY API: alipay.ebpp.bill.add request
#
# @author auto create
# @since 1.0, 2018-01-22 21:21:47
class AlipayEbppBillAddRequest:
    # 外部订单号
    bankBillNo = None
    # 账单的账期，例如201203表示2012年3月的账单。
    billDate = None
    # 账单单据号，例如水费单号，手机号，电费号，信用卡卡号。没有唯一性要求。
    billKey = None
    # 支付宝给每个出账机构指定了一个对应的英文短名称来唯一表示该收费单位。
    chargeInst = None
    # 扩展属性
    extendField = None
    # 输出机构的业务流水号，需要保证唯一性
    merchantOrderNo = None
    # 用户的手机号
    mobile = None
    # 支付宝订单类型。公共事业缴纳JF,信用卡还款HK
    orderType = None
    # 拥有该账单的用户姓名
    ownerName = None
    # 缴费金额。用户支付的总金额。单位为：RMB Yuan。取值范围为[0.01，100000000.00]，精确到小数点后两位。
    payAmount = None
    # 账单的服务费。
    serviceAmount = None
    # 子业务类型是业务类型的下一级概念，例如：WATER表示JF下面的水费，ELECTRIC表示JF下面的电费，GAS表示JF下面的燃气费。
    subOrderType = None
    # 交通违章地点，sub_order_type=TRAFFIC时填写。
    trafficLocation = None
    # 违章行为，sub_order_type=TRAFFIC时填写。
    trafficRegulations = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBankBillNo(self, bankBillNo):
        self.bankBillNo = bankBillNo
        self.apiParas["bank_bill_no"] = bankBillNo

    def getBankBillNo(self):
        return self.bankBillNo

    def setBillDate(self, billDate):
        self.billDate = billDate
        self.apiParas["bill_date"] = billDate

    def getBillDate(self):
        return self.billDate

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

    def setExtendField(self, extendField):
        self.extendField = extendField
        self.apiParas["extend_field"] = extendField

    def getExtendField(self):
        return self.extendField

    def setMerchantOrderNo(self, merchantOrderNo):
        self.merchantOrderNo = merchantOrderNo
        self.apiParas["merchant_order_no"] = merchantOrderNo

    def getMerchantOrderNo(self):
        return self.merchantOrderNo

    def setMobile(self, mobile):
        self.mobile = mobile
        self.apiParas["mobile"] = mobile

    def getMobile(self):
        return self.mobile

    def setOrderType(self, orderType):
        self.orderType = orderType
        self.apiParas["order_type"] = orderType

    def getOrderType(self):
        return self.orderType

    def setOwnerName(self, ownerName):
        self.ownerName = ownerName
        self.apiParas["owner_name"] = ownerName

    def getOwnerName(self):
        return self.ownerName

    def setPayAmount(self, payAmount):
        self.payAmount = payAmount
        self.apiParas["pay_amount"] = payAmount

    def getPayAmount(self):
        return self.payAmount

    def setServiceAmount(self, serviceAmount):
        self.serviceAmount = serviceAmount
        self.apiParas["service_amount"] = serviceAmount

    def getServiceAmount(self):
        return self.serviceAmount

    def setSubOrderType(self, subOrderType):
        self.subOrderType = subOrderType
        self.apiParas["sub_order_type"] = subOrderType

    def getSubOrderType(self):
        return self.subOrderType

    def setTrafficLocation(self, trafficLocation):
        self.trafficLocation = trafficLocation
        self.apiParas["traffic_location"] = trafficLocation

    def getTrafficLocation(self):
        return self.trafficLocation

    def setTrafficRegulations(self, trafficRegulations):
        self.trafficRegulations = trafficRegulations
        self.apiParas["traffic_regulations"] = trafficRegulations

    def getTrafficRegulations(self):
        return self.trafficRegulations

    def getApiMethodName(self):
        return "alipay.ebpp.bill.add"

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
