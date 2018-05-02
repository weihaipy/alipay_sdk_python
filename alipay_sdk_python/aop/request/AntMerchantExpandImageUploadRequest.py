# ALIPAY API: ant.merchant.expand.image.upload request
#
# @author auto create
# @since 1.0, 2017-12-08 19:38:57
class AntMerchantExpandImageUploadRequest:
    # 图片二进制字节流
    imageContent = None
    # 图片格式
    imageType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setImageContent(self, imageContent):
        self.imageContent = imageContent
        self.apiParas["image_content"] = imageContent

    def getImageContent(self):
        return self.imageContent

    def setImageType(self, imageType):
        self.imageType = imageType
        self.apiParas["image_type"] = imageType

    def getImageType(self):
        return self.imageType

    def getApiMethodName(self):
        return "ant.merchant.expand.image.upload"

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
