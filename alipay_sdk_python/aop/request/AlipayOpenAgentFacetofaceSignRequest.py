# ALIPAY API: alipay.open.agent.facetoface.sign request
#
# @author auto create
# @since 1.0, 2018-01-31 21:19:41
class AlipayOpenAgentFacetofaceSignRequest:
    # 代商户操作事务编号，通过alipay.open.isv.agent.create接口进行创建。
    batchNo = None

    # 营业执照授权函图片，个体工商户如果使用总公司或其他公司的营业执照认证需上传该授权函图片，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    businessLicenseAuthPic = None

    # 营业执照号码
    businessLicenseNo = None

    # 营业执照图片。被代创建商户运营主体为个人账户必填，企业账户无需填写，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    businessLicensePic = None

    # 营业期限
    dateLimitation = None

    # 营业期限是否长期有效
    longTerm = None

    # 所属MCCCode，详情可参考
    # < a href = "https:# doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.59bgD2&treeId=222&articleId=105364&docType=1# s1">商家经营类目</a> 中的“经营类目编码”
    mccCode = None

    # 店铺内景图片，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    shopScenePic = None

    # 店铺门头照图片，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    shopSignBoardPic = None

    # 企业特殊资质图片，可参考
    # < ahref = "https:# doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.59bgD2&treeId=222&articleId=105364&docType=1# s1">商家经营类目</a> 中的“需要的特殊资质证书”，最小50KB，图片格式必须为：png、bmp、gif、jpg、jpeg
    specialLicensePic = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

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

    def setDateLimitation(self, dateLimitation):
        self.dateLimitation = dateLimitation
        self.apiParas["date_limitation"] = dateLimitation

    def getDateLimitation(self):
        return self.dateLimitation

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
        return "alipay.open.agent.facetoface.sign"

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
