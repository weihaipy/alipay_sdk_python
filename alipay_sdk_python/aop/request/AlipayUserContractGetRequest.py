# ALIPAY API: alipay.user.contract.get request
#
# @author auto create
# @since 1.0, 2016-06-06 20:23:18
class AlipayUserContractGetRequest:
    # 订购者支付宝ID。session与subscriber_user_id二选一即可。
    subscriberUserId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setSubscriberUserId(self, subscriberUserId):
        self.subscriberUserId = subscriberUserId
        self.apiParas["subscriber_user_id"] = subscriberUserId

    def getSubscriberUserId(self):
        return self.subscriberUserId

    def getApiMethodName(self):
        return "alipay.user.contract.get"

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
