# ALIPAY API: alipay.user.account.freeze.get request
#
# @author auto create
# @since 1.0, 2016-08-11 15:48:05
class AlipayUserAccountFreezeGetRequest:
    # 冻结类型，多个用,分隔。不传返回所有类型的冻结金额。 DEPOSIT_FREEZE,充值冻结 WITHDRAW_FREEZE,提现冻结 PAYMENT_FREEZE,支付冻结 BAIL_FREEZE,保证金冻结 CHARGE_FREEZE,收费冻结 PRE_DEPOSIT_FREEZE,预存款冻结 LOAN_FREEZE,贷款冻结 OTHER_FREEZE,其它
    freezeType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setFreezeType(self, freezeType):
        self.freezeType = freezeType
        self.apiParas["freeze_type"] = freezeType

    def getFreezeType(self):
        return self.freezeType

    def getApiMethodName(self):
        return "alipay.user.account.freeze.get"

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
