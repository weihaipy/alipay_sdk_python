# ALIPAY API: alipay.transfer.thirdparty.bill.create request
#
# @author auto create
# @since 1.0, 2014-06-25 17:00:56
class AlipayTransferThirdpartyBillCreateRequest:
    # 收款金额，单位：分
    amount = None
    # 收款币种，默认为156（人民币）目前只允许转账人民币
    currency = None
    # 扩展参数
    extParam = None
    # 转账备注
    memo = None
    # 合作方的支付宝帐号UID
    partnerId = None
    # 外部系统收款方UID，付款人和收款人不能是同一个帐户
    payeeAccount = None
    # （同payer_type所列举的）
    # 目前限制payer_type和payee_type必须一致
    payeeType = None
    # 外部系统付款方的UID
    payerAccount = None
    # 1-支付宝帐户
    # 2 - 淘宝帐户
    # 10001 - 新浪微博帐户
    # 10002 - 阿里云帐户
    # （1、2目前对外不可见、不可用）
    payerType = None
    # 发起支付交易来源方定义的交易ID，用于将支付回执通知给来源方。不同来源方给出的ID可以重复，同一个来源方给出的ID唯一性由来源方保证。
    paymentId = None
    # 支付来源
    # 10001 - 新浪微博
    # 10002 - 阿里云
    paymentSource = None
    # 支付款项的标题
    title = None
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

    def setCurrency(self, currency):
        self.currency = currency
        self.apiParas["currency"] = currency

    def getCurrency(self):
        return self.currency

    def setExtParam(self, extParam):
        self.extParam = extParam
        self.apiParas["ext_param"] = extParam

    def getExtParam(self):
        return self.extParam

    def setMemo(self, memo):
        self.memo = memo
        self.apiParas["memo"] = memo

    def getMemo(self):
        return self.memo

    def setPartnerId(self, partnerId):
        self.partnerId = partnerId
        self.apiParas["partner_id"] = partnerId

    def getPartnerId(self):
        return self.partnerId

    def setPayeeAccount(self, payeeAccount):
        self.payeeAccount = payeeAccount
        self.apiParas["payee_account"] = payeeAccount

    def getPayeeAccount(self):
        return self.payeeAccount

    def setPayeeType(self, payeeType):
        self.payeeType = payeeType
        self.apiParas["payee_type"] = payeeType

    def getPayeeType(self):
        return self.payeeType

    def setPayerAccount(self, payerAccount):
        self.payerAccount = payerAccount
        self.apiParas["payer_account"] = payerAccount

    def getPayerAccount(self):
        return self.payerAccount

    def setPayerType(self, payerType):
        self.payerType = payerType
        self.apiParas["payer_type"] = payerType

    def getPayerType(self):
        return self.payerType

    def setPaymentId(self, paymentId):
        self.paymentId = paymentId
        self.apiParas["payment_id"] = paymentId

    def getPaymentId(self):
        return self.paymentId

    def setPaymentSource(self, paymentSource):
        self.paymentSource = paymentSource
        self.apiParas["payment_source"] = paymentSource

    def getPaymentSource(self):
        return self.paymentSource

    def setTitle(self, title):
        self.title = title
        self.apiParas["title"] = title

    def getTitle(self):
        return self.title

    def getApiMethodName(self):
        return "alipay.transfer.thirdparty.bill.create"

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
