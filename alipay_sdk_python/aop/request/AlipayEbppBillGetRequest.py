# ALIPAY API: alipay.ebpp.bill.get request
#
# @author auto create
# @since 1.0, 2017-06-30 10:54:34
class AlipayEbppBillGetRequest:
    # 输出机构的业务流水号，需要保证唯一性。
    merchantOrderNo = None

    # 支付宝订单类型。公共事业缴纳JF,信用卡还款HK
    orderType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setMerchantOrderNo(self, merchantOrderNo):
        self.merchantOrderNo = merchantOrderNo
        self.apiParas["merchant_order_no"] = merchantOrderNo

    def getMerchantOrderNo(self):
        return self.merchantOrderNo

    def setOrderType(self, orderType):
        self.orderType = orderType
        self.apiParas["order_type"] = orderType

    def getOrderType(self):
        return self.orderType

    def getApiMethodName(self):
        return "alipay.ebpp.bill.get"

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
