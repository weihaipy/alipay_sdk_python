# ALIPAY API: alipay.open.public.life.account.create request
#
# @author auto create
# @since 1.0, 2017-08-01 16:01:03
class AlipayOpenPublicLifeAccountCreateRequest:
    # 背景图片，需上传图片原始二进制流，此图片显示在支付宝客户端生活号主页上方背景图位置，后缀是jpg或者jpeg，图片大小限制1mb
    background = None
    # 生活号二级分类id，请按照以下分类进行填写，非以下分类账号请联系相应人员添加类别
    # 综合媒体(INTEG)，新闻(NEWS)，科技(SCIENCE)，养生(WELLNESS)，财经(FINANCE)，情感(EMOTION)，美食(DELICACY)，搞笑(FUNNY)，娱乐(ENTERTM)，摄影(SHOOT)，影视(MOVIES)，教育(EDUCATE)，文艺(LITER)，时尚(FASHION)，动漫(COMIC)，美妆(COSMETIC)，体育(SPOTRS)，旅行(TRIP)，健身(BODYB)，星座(CONSTT)，音乐(ONGAKU)，母婴(MUNBABY)，公益(PUBLICW)，汽车(CARS)，地产(LAND)，数码(NUMERAL)，游戏(GAMES)，电视剧(TVPLAY)，宠物(PET)，其他(OTHERS)
    catagoryId = None
    # 联系人邮箱，可以是调用者的联系人邮箱
    contactEmail = None
    # 联系人电话，可以是调用者的联系人电话
    contactTel = None
    # 生活号简介，此内容显示在支付宝客户端生活号主页简介区块
    content = None
    # 客服电话，可以是电话号码，手机号码，400电话
    customerTel = None
    # 生活号名称，该名称会显示在支付宝客户端生活号主页上方
    lifeName = None
    # logo图片，需上传图片原始二进制流，此图片显示在支付宝客户端生活号主页上方位置，后缀是jpg或者jpeg，图片大小限制1mb
    logo = None
    # 支付宝用户id，由支付宝同学提供用户id，为该生活号对应pid
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

    def setCatagoryId(self, catagoryId):
        self.catagoryId = catagoryId
        self.apiParas["catagory_id"] = catagoryId

    def getCatagoryId(self):
        return self.catagoryId

    def setContactEmail(self, contactEmail):
        self.contactEmail = contactEmail
        self.apiParas["contact_email"] = contactEmail

    def getContactEmail(self):
        return self.contactEmail

    def setContactTel(self, contactTel):
        self.contactTel = contactTel
        self.apiParas["contact_tel"] = contactTel

    def getContactTel(self):
        return self.contactTel

    def setContent(self, content):
        self.content = content
        self.apiParas["content"] = content

    def getContent(self):
        return self.content

    def setCustomerTel(self, customerTel):
        self.customerTel = customerTel
        self.apiParas["customer_tel"] = customerTel

    def getCustomerTel(self):
        return self.customerTel

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
        return "alipay.open.public.life.account.create"

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
