# ALIPAY API: alipay.offline.material.image.upload request
#
# @author auto create
# @since 1.0, 2018-01-10 20:15:08
class AlipayOfflineMaterialImageUploadRequest:
    # 图片/视频二进制内容，图片/视频大小不能超过5M
    imageContent = None
    # 图片/视频名称
    imageName = None
    # 用于显示指定图片/视频所属的partnerId（支付宝内部使用，外部商户无需填写此字段）
    imagePid = None
    # 图片/视频格式
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

    def setImageName(self, imageName):
        self.imageName = imageName
        self.apiParas["image_name"] = imageName

    def getImageName(self):
        return self.imageName

    def setImagePid(self, imagePid):
        self.imagePid = imagePid
        self.apiParas["image_pid"] = imagePid

    def getImagePid(self):
        return self.imagePid

    def setImageType(self, imageType):
        self.imageType = imageType
        self.apiParas["image_type"] = imageType

    def getImageType(self):
        return self.imageType

    def getApiMethodName(self):
        return "alipay.offline.material.image.upload"

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
