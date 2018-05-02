# ALIPAY API: alipay.mobile.public.template.message.modify request
#
# @author auto create
# @since 1.0, 2017-04-14 20:26:03
class AlipayMobilePublicTemplateMessageModifyRequest:
    # 模板id
    templateId = None

    # 行业设置
    tradeSetting = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setTemplateId(self, templateId):
        self.templateId = templateId
        self.apiParas["template_id"] = templateId

    def getTemplateId(self):
        return self.templateId

    def setTradeSetting(self, tradeSetting):
        self.tradeSetting = tradeSetting
        self.apiParas["trade_setting"] = tradeSetting

    def getTradeSetting(self):
        return self.tradeSetting

    def getApiMethodName(self):
        return "alipay.mobile.public.template.message.modify"

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
