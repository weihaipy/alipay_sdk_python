# ALIPAY API: alipay.promorulecenter.rule.analyze request
#
# @author auto create
# @since 1.0, 2017-10-09 17:38:20
class AlipayPromorulecenterRuleAnalyzeRequest:
    # 业务id
    bizId = None
    # 规则id
    ruleUuid = None
    # 支付宝用户id
    userId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBizId(self, bizId):
        self.bizId = bizId
        self.apiParas["biz_id"] = bizId

    def getBizId(self):
        return self.bizId

    def setRuleUuid(self, ruleUuid):
        self.ruleUuid = ruleUuid
        self.apiParas["rule_uuid"] = ruleUuid

    def getRuleUuid(self):
        return self.ruleUuid

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.promorulecenter.rule.analyze"

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
