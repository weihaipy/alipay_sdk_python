# ALIPAY API: alipay.acquire.precreate request
#
# @author auto create
# @since 1.0, 2014-05-28 11:57:10
class AlipayAcquirePrecreateRequest:
    # 对一笔交易的具体描述信息。如果是多种商品，请将商品描述字符串累加传给body
    body = None
    # 描述多渠道收单的渠道明细信息，json格式
    channelParameters = None
    # 订单金额币种。目前只支持传入156（人民币）。
    # 如果为空，则默认设置为156
    currency = None
    # 公用业务扩展信息。用于商户的特定业务信息的传递，只有商户与支付宝约定了传递此参数且约定了参数含义，此参数才有效。
    # 比如可传递二维码支付场景下的门店ID等信息，以json格式传输。
    extendParams = None
    # 描述商品明细信息，json格式。
    goodsDetail = None
    # 订单支付超时时间。设置未付款交易的超时时间，一旦超时，该笔交易就会自动被关闭。
    # 取值范围：1m～15d。
    # m-分钟，h-小时，d-天，1c-当天（无论交易何时创建，都在0点关闭）。
    # 该参数数值不接受小数点，如1.5h，可转换为90m。
    # 该功能需要联系支付宝配置关闭时间。
    itBPay = None
    # 操作员的类型：
    # 0：支付宝操作员
    # 1：商户的操作员
    # 如果传入其它值或者为空，则默认设置为1
    operatorCode = None
    # 卖家的操作员ID
    operatorId = None
    # 支付宝合作商户网站唯一订单号
    outTradeNo = None
    # 订单中商品的单价。
    # 如果请求时传入本参数，则必须满足total_fee=price×quantity的条件
    price = None
    # 订单中商品的数量。
    # 如果请求时传入本参数，则必须满足total_fee=price×quantity的条件
    quantity = None
    # 分账信息。
    # 描述分账明细信息，json格式
    royaltyParameters = None
    # 分账类型。卖家的分账类型，目前只支持传入ROYALTY（普通分账类型）
    royaltyType = None
    # 卖家支付宝账号，可以为email或者手机号。如果seller_id不为空，则以seller_id的值作为卖家账号，忽略本参数
    sellerEmail = None
    # 卖家支付宝账号对应的支付宝唯一用户号，以2088开头的纯16位数字。如果和seller_email同时为空，则本参数默认填充partner的值
    sellerId = None
    # 收银台页面上，商品展示的超链接
    showUrl = None
    # 商品购买
    subject = None
    # 订单金额。该笔订单的资金总额，取值范围[0.01,100000000]，精确到小数点后2位。
    totalFee = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBody(self, body):
        self.body = body
        self.apiParas["body"] = body

    def getBody(self):
        return self.body

    def setChannelParameters(self, channelParameters):
        self.channelParameters = channelParameters
        self.apiParas["channel_parameters"] = channelParameters

    def getChannelParameters(self):
        return self.channelParameters

    def setCurrency(self, currency):
        self.currency = currency
        self.apiParas["currency"] = currency

    def getCurrency(self):
        return self.currency

    def setExtendParams(self, extendParams):
        self.extendParams = extendParams
        self.apiParas["extend_params"] = extendParams

    def getExtendParams(self):
        return self.extendParams

    def setGoodsDetail(self, goodsDetail):
        self.goodsDetail = goodsDetail
        self.apiParas["goods_detail"] = goodsDetail

    def getGoodsDetail(self):
        return self.goodsDetail

    def setItBPay(self, itBPay):
        self.itBPay = itBPay
        self.apiParas["it_b_pay"] = itBPay

    def getItBPay(self):
        return self.itBPay

    def setOperatorCode(self, operatorCode):
        self.operatorCode = operatorCode
        self.apiParas["operator_code"] = operatorCode

    def getOperatorCode(self):
        return self.operatorCode

    def setOperatorId(self, operatorId):
        self.operatorId = operatorId
        self.apiParas["operator_id"] = operatorId

    def getOperatorId(self):
        return self.operatorId

    def setOutTradeNo(self, outTradeNo):
        self.outTradeNo = outTradeNo
        self.apiParas["out_trade_no"] = outTradeNo

    def getOutTradeNo(self):
        return self.outTradeNo

    def setPrice(self, price):
        self.price = price
        self.apiParas["price"] = price

    def getPrice(self):
        return self.price

    def setQuantity(self, quantity):
        self.quantity = quantity
        self.apiParas["quantity"] = quantity

    def getQuantity(self):
        return self.quantity

    def setRoyaltyParameters(self, royaltyParameters):
        self.royaltyParameters = royaltyParameters
        self.apiParas["royalty_parameters"] = royaltyParameters

    def getRoyaltyParameters(self):
        return self.royaltyParameters

    def setRoyaltyType(self, royaltyType):
        self.royaltyType = royaltyType
        self.apiParas["royalty_type"] = royaltyType

    def getRoyaltyType(self):
        return self.royaltyType

    def setSellerEmail(self, sellerEmail):
        self.sellerEmail = sellerEmail
        self.apiParas["seller_email"] = sellerEmail

    def getSellerEmail(self):
        return self.sellerEmail

    def setSellerId(self, sellerId):
        self.sellerId = sellerId
        self.apiParas["seller_id"] = sellerId

    def getSellerId(self):
        return self.sellerId

    def setShowUrl(self, showUrl):
        self.showUrl = showUrl
        self.apiParas["show_url"] = showUrl

    def getShowUrl(self):
        return self.showUrl

    def setSubject(self, subject):
        self.subject = subject
        self.apiParas["subject"] = subject

    def getSubject(self):
        return self.subject

    def setTotalFee(self, totalFee):
        self.totalFee = totalFee
        self.apiParas["total_fee"] = totalFee

    def getTotalFee(self):
        return self.totalFee

    def getApiMethodName(self):
        return "alipay.acquire.precreate"

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
