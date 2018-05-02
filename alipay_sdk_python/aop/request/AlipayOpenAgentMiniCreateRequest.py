# ALIPAY API: alipay.open.agent.mini.create request
# 
# @author auto create
# @since 1.0, 2018-01-31 17:53:02
class AlipayOpenAgentMiniCreateRequest:
    # 小程序应用类目，参数格式：一级类目_二级类目。
    # 应用类目参考文档：https:  # docs.alipay.com/isv/10325
    appCategoryIds = None
    # 商户小程序描述信息，简要描述小程序主要功能（20-500个字），例：xx小程序提供了xx功能，主要解决了XX问题。
    appDesc = None
    # 小程序英文名称，长度3~20个字符
    appEnglishName = None
    # 商户小程序应用图标，最大256KB，LOGO不允许涉及政治敏感与色情；图片格式必须为：png、jpeg、jpg，建议上传像素为180#  180，LOGO核心图形建议在白色160PX范围内
    appLogo = None
    # 代商户创建的小程序应用名称。名称可以由中文、数字、英文及下划线组成，长度在3-20个字符之间，一个中文字等于2个字符，更多名称规则见：https:# docs.alipay.com/mini/operation/name
    appName = None
    # 代商户创建的小程序的简介，请用一句话简要描述小程序提供的服务；应用上架后一个自然月可修改5次（10~32个字符）
    appSlogan = None
    # ISV 代商户操作事务编号，通过事务开启接口alipay.open.agent.create调用返回。
    batchNo = None
    # 商户小程序客服邮箱
    # 商户小程序客服电话和邮箱，可以二选一填写，但不能同时为空
    serviceEmail = None
    # 商户小程序的客服电话，推荐填写
    # 商户小程序客服电话和邮箱，可以二选一填写，但不能同时为空
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

    def setBatchNo(self, batchNo):
        self.batchNo = batchNo
        self.apiParas["batch_no"] = batchNo

    def getBatchNo(self):
        return self.batchNo

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
        return "alipay.open.agent.mini.create"

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
