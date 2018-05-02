# ALIPAY API: alipay.micropay.order.direct.pay request
#
# @author auto create
# @since 1.0, 2018-02-06 10:34:09
class AlipayMicropayOrderDirectPayRequest:
    # 支付宝订单号，冻结流水号.这个是创建冻结订单支付宝返回的
    alipayOrderNo = None

    # 支付金额,区间必须在[0.01,30]，只能保留小数点后两位
    amount = None

    # 支付备注
    memo = None

    # 收款方的支付宝ID
    receiveUserId = None

    # 本次转账的外部单据号（只能由字母和数字组成,maxlength=32
    transferOutOrderNo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAlipayOrderNo(self, alipayOrderNo):
        self.alipayOrderNo = alipayOrderNo
        self.apiParas["alipay_order_no"] = alipayOrderNo

    def getAlipayOrderNo(self):
        return self.alipayOrderNo

    def setAmount(self, amount):
        self.amount = amount
        self.apiParas["amount"] = amount

    def getAmount(self):
        return self.amount

    def setMemo(self, memo):
        self.memo = memo
        self.apiParas["memo"] = memo

    def getMemo(self):
        return self.memo

    def setReceiveUserId(self, receiveUserId):
        self.receiveUserId = receiveUserId
        self.apiParas["receive_user_id"] = receiveUserId

    def getReceiveUserId(self):
        return self.receiveUserId

    def setTransferOutOrderNo(self, transferOutOrderNo):
        self.transferOutOrderNo = transferOutOrderNo
        self.apiParas["transfer_out_order_no"] = transferOutOrderNo

    def getTransferOutOrderNo(self):
        return self.transferOutOrderNo

    def getApiMethodName(self):
        return "alipay.micropay.order.direct.pay"

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
