# ALIPAY API: alipay.mobile.bksigntoken.verify request
#
# @author auto create
# @since 1.0, 2017-04-07 18:08:15
class AlipayMobileBksigntokenVerifyRequest:
    # 设备标识
    deviceid = None
    # 调用来源
    source = None
    # 查询token
    token = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setDeviceid(self, deviceid):
        self.deviceid = deviceid
        self.apiParas["deviceid"] = deviceid

    def getDeviceid(self):
        return self.deviceid

    def setSource(self, source):
        self.source = source
        self.apiParas["source"] = source

    def getSource(self):
        return self.source

    def setToken(self, token):
        self.token = token
        self.apiParas["token"] = token

    def getToken(self):
        return self.token

    def getApiMethodName(self):
        return "alipay.mobile.bksigntoken.verify"

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
