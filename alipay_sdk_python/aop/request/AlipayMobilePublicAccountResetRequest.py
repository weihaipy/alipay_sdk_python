# ALIPAY API: alipay.mobile.public.account.reset request
#
# @author auto create
# @since 1.0, 2016-12-19 20:52:24
class AlipayMobilePublicAccountResetRequest:
    # 协议号
    agreementId = None

    # 绑定账户
    bindAccountNo = None

    # json
    bizContent = None

    # 绑定账户的名
    displayName = None

    # 关注者标识
    fromUserId = None

    # 绑定账户的用户名
    realName = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAgreementId(self, agreementId):
        self.agreementId = agreementId
        self.apiParas["agreement_id"] = agreementId

    def getAgreementId(self):
        return self.agreementId

    def setBindAccountNo(self, bindAccountNo):
        self.bindAccountNo = bindAccountNo
        self.apiParas["bind_account_no"] = bindAccountNo

    def getBindAccountNo(self):
        return self.bindAccountNo

    def setBizContent(self, bizContent):
        self.bizContent = bizContent
        self.apiParas["biz_content"] = bizContent

    def getBizContent(self):
        return self.bizContent

    def setDisplayName(self, displayName):
        self.displayName = displayName
        self.apiParas["display_name"] = displayName

    def getDisplayName(self):
        return self.displayName

    def setFromUserId(self, fromUserId):
        self.fromUserId = fromUserId
        self.apiParas["from_user_id"] = fromUserId

    def getFromUserId(self):
        return self.fromUserId

    def setRealName(self, realName):
        self.realName = realName
        self.apiParas["real_name"] = realName

    def getRealName(self):
        return self.realName

    def getApiMethodName(self):
        return "alipay.mobile.public.account.reset"

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
