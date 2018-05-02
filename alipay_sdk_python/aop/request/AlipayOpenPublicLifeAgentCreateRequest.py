# ALIPAY API: alipay.open.public.life.agent.create request
#
# @author auto create
# @since 1.0, 2017-11-02 20:21:32
class AlipayOpenPublicLifeAgentCreateRequest:
    # isv代开通生活号的商户支付宝账号或者商户支付宝账号pid（2088开头16位长度的字符串），账号需通过实名认证
    account = None
    # 生活号背景图片
    backgroundPic = None
    # 营业执照授权函图片，个体工商户如果使用总公司或其他公司的营业执照认证需上传该授权函图片
    businessLicenseAuthPic = None
    # 营业执照号码。被代创建商户运营主体为个人账户必填，企业账户无需填写
    businessLicenseNo = None
    # 营业执照图片。被代创建商户运营主体为个人账户必填，企业账户无需填写
    businessLicensePic = None
    # 联系人邮箱
    contactEmail = None
    # 联系人手机号
    contactMobile = None
    # 联系人名称
    contactName = None
    # 生活号头像
    logoPic = None
    # 所属MCCCode，详情可参考
    # < a href = "https:# doc.open.alipay.com/docs/doc.htm?spm=a219a.7629140.0.0.INIZWb&articleId=105364&docType=1" > 商家经营类目 < / a > 中的“经营类目编码”
    mccCode = None
    # 外部入驻申请单据号，由开发者生成，并需保证在开发者端不重复。另，如果代创建被驳回，需更换新的申请号，原申请号不能再次使用
    outBizNo = None
    # 自有知识产权证书图片
    ownIntellectualPic = None
    # 生活号简介
    publicDesc = None
    # 生活号名称
    publicName = None
    # 店铺内景图片，被代创建商户运营主体为个人账户必填，企业账户选填
    shopScenePic = None
    # 店铺门头照图片，被代创建商户运营主体为个人账户必填，企业账户选填
    shopSignBoardPic = None
    # 企业特殊资质图片，可参考 <a href="https:# doc.open.alipay.com/docs/doc.htm?spm=a219a.7629140.0.0.INIZWb&articleId=105364&docType=1">商家经营类目</a> 中的 “需要的特殊资质证书”
    specialLicensePic = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAccount(self, account):
        self.account = account
        self.apiParas["account"] = account

    def getAccount(self):
        return self.account

    def setBackgroundPic(self, backgroundPic):
        self.backgroundPic = backgroundPic
        self.apiParas["background_pic"] = backgroundPic

    def getBackgroundPic(self):
        return self.backgroundPic

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

    def setContactEmail(self, contactEmail):
        self.contactEmail = contactEmail
        self.apiParas["contact_email"] = contactEmail

    def getContactEmail(self):
        return self.contactEmail

    def setContactMobile(self, contactMobile):
        self.contactMobile = contactMobile
        self.apiParas["contact_mobile"] = contactMobile

    def getContactMobile(self):
        return self.contactMobile

    def setContactName(self, contactName):
        self.contactName = contactName
        self.apiParas["contact_name"] = contactName

    def getContactName(self):
        return self.contactName

    def setLogoPic(self, logoPic):
        self.logoPic = logoPic
        self.apiParas["logo_pic"] = logoPic

    def getLogoPic(self):
        return self.logoPic

    def setMccCode(self, mccCode):
        self.mccCode = mccCode
        self.apiParas["mcc_code"] = mccCode

    def getMccCode(self):
        return self.mccCode

    def setOutBizNo(self, outBizNo):
        self.outBizNo = outBizNo
        self.apiParas["out_biz_no"] = outBizNo

    def getOutBizNo(self):
        return self.outBizNo

    def setOwnIntellectualPic(self, ownIntellectualPic):
        self.ownIntellectualPic = ownIntellectualPic
        self.apiParas["own_intellectual_pic"] = ownIntellectualPic

    def getOwnIntellectualPic(self):
        return self.ownIntellectualPic

    def setPublicDesc(self, publicDesc):
        self.publicDesc = publicDesc
        self.apiParas["public_desc"] = publicDesc

    def getPublicDesc(self):
        return self.publicDesc

    def setPublicName(self, publicName):
        self.publicName = publicName
        self.apiParas["public_name"] = publicName

    def getPublicName(self):
        return self.publicName

    def setShopScenePic(self, shopScenePic):
        self.shopScenePic = shopScenePic
        self.apiParas["shop_scene_pic"] = shopScenePic

    def getShopScenePic(self):
        return self.shopScenePic

    def setShopSignBoardPic(self, shopSignBoardPic):
        self.shopSignBoardPic = shopSignBoardPic
        self.apiParas["shop_sign_board_pic"] = shopSignBoardPic

    def getShopSignBoardPic(self):
        return self.shopSignBoardPic

    def setSpecialLicensePic(self, specialLicensePic):
        self.specialLicensePic = specialLicensePic
        self.apiParas["special_license_pic"] = specialLicensePic

    def getSpecialLicensePic(self):
        return self.specialLicensePic

    def getApiMethodName(self):
        return "alipay.open.public.life.agent.create"

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
