# ALIPAY API: alipay.ebpp.pdeduct.bill.pay.status request
#
# @author auto create
# @since 1.0, 2017-08-04 11:19:05
class AlipayEbppPdeductBillPayStatusRequest:
    # 支付宝用户ID
    agreementId = None

    # 商户代扣业务流水
    outOrderNo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAgreementId(self, agreementId):
        self.agreementId = agreementId
        self.apiParas["agreement_id"] = agreementId

    def getAgreementId(self):
        return self.agreementId

    def setOutOrderNo(self, outOrderNo):
        self.outOrderNo = outOrderNo
        self.apiParas["out_order_no"] = outOrderNo

    def getOutOrderNo(self):
        return self.outOrderNo

    def getApiMethodName(self):
        return "alipay.ebpp.pdeduct.bill.pay.status"

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
