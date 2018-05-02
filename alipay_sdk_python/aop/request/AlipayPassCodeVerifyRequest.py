# ALIPAY API: alipay.pass.code.verify request
#
# @author auto create
# @since 1.0, 2014-06-12 17:16:11
class AlipayPassCodeVerifyRequest:
    # 商户核销操作扩展信息
    extInfo = None
    # 操作员id
    # 如果operator_type为1，则此id代表核销人员id
    # 如果operator_type为2，则此id代表核销机具id
    operatorId = None
    # 操作员类型
    # 1 核销人员
    # 2 核销机具
    operatorType = None
    # Alipass对应的核销码串
    verifyCode = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setExtInfo(self, extInfo):
        self.extInfo = extInfo
        self.apiParas["ext_info"] = extInfo

    def getExtInfo(self):
        return self.extInfo

    def setOperatorId(self, operatorId):
        self.operatorId = operatorId
        self.apiParas["operator_id"] = operatorId

    def getOperatorId(self):
        return self.operatorId

    def setOperatorType(self, operatorType):
        self.operatorType = operatorType
        self.apiParas["operator_type"] = operatorType

    def getOperatorType(self):
        return self.operatorType

    def setVerifyCode(self, verifyCode):
        self.verifyCode = verifyCode
        self.apiParas["verify_code"] = verifyCode

    def getVerifyCode(self):
        return self.verifyCode

    def getApiMethodName(self):
        return "alipay.pass.code.verify"

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
