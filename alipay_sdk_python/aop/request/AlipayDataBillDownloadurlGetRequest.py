# ALIPAY API: alipay.data.bill.downloadurl.get request
#
# @author auto create
# @since 1.0, 2017-04-14 11:43:02
class AlipayDataBillDownloadurlGetRequest:
    # 账单时间：日账单格式为yyyy-MM-dd,月账单格式为yyyy-MM
    billDate = None

    # 账单类型，目前支持的类型由：trade、air、air_b2b；trade指商户通过接口所获取的账单，或商户经开放平台授权后其所属服务商通过接口所获取的账单；air、air_b2b是航旅行业定制的账单，一般商户没有此账单；
    billType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBillDate(self, billDate):
        self.billDate = billDate
        self.apiParas["bill_date"] = billDate

    def getBillDate(self):
        return self.billDate

    def setBillType(self, billType):
        self.billType = billType
        self.apiParas["bill_type"] = billType

    def getBillType(self):
        return self.billType

    def getApiMethodName(self):
        return "alipay.data.bill.downloadurl.get"

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
