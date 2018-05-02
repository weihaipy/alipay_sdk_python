# ALIPAY API: alipay.user.trade.search request
#
# @author auto create
# @since 1.0, 2018-03-14 11:11:45
class AlipayUserTradeSearchRequest:
    # 支付宝订单号，为空查询所有记录
    alipayOrderNo = None
    # 结束时间。与开始时间间隔在七天之内
    endTime = None
    # 商户订单号，为空查询所有记录
    merchantOrderNo = None
    # 订单来源，为空查询所有来源。淘宝(TAOBAO)，支付宝(ALIPAY)，其它(OTHER)
    orderFrom = None
    # 订单状态，为空查询所有状态订单。例如：等待买家付款（WAIT_BUYER_PAY），等待卖家发货（WAIT_SELLER_SEND_GOODS），等待买家确认收货（WAIT_BUYER_CONFIRM_GOODS），交易完成（TRADE_FINISHED），交易关闭（TRADE_CLOSED），交易成功（TRADE_SUCCESS）
    orderStatus = None
    # 订单类型，为空查询所有类型订单。例如：交易（TRADE）,CAE代扣（CAE）,代付（PEERPAY）,转账到卡（TRANSFER）
    orderType = None
    # 页码。取值范围:大于零的整数 默认值1
    pageNo = None
    # 每页获取条数。最大值500。
    pageSize = None
    # 开始时间，时间必须是今天范围之内。格式为yyyy-MM-dd HH:mm:ss，精确到秒(升级后的api 1.1版本)
    startTime = None
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

    def setEndTime(self, endTime):
        self.endTime = endTime
        self.apiParas["end_time"] = endTime

    def getEndTime(self):
        return self.endTime

    def setMerchantOrderNo(self, merchantOrderNo):
        self.merchantOrderNo = merchantOrderNo
        self.apiParas["merchant_order_no"] = merchantOrderNo

    def getMerchantOrderNo(self):
        return self.merchantOrderNo

    def setOrderFrom(self, orderFrom):
        self.orderFrom = orderFrom
        self.apiParas["order_from"] = orderFrom

    def getOrderFrom(self):
        return self.orderFrom

    def setOrderStatus(self, orderStatus):
        self.orderStatus = orderStatus
        self.apiParas["order_status"] = orderStatus

    def getOrderStatus(self):
        return self.orderStatus

    def setOrderType(self, orderType):
        self.orderType = orderType
        self.apiParas["order_type"] = orderType

    def getOrderType(self):
        return self.orderType

    def setPageNo(self, pageNo):
        self.pageNo = pageNo
        self.apiParas["page_no"] = pageNo

    def getPageNo(self):
        return self.pageNo

    def setPageSize(self, pageSize):
        self.pageSize = pageSize
        self.apiParas["page_size"] = pageSize

    def getPageSize(self):
        return self.pageSize

    def setStartTime(self, startTime):
        self.startTime = startTime
        self.apiParas["start_time"] = startTime

    def getStartTime(self):
        return self.startTime

    def getApiMethodName(self):
        return "alipay.user.trade.search"

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
