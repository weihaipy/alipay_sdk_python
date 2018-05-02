# ALIPAY API: alipay.open.mini.version.audit.apply request
#
# @author auto create
# @since 1.0, 2018-01-25 00:27:43
class AlipayOpenMiniVersionAuditApplyRequest:
    # 小程序类目，格式为 第一个一级类目_第一个二级类目第二个一级类目_第二个二级类目，详细类目可以参考https:# docs.alipay.com/isv/10325
    appCategoryIds = None
    # 小程序应用描述，20-200个字
    appDesc = None
    # 小程序应用英文名称
    appEnglishName = None
    # 小程序logo图标，图片格式必须为：png、jpeg、jpg，建议上传像素为180#  180
    appLogo = None
    # 小程序应用名称
    appName = None
    # 小程序应用简介，一句话描述小程序功能
    appSlogan = None
    # 小程序版本号
    appVersion = None
    # 小程序第四张应用截图，不能超过4MB，图片格式只支持jpg，png
    fifthScreenShot = None
    # 实例化的小程序可以不用传第一张应用截图，小程序第一张应用截图，不能超过4MB，图片格式只支持jpg，png
    firstScreenShot = None
    # 小程序第四张应用截图，不能超过4MB，图片格式只支持jpg，png
    fourthScreenShot = None
    # 小程序备注
    memo = None
    # 小程序服务区域类型，GLOBLE-全球，CHINA-中国，LOCATION-指定区域
    regionType = None
    # 实例化的小程序可以不用传第二张应用截图，小程序第二张应用截图，不能超过4MB，图片格式只支持jpg，png
    secondScreenShot = None
    # 小程序客服邮箱
    serviceEmail = None
    # 小程序客服电话
    servicePhone = None
    # 省市区信息，当区域类型为LOCATION时，不能为空，province_code不能为空，当填写city_code时，province_code不能为空，当填写area_code时，province_code和city_code不能为空。只填province_code时，该省全部选择；province_code和city_code都填时，该市全部选择。province_code，city_code和area_code都填时，该县全部选择。具体code可以参考https:# docs.alipay.com/isv/10327
    serviceRegionInfo = None
    # 小程序第三张应用截图，不能超过4MB，图片格式只支持jpg，png
    thirdScreenShot = None
    # 小程序版本描述
    versionDesc = None
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

    def setAppVersion(self, appVersion):
        self.appVersion = appVersion
        self.apiParas["app_version"] = appVersion

    def getAppVersion(self):
        return self.appVersion

    def setFifthScreenShot(self, fifthScreenShot):
        self.fifthScreenShot = fifthScreenShot
        self.apiParas["fifth_screen_shot"] = fifthScreenShot

    def getFifthScreenShot(self):
        return self.fifthScreenShot

    def setFirstScreenShot(self, firstScreenShot):
        self.firstScreenShot = firstScreenShot
        self.apiParas["first_screen_shot"] = firstScreenShot

    def getFirstScreenShot(self):
        return self.firstScreenShot

    def setFourthScreenShot(self, fourthScreenShot):
        self.fourthScreenShot = fourthScreenShot
        self.apiParas["fourth_screen_shot"] = fourthScreenShot

    def getFourthScreenShot(self):
        return self.fourthScreenShot

    def setMemo(self, memo):
        self.memo = memo
        self.apiParas["memo"] = memo

    def getMemo(self):
        return self.memo

    def setRegionType(self, regionType):
        self.regionType = regionType
        self.apiParas["region_type"] = regionType

    def getRegionType(self):
        return self.regionType

    def setSecondScreenShot(self, secondScreenShot):
        self.secondScreenShot = secondScreenShot
        self.apiParas["second_screen_shot"] = secondScreenShot

    def getSecondScreenShot(self):
        return self.secondScreenShot

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

    def setServiceRegionInfo(self, serviceRegionInfo):
        self.serviceRegionInfo = serviceRegionInfo
        self.apiParas["service_region_info"] = serviceRegionInfo

    def getServiceRegionInfo(self):
        return self.serviceRegionInfo

    def setThirdScreenShot(self, thirdScreenShot):
        self.thirdScreenShot = thirdScreenShot
        self.apiParas["third_screen_shot"] = thirdScreenShot

    def getThirdScreenShot(self):
        return self.thirdScreenShot

    def setVersionDesc(self, versionDesc):
        self.versionDesc = versionDesc
        self.apiParas["version_desc"] = versionDesc

    def getVersionDesc(self):
        return self.versionDesc

    def getApiMethodName(self):
        return "alipay.open.mini.version.audit.apply"

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
