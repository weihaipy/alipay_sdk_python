# ALIPAY API: alipay.offline.market.shop.public.unbind request
#
# @author auto create
# @since 1.0, 2016-12-19 20:52:06
class AlipayOfflineMarketShopPublicUnbindRequest:
    # 是否解绑所有门店，T表示解绑所有门店，F表示解绑指定shop_ids的门店列表
    isAll = None

    # 解除绑定门店的ID列表，一次最多解绑100个门店，is_all为T时表示解除绑定本商家下所有门店，即门店列表无需通过本参数shop_ids传入，由系统自动查询is_all为F时该参数必填
    shopIds = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setIsAll(self, isAll):
        self.isAll = isAll
        self.apiParas["is_all"] = isAll

    def getIsAll(self):
        return self.isAll

    def setShopIds(self, shopIds):
        self.shopIds = shopIds
        self.apiParas["shop_ids"] = shopIds

    def getShopIds(self):
        return self.shopIds

    def getApiMethodName(self):
        return "alipay.offline.market.shop.public.unbind"

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
