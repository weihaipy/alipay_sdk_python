# ALIPAY API: alipay.ebpp.pdeduct.pay request
#
# @author auto create
# @since 1.0, 2017-04-07 16:45:48
class AlipayEbppPdeductPayRequest:
    # 渠道码，如用户通过机构通过服务窗进来签约则是PUBLICFORM，此值可随意传，只要不空就行
    agentChannel = None
    # 二级渠道码，预留字段
    agentCode = None
    # 支付宝代扣协议Id
    agreementId = None
    # 账期
    billDate = None
    # 户号，缴费单位用于标识每一户的唯一性的
    billKey = None
    # 扩展参数。必须以key value形式定义，

    # 转为json为格式："key1": "value1", "key2": "value2",
    # "key3": "value3", "key4": "value4"
    # 后端会直接转换为MAP对象，转换异常会报参数格式错误
    extendField = None
    # 滞纳金
    fineAmount = None
    # 备注信息
    memo = None
    # 商户外部业务流水号
    outOrderNo = None
    # 扣款金额，支付总金额，包含滞纳金
    payAmount = None
    # 商户PartnerId
    pid = None
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

    def setBillDate(self, billDate):
        self.billDate = billDate
        self.apiParas["bill_date"] = billDate

    def getBillDate(self):
        return self.billDate

    def setBillKey(self, billKey):
        self.billKey = billKey
        self.apiParas["bill_key"] = billKey

    def getBillKey(self):
        return self.billKey

    def setExtendField(self, extendField):
        self.extendField = extendField
        self.apiParas["extend_field"] = extendField

    def getExtendField(self):
        return self.extendField

    def setFineAmount(self, fineAmount):
        self.fineAmount = fineAmount
        self.apiParas["fine_amount"] = fineAmount

    def getFineAmount(self):
        return self.fineAmount

    def setMemo(self, memo):
        self.memo = memo
        self.apiParas["memo"] = memo

    def getMemo(self):
        return self.memo

    def setOutOrderNo(self, outOrderNo):
        self.outOrderNo = outOrderNo
        self.apiParas["out_order_no"] = outOrderNo

    def getOutOrderNo(self):
        return self.outOrderNo

    def setPayAmount(self, payAmount):
        self.payAmount = payAmount
        self.apiParas["pay_amount"] = payAmount

    def getPayAmount(self):
        return self.payAmount

    def setPid(self, pid):
        self.pid = pid
        self.apiParas["pid"] = pid

    def getPid(self):
        return self.pid

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.ebpp.pdeduct.pay"

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
