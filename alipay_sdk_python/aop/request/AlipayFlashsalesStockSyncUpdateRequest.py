# ALIPAY API: alipay.flashsales.stock.sync.update request
#
# @author auto create
# @since 1.0, 2014-08-22 15:32:32
class AlipayFlashsalesStockSyncUpdateRequest:
    # 商户的商品id
    outProductId = None
    # 服务窗id
    publicId = None
    # 库存数量
    stock = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setOutProductId(self, outProductId):
        self.outProductId = outProductId
        self.apiParas["out_product_id"] = outProductId

    def getOutProductId(self):
        return self.outProductId

    def setPublicId(self, publicId):
        self.publicId = publicId
        self.apiParas["public_id"] = publicId

    def getPublicId(self):
        return self.publicId

    def setStock(self, stock):
        self.stock = stock
        self.apiParas["stock"] = stock

    def getStock(self):
        return self.stock

    def getApiMethodName(self):
        return "alipay.flashsales.stock.sync.update"

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
