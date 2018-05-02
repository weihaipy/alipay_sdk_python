# ALIPAY API: alipay.pass.tpl.update request
#
# @author auto create
# @since 1.0, 2016-07-01 15:35:58
class AlipayPassTplUpdateRequest:
    # 模版内容
    tplContent = None
    # 模版ID
    tplId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setTplContent(self, tplContent):
        self.tplContent = tplContent
        self.apiParas["tpl_content"] = tplContent

    def getTplContent(self):
        return self.tplContent

    def setTplId(self, tplId):
        self.tplId = tplId
        self.apiParas["tpl_id"] = tplId

    def getTplId(self):
        return self.tplId

    def getApiMethodName(self):
        return "alipay.pass.tpl.update"

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
