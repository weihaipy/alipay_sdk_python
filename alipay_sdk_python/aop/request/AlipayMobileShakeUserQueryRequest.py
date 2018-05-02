# ALIPAY API: alipay.mobile.shake.user.query request
#
# @author auto create
# @since 1.0, 2018-01-03 16:35:37
class AlipayMobileShakeUserQueryRequest:
    # 动态ID
    dynamicId = None
    # 动态ID类型：
    # wave_code：声波
    # qr_code：二维码
    # bar_code：条码
    dynamicIdType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False


    def setDynamicId(self, dynamicId):
        self.dynamicId = dynamicId
        self.apiParas["dynamic_id"] = dynamicId


    def getDynamicId(self):
        return self.dynamicId


    def setDynamicIdType(self, dynamicIdType):
        self.dynamicIdType = dynamicIdType
        self.apiParas["dynamic_id_type"] = dynamicIdType


    def getDynamicIdType(self):
        return self.dynamicIdType


    def getApiMethodName(self):
        return "alipay.mobile.shake.user.query"


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
