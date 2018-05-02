# ALIPAY API: alipay.point.order.add request
#
# @author auto create
# @since 1.0, 2017-07-11 11:00:47
class AlipayPointOrderAddRequest:
    # 向用户展示集分宝发放备注
    memo = None
    # isv提供的发放订单号，由数字和字母组成，最大长度为32位，需要保证每笔订单发放的唯一性，支付宝对该参数做唯一性校验。如果订单号已存在，支付宝将返回订单号已经存在的错误
    merchantOrderNo = None
    # 发放集分宝时间
    orderTime = None
    # 发放集分宝的数量
    pointCount = None
    # 用户标识符，用于指定集分宝发放的用户，和user_symbol_type一起使用，确定一个唯一的支付宝用户
    userSymbol = None
    # 用户标识符类型，现在支持ALIPAY_USER_ID:表示支付宝用户ID,ALIPAY_LOGON_ID:表示支付宝登陆号
    userSymbolType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

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

    def setOrderTime(self, orderTime):
        self.orderTime = orderTime
        self.apiParas["order_time"] = orderTime

    def getOrderTime(self):
        return self.orderTime

    def setPointCount(self, pointCount):
        self.pointCount = pointCount
        self.apiParas["point_count"] = pointCount

    def getPointCount(self):
        return self.pointCount

    def setUserSymbol(self, userSymbol):
        self.userSymbol = userSymbol
        self.apiParas["user_symbol"] = userSymbol

    def getUserSymbol(self):
        return self.userSymbol

    def setUserSymbolType(self, userSymbolType):
        self.userSymbolType = userSymbolType
        self.apiParas["user_symbol_type"] = userSymbolType

    def getUserSymbolType(self):
        return self.userSymbolType

    def getApiMethodName(self):
        return "alipay.point.order.add"

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
