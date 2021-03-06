# ALIPAY API: alipay.open.public.life.modify request
#
# @author auto create
# @since 1.0, 2017-12-18 14:58:00
class AlipayOpenPublicLifeModifyRequest:
    # 背景图片，需上传图片原始二进制流，此图片显示在支付宝客户端生活号主页上方背景图位置，后缀是jpg或者jpeg，图片大小限制1mb
    background = None
    # 联系人邮箱，可以是调用者的联系人邮箱
    contactEmail = None
    # 联系人姓名，可以是调用者的联系人姓名
    contactName = None
    # 联系人电话，可以是调用者的联系人电话
    contactTel = None
    # 客服电话，可以是电话号码，手机号码，400电话
    customerTel = None
    # 生活号描述，此内容显示在支付宝客户端生活号主页简介区块
    description = None
    # 扩展信息JSON串。为空则不修改，不为空则覆盖更新
    extendData = None
    # 生活号名称
    lifeName = None
    # logo图片，需上传图片原始二进制流，此图片显示在支付宝客户端生活号主页上方位置，后缀是jpg或者jpeg，图片大小限制1mb，图片最小150px，图片建议为是正方形。为空则不修改。
    logo = None
    # 用户ID
    userId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBackground(self, background):
        self.background = background
        self.apiParas["background"] = background

    def getBackground(self):
        return self.background

    def setContactEmail(self, contactEmail):
        self.contactEmail = contactEmail
        self.apiParas["contact_email"] = contactEmail

    def getContactEmail(self):
        return self.contactEmail

    def setContactName(self, contactName):
        self.contactName = contactName
        self.apiParas["contact_name"] = contactName

    def getContactName(self):
        return self.contactName

    def setContactTel(self, contactTel):
        self.contactTel = contactTel
        self.apiParas["contact_tel"] = contactTel

    def getContactTel(self):
        return self.contactTel

    def setCustomerTel(self, customerTel):
        self.customerTel = customerTel
        self.apiParas["customer_tel"] = customerTel

    def getCustomerTel(self):
        return self.customerTel

    def setDescription(self, description):
        self.description = description
        self.apiParas["description"] = description

    def getDescription(self):
        return self.description

    def setExtendData(self, extendData):
        self.extendData = extendData
        self.apiParas["extend_data"] = extendData

    def getExtendData(self):
        return self.extendData

    def setLifeName(self, lifeName):
        self.lifeName = lifeName
        self.apiParas["life_name"] = lifeName

    def getLifeName(self):
        return self.lifeName

    def setLogo(self, logo):
        self.logo = logo
        self.apiParas["logo"] = logo

    def getLogo(self):
        return self.logo

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.open.public.life.modify"

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
