# ALIPAY API: alipay.offline.marketing.voucher.code.upload request
#
# @author auto create
# @since 1.0, 2018-01-12 10:57:49
class AlipayOfflineMarketingVoucherCodeUploadRequest:
    # 约定的扩展参数
    extendParams = None
    # 文件编码
    fileCharset = None
    # 文件二进制内容
    fileContent = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setExtendParams(self, extendParams):
        self.extendParams = extendParams
        self.apiParas["extend_params"] = extendParams

    def getExtendParams(self):
        return self.extendParams

    def setFileCharset(self, fileCharset):
        self.fileCharset = fileCharset
        self.apiParas["file_charset"] = fileCharset

    def getFileCharset(self):
        return self.fileCharset

    def setFileContent(self, fileContent):
        self.fileContent = fileContent
        self.apiParas["file_content"] = fileContent

    def getFileContent(self):
        return self.fileContent

    def getApiMethodName(self):
        return "alipay.offline.marketing.voucher.code.upload"

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
