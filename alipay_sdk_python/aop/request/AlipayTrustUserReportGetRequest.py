# ALIPAY API: alipay.trust.user.report.get request
#
# @author auto create
# @since 1.0, 2018-02-02 17:40:14
class AlipayTrustUserReportGetRequest:
    # 指定该接口在商户端的使用场景。具体枚举值在样例代码中给出
    scene = None
    # FN_S（金融简版）
    type = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setScene(self, scene):
        self.scene = scene
        self.apiParas["scene"] = scene

    def getScene(self):
        return self.scene

    def setType(self, type):
        self.type = type
        self.apiParas["type"] = type

    def getType(self):
        return self.type

    def getApiMethodName(self):
        return "alipay.trust.user.report.get"

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
