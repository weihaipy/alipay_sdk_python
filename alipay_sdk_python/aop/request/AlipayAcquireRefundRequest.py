# ALIPAY API: alipay.acquire.refund request
#
# @author auto create
# @since 1.0, 2014-06-12 17:17:03
class AlipayAcquireRefundRequest:
    # 卖家的操作员ID。
    operatorId = None
    # 操作员的类型：
    #  0：支付宝操作员
    #  1：商户的操作员
    #  如果传入其它值或者为空，则默认设置为1。
    operatorType = None

    # 商户退款请求单号，用以标识本次交易的退款请求。
    #  如果不传入本参数，则以out_trade_no填充本参数的值。同时，认为本次请求为全额退款，要求退款金额和交易支付金额一致。
    outRequestNo = None

    # 商户网站唯一订单号
    outTradeNo = None

    # 业务关联ID集合，用于放置商户的退款单号、退款流水号等信息，json格式
    refIds = None

    # 退款金额；退款金额不能大于订单金额，全额退款必须与订单金额一致。
    refundAmount = None

    # 退款原因说明。
    refundReason = None
    # 该交易在支付宝系统中的交易流水号。
    #  #  最短16位，最长64位。
    #  如果同时传了out_trade_no和trade_no，则以trade_no为准
    tradeNo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setOperatorId(self, operatorId):
        self.operatorId = operatorId
        self.apiParas["operator_id"] = operatorId

    def getOperatorId(self):
        return self.operatorId

    def setOperatorType(self, operatorType):
        self.operatorType = operatorType
        self.apiParas["operator_type"] = operatorType

    def getOperatorType(self):
        return self.operatorType

    def setOutRequestNo(self, outRequestNo):
        self.outRequestNo = outRequestNo
        self.apiParas["out_request_no"] = outRequestNo

    def getOutRequestNo(self):
        return self.outRequestNo

    def setOutTradeNo(self, outTradeNo):
        self.outTradeNo = outTradeNo
        self.apiParas["out_trade_no"] = outTradeNo

    def getOutTradeNo(self):
        return self.outTradeNo

    def setRefIds(self, refIds):
        self.refIds = refIds
        self.apiParas["ref_ids"] = refIds

    def getRefIds(self):
        return self.refIds

    def setRefundAmount(self, refundAmount):
        self.refundAmount = refundAmount
        self.apiParas["refund_amount"] = refundAmount

    def getRefundAmount(self):
        return self.refundAmount

    def setRefundReason(self, refundReason):
        self.refundReason = refundReason
        self.apiParas["refund_reason"] = refundReason

    def getRefundReason(self):
        return self.refundReason

    def setTradeNo(self, tradeNo):
        self.tradeNo = tradeNo
        self.apiParas["trade_no"] = tradeNo

    def getTradeNo(self):
        return self.tradeNo

    def getApiMethodName(self):
        return "alipay.acquire.refund"

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
