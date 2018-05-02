# ALIPAY API: alipay.micropay.order.freeze request
#
# @author auto create
# @since 1.0, 2016-06-06 17:49:00
class AlipayMicropayOrderFreezeRequest:
    # 需要冻结金额，[0.01,2000]，必须是正数，最多只能保留小数点两位,单位是元
    amount = None

    # 冻结资金的到期时间，超过此日期，冻结金会自动解冻,时间要求是:[当前时间+24h,订购时间-8h] .
    expireTime = None

    # 冻结备注,maxLength=40
    memo = None

    # 商户订单号,只能由字母和数字组成，最大长度32.此外部订单号与支付宝的冻结订单号对应,注意 应用id和订购者id和外部订单号必须保证唯一性。
    merchantOrderNo = None

    # 在解冻转账的时候的支付方式: NO_CONFIRM：不需要付款确认，调用接口直接扣款 PAY_PASSWORD: 在转账需要付款方用支付密码确认，才可以转账成功
    payConfirm = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAmount(self, amount):
        self.amount = amount
        self.apiParas["amount"] = amount

    def getAmount(self):
        return self.amount

    def setExpireTime(self, expireTime):
        self.expireTime = expireTime
        self.apiParas["expire_time"] = expireTime

    def getExpireTime(self):
        return self.expireTime

    def setMemo(self, memo):
        self.memo = memo
        self.apiParas["memo"] = memo

    def getMemo(self):
        return self.memo

    def setMerchantOrderNo(self, merchantOrderNo):
        self.merchantOrderNo = merchantOrderNo
        self.apiParas["merchant_order_no"] = merchantOrderNo

    def getMerchantOrderNo(self):
        return self.merchantOrderNo

    def setPayConfirm(self, payConfirm):
        self.payConfirm = payConfirm
        self.apiParas["pay_confirm"] = payConfirm

    def getPayConfirm(self):
        return self.payConfirm

    def getApiMethodName(self):
        return "alipay.micropay.order.freeze"

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
