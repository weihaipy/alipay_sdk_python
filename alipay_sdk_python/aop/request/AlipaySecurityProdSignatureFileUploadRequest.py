# ALIPAY API: alipay.security.prod.signature.file.upload request
#
# @author auto create
# @since 1.0, 2017-12-20 15:24:53
class AlipaySecurityProdSignatureFileUploadRequest:
    # 业务唯一标识，由支付宝统一分配，无法自助获取
    bizProduct = None

    # 传入上传的文件流
    fileContent = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBizProduct(self, bizProduct):
        self.bizProduct = bizProduct
        self.apiParas["biz_product"] = bizProduct

    def getBizProduct(self):
        return self.bizProduct

    def setFileContent(self, fileContent):
        self.fileContent = fileContent
        self.apiParas["file_content"] = fileContent

    def getFileContent(self):
        return self.fileContent

    def getApiMethodName(self):
        return "alipay.security.prod.signature.file.upload"

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
