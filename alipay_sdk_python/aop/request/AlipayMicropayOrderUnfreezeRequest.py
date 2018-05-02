# ALIPAY API: alipay.micropay.order.unfreeze request
#
# @author auto create
# @since 1.0, 2016-06-06 17:54:23
class AlipayMicropayOrderUnfreezeRequest:
    # 冻结资金流水号,在创建资金订单时支付宝返回的流水号
    alipayOrderNo = None
    # 冻结备注
    memo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAlipayOrderNo(self, alipayOrderNo):
        self.alipayOrderNo = alipayOrderNo
        self.apiParas["alipay_order_no"] = alipayOrderNo

    def getAlipayOrderNo(self):
        return self.alipayOrderNo

    def setMemo(self, memo):
        self.memo = memo
        self.apiParas["memo"] = memo

    def getMemo(self):
        return self.memo

    def getApiMethodName(self):
        return "alipay.micropay.order.unfreeze"

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
