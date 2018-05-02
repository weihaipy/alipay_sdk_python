# ALIPAY API: alipay.trust.user.auth.send request
#
# @author auto create
# @since 1.0, 2015-05-15 09:36:22
class AlipayTrustUserAuthSendRequest:
    # 申请授权的用户信息
    aliTrustUserInfo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAliTrustUserInfo(self, aliTrustUserInfo):
        self.aliTrustUserInfo = aliTrustUserInfo
        self.apiParas["ali_trust_user_info"] = aliTrustUserInfo

    def getAliTrustUserInfo(self):
        return self.aliTrustUserInfo

    def getApiMethodName(self):
        return "alipay.trust.user.auth.send"

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
