# ALIPAY API: alipay.pass.sync.add request
#
# @author auto create
# @since 1.0, 2016-12-16 16:35:12
class AlipayPassSyncAddRequest:
    # alipass文件Base64编码后的内容。
    fileContent = None
    # 商户外部交易号，由商户生成并确保其唯一性
    outTradeNo = None
    # 商户与支付宝签约时，分配的唯一ID。
    partnerId = None
    # 支付宝用户ID，即买家用户ID
    userId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setFileContent(self, fileContent):
        self.fileContent = fileContent
        self.apiParas["file_content"] = fileContent

    def getFileContent(self):
        return self.fileContent

    def setOutTradeNo(self, outTradeNo):
        self.outTradeNo = outTradeNo
        self.apiParas["out_trade_no"] = outTradeNo

    def getOutTradeNo(self):
        return self.outTradeNo

    def setPartnerId(self, partnerId):
        self.partnerId = partnerId
        self.apiParas["partner_id"] = partnerId

    def getPartnerId(self):
        return self.partnerId

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.pass.sync.add"

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
