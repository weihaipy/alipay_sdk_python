# ALIPAY API: alipay.mobile.public.info.modify request
#
# @author auto create
# @since 1.0, 2017-09-01 20:55:35
class AlipayMobilePublicInfoModifyRequest:
    # 服务窗名称，2-20个字之间；不得含有违反法律法规和公序良俗的相关信息；不得侵害他人名誉权、知识产权、商业秘密等合法权利；不得以太过广泛的、或产品、行业词组来命名，如：女装、皮革批发；不得以实名认证的媒体资质账号创建服务窗，或媒体相关名称命名服务窗，如：XX电视台、XX杂志等
    appName = None

    # 授权运营书，企业商户若为被经营方授权，需上传加盖公章的扫描件，请使用照片上传接口上传图片获得image_url
    authPic = None

    # 营业执照地址，建议尺寸 320 x 320px，支持.jpg .jpeg .png 格式，小于3M
    licenseUrl = None

    # 服务窗头像地址，建议尺寸 320 x 320px，支持.jpg .jpeg .png 格式，小于3M
    logoUrl = None

    # 服务窗欢迎语，200字以内，首次使用服务窗必须
    publicGreeting = None

    # 第一张门店照片地址，建议尺寸 320 x 320px，支持.jpg .jpeg .png 格式，小于3M
    shopPic1

    # 第二张门店照片地址
    shopPic2

    # 第三张门店照片地址
    shopPic3
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAppName(self, appName):
        self.appName = appName
        self.apiParas["app_name"] = appName

    def getAppName(self):
        return self.appName

    def setAuthPic(self, authPic):
        self.authPic = authPic
        self.apiParas["auth_pic"] = authPic

    def getAuthPic(self):
        return self.authPic

    def setLicenseUrl(self, licenseUrl):
        self.licenseUrl = licenseUrl
        self.apiParas["license_url"] = licenseUrl

    def getLicenseUrl(self):
        return self.licenseUrl

    def setLogoUrl(self, logoUrl):
        self.logoUrl = logoUrl
        self.apiParas["logo_url"] = logoUrl

    def getLogoUrl(self):
        return self.logoUrl

    def setPublicGreeting(self, publicGreeting):
        self.publicGreeting = publicGreeting
        self.apiParas["public_greeting"] = publicGreeting

    def getPublicGreeting(self):
        return self.publicGreeting

    def setShopPic1(shopPic1):
        self.shopPic1 = shopPic1
        self.apiParas["shop_pic1"] = shopPic1

    def getShopPic1(self):
        return self.shopPic1

    def setShopPic2(shopPic2):
        self.shopPic2 = shopPic2
        self.apiParas["shop_pic2"] = shopPic2

    def getShopPic2(self):
        return self.shopPic2

    def setShopPic3(shopPic3):
        self.shopPic3 = shopPic3
        self.apiParas["shop_pic3"] = shopPic3

    def getShopPic3(self):
        return self.shopPic3

    def getApiMethodName(self):
        return "alipay.mobile.public.info.modify"

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
