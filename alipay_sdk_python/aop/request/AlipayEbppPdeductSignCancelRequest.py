# ALIPAY API: alipay.ebpp.pdeduct.sign.cancel request
#
# @author auto create
# @since 1.0, 2017-08-04 11:19:20
class AlipayEbppPdeductSignCancelRequest:
    # 此值只是供代扣中心做最后的渠道统计用，并不做值是什么的强校验，只要不为空就可以
    agentChannel = None

    # 标识发起方的ID，从服务窗发起则为appId的值，appId即开放平台分配给接入ISV的id，此处也可以随便真其它值，只要能标识唯一即可
    agentCode = None

    # 支付宝代扣协议ID
    agreementId = None

    # 需要用户首先处于登陆态，然后访问https:# ebppprod.alipay.com/deduct/enterMobileicPayPassword.htm?cb=自己指定的回跳连接地址,访问页面后会进到独立密码校验页，用户输入密码校验成功后，会生成token回调到指定的回跳地址，如果设置cb=www.baidu.com则最后回调的内容是www.baidu.com?token=312314ADFDSFAS,然后签约时直接取得地址后token的值即可
    payPasswordToken = None

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

    def setAgentChannel(self, agentChannel):
        self.agentChannel = agentChannel
        self.apiParas["agent_channel"] = agentChannel

    def getAgentChannel(self):
        return self.agentChannel

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

    def setPayPasswordToken(self, payPasswordToken):
        self.payPasswordToken = payPasswordToken
        self.apiParas["pay_password_token"] = payPasswordToken

    def getPayPasswordToken(self):
        return self.payPasswordToken

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.ebpp.pdeduct.sign.cancel"

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
