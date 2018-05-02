# ALIPAY API: alipay.open.agent.zhimabrief.sign request
#
# @author auto create
# @since 1.0, 2018-01-31 21:21:06
class AlipayOpenAgentZhimabriefSignRequest:
    # 支付宝生活号(原服务窗)名称（1 app_name、app_demo；2 web_sites；3 alipay_life_name；4 wechat_official_account_name。1、2、3、4至少选择一个填写）
    alipayLifeName = None
    # APP demo，格式为.apk；或者应用说明文档, 格式为.doc .docx .pdf格式（1 app_name、app_demo；2 web_sites；3 alipay_life_name；4 wechat_official_account_name。1、2、3、4至少选择一个填写）
    appDemo = None
    # 商户的APP应用名称（1 app_name、app_demo；2 web_sites；3 alipay_life_name；4 wechat_official_account_name。1、2、3、4至少选择一个填写）
    appName = None
    # 代商户操作事务编号，通过alipay.open.isv.agent.create接口进行创建。
    batchNo = None
    # 营业执照授权函图片，个体工商户如果使用总公司或其他公司的营业执照认证需上传该授权函图片，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    businessLicenseAuthPic = None
    # 营业执照号码。
    businessLicenseNo = None
    # 营业执照图片，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    businessLicensePic = None
    # 自定义使用场景描述，usage_scene选项中无符合描述，填写自定义使用场景描述(usage_scene不填写，则custom_usage_scene必填)
    customUsageScene = None
    # 营业期限
    dateLimitation = None
    # 数据反馈接口人
    drContact = None
    # 例如：浙江飞猪网络技术有限公司，企业别称请填写【飞猪】。
    enterpriseAlias = None
    # 企业LOGO-图片，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    enterpriseLogo = None
    # 营业期限是否长期有效
    longTerm = None
    # 所属MCCCode，详情可参考
    # < a href = "https:# doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.59bgD2&treeId=222&articleId=105364&docType=1# s1">商家经营类目</a> 中的“经营类目编码”
    mccCode = None
    # 异议处理接口人
    ohContact = None
    # 用户服务联动机制接口人
    prContact = None
    # 企业特殊资质图片，可参考
    # < a href = "https:# doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.59bgD2&treeId=222&articleId=105364&docType=1# s1">商家经营类目</a> 中的“需要的特殊资质证书”，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    specialLicensePic = None
    # 使用场景描述，签约芝麻信用产品的用途，可选值："现金放贷","其他", "消费分期（例如买房、装修等）", "融资租赁", "发放信用卡", "极速返利", "押金减免", "先用后付", "社交场景信用互查", "会员分层信用参考"
    usageScene = None
    # 接入网址信息（1 app_name、app_demo；2 web_sites；3 alipay_life_name；4 wechat_official_account_name。1、2、3、4至少选择一个填写）
    webSites = None
    # 微信公众号名称（1 app_name、app_demo；2 web_sites；3 alipay_life_name；4 wechat_official_account_name。1、2、3、4至少选择一个填写）
    wechatOfficialAccountName = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAlipayLifeName(self, alipayLifeName):
        self.alipayLifeName = alipayLifeName
        self.apiParas["alipay_life_name"] = alipayLifeName

    def getAlipayLifeName(self):
        return self.alipayLifeName

    def setAppDemo(self, appDemo):
        self.appDemo = appDemo
        self.apiParas["app_demo"] = appDemo

    def getAppDemo(self):
        return self.appDemo

    def setAppName(self, appName):
        self.appName = appName
        self.apiParas["app_name"] = appName

    def getAppName(self):
        return self.appName

    def setBatchNo(self, batchNo):
        self.batchNo = batchNo
        self.apiParas["batch_no"] = batchNo

    def getBatchNo(self):
        return self.batchNo

    def setBusinessLicenseAuthPic(self, businessLicenseAuthPic):
        self.businessLicenseAuthPic = businessLicenseAuthPic
        self.apiParas["business_license_auth_pic"] = businessLicenseAuthPic

    def getBusinessLicenseAuthPic(self):
        return self.businessLicenseAuthPic

    def setBusinessLicenseNo(self, businessLicenseNo):
        self.businessLicenseNo = businessLicenseNo
        self.apiParas["business_license_no"] = businessLicenseNo

    def getBusinessLicenseNo(self):
        return self.businessLicenseNo

    def setBusinessLicensePic(self, businessLicensePic):
        self.businessLicensePic = businessLicensePic
        self.apiParas["business_license_pic"] = businessLicensePic

    def getBusinessLicensePic(self):
        return self.businessLicensePic

    def setCustomUsageScene(self, customUsageScene):
        self.customUsageScene = customUsageScene
        self.apiParas["custom_usage_scene"] = customUsageScene

    def getCustomUsageScene(self):
        return self.customUsageScene

    def setDateLimitation(self, dateLimitation):
        self.dateLimitation = dateLimitation
        self.apiParas["date_limitation"] = dateLimitation

    def getDateLimitation(self):
        return self.dateLimitation

    def setDrContact(self, drContact):
        self.drContact = drContact
        self.apiParas["dr_contact"] = drContact

    def getDrContact(self):
        return self.drContact

    def setEnterpriseAlias(self, enterpriseAlias):
        self.enterpriseAlias = enterpriseAlias
        self.apiParas["enterprise_alias"] = enterpriseAlias

    def getEnterpriseAlias(self):
        return self.enterpriseAlias

    def setEnterpriseLogo(self, enterpriseLogo):
        self.enterpriseLogo = enterpriseLogo
        self.apiParas["enterprise_logo"] = enterpriseLogo

    def getEnterpriseLogo(self):
        return self.enterpriseLogo

    def setLongTerm(self, longTerm):
        self.longTerm = longTerm
        self.apiParas["long_term"] = longTerm

    def getLongTerm(self):
        return self.longTerm

    def setMccCode(self, mccCode):
        self.mccCode = mccCode
        self.apiParas["mcc_code"] = mccCode

    def getMccCode(self):
        return self.mccCode

    def setOhContact(self, ohContact):
        self.ohContact = ohContact
        self.apiParas["oh_contact"] = ohContact

    def getOhContact(self):
        return self.ohContact

    def setPrContact(self, prContact):
        self.prContact = prContact
        self.apiParas["pr_contact"] = prContact

    def getPrContact(self):
        return self.prContact

    def setSpecialLicensePic(self, specialLicensePic):
        self.specialLicensePic = specialLicensePic
        self.apiParas["special_license_pic"] = specialLicensePic

    def getSpecialLicensePic(self):
        return self.specialLicensePic

    def setUsageScene(self, usageScene):
        self.usageScene = usageScene
        self.apiParas["usage_scene"] = usageScene

    def getUsageScene(self):
        return self.usageScene

    def setWebSites(self, webSites):
        self.webSites = webSites
        self.apiParas["web_sites"] = webSites

    def getWebSites(self):
        return self.webSites

    def setWechatOfficialAccountName(self, wechatOfficialAccountName):
        self.wechatOfficialAccountName = wechatOfficialAccountName
        self.apiParas["wechat_official_account_name"] = wechatOfficialAccountName

    def getWechatOfficialAccountName(self):
        return self.wechatOfficialAccountName

    def getApiMethodName(self):
        return "alipay.open.agent.zhimabrief.sign"

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
