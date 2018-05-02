# ALIPAY API: alipay.open.mini.baseinfo.modify request
#
# @author auto create
# @since 1.0, 2018-01-25 00:19:21
class AlipayOpenMiniBaseinfoModifyRequest:
    # 11_1212_13。小程序类目，格式为 第一个一级类目_第一个二级类目第二个一级类目_第二个二级类目，详细类目可以参考https:# docs.alipay.com/isv/10325
    appCategoryIds = None
    # 小程序应用描述，20-200个字
    appDesc = None
    # 小程序应用英文名称
    appEnglishName = None
    # 小程序应用logo图标，图片格式必须为：png、jpeg、jpg，建议上传像素为180#  180
    appLogo = None
    # 小程序应用名称
    appName = None
    # 小程序应用简介，一句话描述小程序功能
    appSlogan = None
    # 小程序客服邮箱
    serviceEmail = None
    # 小程序客服电话
    servicePhone = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAppCategoryIds(self, appCategoryIds):
        self.appCategoryIds = appCategoryIds
        self.apiParas["app_category_ids"] = appCategoryIds

    def getAppCategoryIds(self):
        return self.appCategoryIds

    def setAppDesc(self, appDesc):
        self.appDesc = appDesc
        self.apiParas["app_desc"] = appDesc

    def getAppDesc(self):
        return self.appDesc

    def setAppEnglishName(self, appEnglishName):
        self.appEnglishName = appEnglishName
        self.apiParas["app_english_name"] = appEnglishName

    def getAppEnglishName(self):
        return self.appEnglishName

    def setAppLogo(self, appLogo):
        self.appLogo = appLogo
        self.apiParas["app_logo"] = appLogo

    def getAppLogo(self):
        return self.appLogo

    def setAppName(self, appName):
        self.appName = appName
        self.apiParas["app_name"] = appName

    def getAppName(self):
        return self.appName

    def setAppSlogan(self, appSlogan):
        self.appSlogan = appSlogan
        self.apiParas["app_slogan"] = appSlogan

    def getAppSlogan(self):
        return self.appSlogan

    def setServiceEmail(self, serviceEmail):
        self.serviceEmail = serviceEmail
        self.apiParas["service_email"] = serviceEmail

    def getServiceEmail(self):
        return self.serviceEmail

    def setServicePhone(self, servicePhone):
        self.servicePhone = servicePhone
        self.apiParas["service_phone"] = servicePhone

    def getServicePhone(self):
        return self.servicePhone

    def getApiMethodName(self):
        return "alipay.open.mini.baseinfo.modify"

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
