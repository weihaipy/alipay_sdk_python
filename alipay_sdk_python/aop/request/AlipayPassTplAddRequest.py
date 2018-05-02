# ALIPAY API: alipay.pass.tpl.add request
#
# @author auto create
# @since 1.0, 2016-07-01 15:35:14
class AlipayPassTplAddRequest:
    # 支付宝pass模版内容【JSON格式】
    # 具体格式可参考https:  # alipass.alipay.com中文档中心-格式说明
    tplContent = None
    # 模版外部唯一标识：商户用于控制模版的唯一性。
    uniqueId = None
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

    def setUniqueId(self, uniqueId):
        self.uniqueId = uniqueId
        self.apiParas["unique_id"] = uniqueId

    def getUniqueId(self):
        return self.uniqueId

    def getApiMethodName(self):
        return "alipay.pass.tpl.add"

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
