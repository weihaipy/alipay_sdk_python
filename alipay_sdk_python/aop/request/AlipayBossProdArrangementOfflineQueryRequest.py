# ALIPAY API: alipay.boss.prod.arrangement.offline.query request
#
# @author auto create
# @since 1.0, 2017-04-14 21:06:47
class AlipayBossProdArrangementOfflineQueryRequest:
    # 签约销售方案的主站产品码，目前只支持ONLINE_TRADE_PAY（在线购买签约）和FACE_TO_FACE_PAYMENT（当面付）两个常量值，不允许传入其他值，否则报SYSTEM_ERROR异常。不传值时，默认查询FACE_TO_FACE_PAYM（当面付产品）。
    productCode = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setProductCode(self, productCode):
        self.productCode = productCode
        self.apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.productCode

    def getApiMethodName(self):
        return "alipay.boss.prod.arrangement.offline.query"

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
