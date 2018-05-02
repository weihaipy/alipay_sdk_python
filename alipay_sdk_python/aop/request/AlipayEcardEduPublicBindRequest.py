# ALIPAY API: alipay.ecard.edu.public.bind request
#
# @author auto create
# @since 1.0, 2014-06-12 17:16:41
class AlipayEcardEduPublicBindRequest:
    # 机构编码
    agentCode = None
    # 公众账号协议Id
    agreementId = None
    # 支付宝userId
    alipayUserId = None
    # 一卡通姓名
    cardName = None
    # 一卡通卡号
    cardNo = None
    # 公众账号id
    publicId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAgentCode(self, agentCode):
        self.agentCode = agentCode
        self.apiParas["agent_code"] = agentCode

    def getAgentCode(self):
        return self.agentCode

    def setAgreementId(self, agreementId):
        self.agreementId = agreementId
        self.apiParas["agreement_id"] = agreementId

    def getAgreementId(self):
        return self.agreementId

    def setAlipayUserId(self, alipayUserId):
        self.alipayUserId = alipayUserId
        self.apiParas["alipay_user_id"] = alipayUserId

    def getAlipayUserId(self):
        return self.alipayUserId

    def setCardName(self, cardName):
        self.cardName = cardName
        self.apiParas["card_name"] = cardName

    def getCardName(self):
        return self.cardName

    def setCardNo(self, cardNo):
        self.cardNo = cardNo
        self.apiParas["card_no"] = cardNo

    def getCardNo(self):
        return self.cardNo

    def setPublicId(self, publicId):
        self.publicId = publicId
        self.apiParas["public_id"] = publicId

    def getPublicId(self):
        return self.publicId

    def getApiMethodName(self):
        return "alipay.ecard.edu.public.bind"

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
