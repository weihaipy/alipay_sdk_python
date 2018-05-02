# ALIPAY API: alipay.acquire.close request
#
# @author auto create
# @since 1.0, 2014-06-12 17:17:06
class AlipayAcquireCloseRequest:
    # 卖家的操作员ID
    operatorId = None
    # 支付宝合作商户网站唯一订单号
    outTradeNo = None
    # 该交易在支付宝系统中的交易流水号。
    #  #  最短16位，最长64位。
    #  如果同时传了out_trade_no和trade_no，则以trade_no为准
    tradeNo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setOperatorId(self, operatorId):
        self.operatorId = operatorId
        self.apiParas["operator_id"] = operatorId

    def getOperatorId(self):
        return self.operatorId

    def setOutTradeNo(self, outTradeNo):
        self.outTradeNo = outTradeNo
        self.apiParas["out_trade_no"] = outTradeNo

    def getOutTradeNo(self):
        return self.outTradeNo

    def setTradeNo(self, tradeNo):
        self.tradeNo = tradeNo
        self.apiParas["trade_no"] = tradeNo

    def getTradeNo(self):
        return self.tradeNo

    def getApiMethodName(self):
        return "alipay.acquire.close"

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
