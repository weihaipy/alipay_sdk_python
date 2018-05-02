# ALIPAY API: alipay.acquire.createandpay request
#
# @author auto create
# @since 1.0, 2017-12-01 21:17:42
class AlipayAcquireCreateandpayRequest:
    # 证书签名
    alipayCaRequest = None
    # 对一笔交易的具体描述信息。如果是多种商品，请将商品描述字符串累加传给body。
    body = None
    # 买家支付宝账号，可以为email或者手机号。
    buyerEmail = None
    # 买家支付宝账号对应的支付宝唯一用户号。
    #  以2088开头的纯16位数字。
    buyerId = None
    # 描述多渠道收单的渠道明细信息，json格式，具体请参见“4.5 渠道明细说明”。
    channelParameters = None
    # 订单金额币种。
    #  目前只支持传入156（人民币）。
    #  如果为空，则默认设置为156。
    currency = None
    # 动态ID。
    dynamicId = None
    # 动态ID类型：
    #  &# 1048698
    #  soundwave：声波
    #  &# 1048698
    #  qrcode：二维码
    #  &# 1048698
    #  barcode：条码
    #  &# 1048698
    #  wave_code：声波，等同soundwave
    #  &# 1048698
    #  qr_code：二维码，等同qrcode
    #  &# 1048698
    #  bar_code：条码，等同barcode
    #  建议取值wave_code、qr_code、bar_code。
    dynamicIdType = None
    # 用于商户的特定业务信息的传递，只有商户与支付宝约定了传递此参数且约定了参数含义，此参数才有效。
    #  比如可传递声波支付场景下的门店ID等信息，以json格式传输，具体请参见“4.7 业务扩展参数说明”。
    extendParams = None
    # xml或json
    formatType = None
    # 描述商品明细信息，json格式，具体请参见“4.3 商品明细说明”。
    goodsDetail = None
    # 设置未付款交易的超时时间，一旦超时，该笔交易就会自动被关闭。
    #  取值范围：1m～15d。
    #  m-分钟，h-小时，d-天，1c-当天（无论交易何时创建，都在0点关闭）。
    #  该参数数值不接受小数点，如1.5h，可转换为90m。
    #  该功能需要联系支付宝配置关闭时间。
    itBPay = None
    # 描述预付卡相关的明细信息，json格式，具体请参见“4.8 预付卡明细参数说明”。
    mcardParameters = None
    # 卖家的操作员ID。
    operatorId = None
    # 操作员的类型：
    #  &# 1048698
    #  0：支付宝操作员
    #  &# 1048698
    #  1：商户的操作员
    #  如果传入其它值或者为空，则默认设置为1。
    operatorType = None
    # 支付宝合作商户网站唯一订单号。
    outTradeNo = None
    # 订单中商品的单价。
    # 如果请求时传入本参数，则必须满足total_fee=price×quantity的条件。
    price = None
    # 订单中商品的数量。
    # 如果请求时传入本参数，则必须满足total_fee=price×quantity的条件。
    quantity = None
    # 业务关联ID集合，用于放置商户的订单号、支付流水号等信息，json格式，具体请参见“4.6 业务关联ID集合说明”。
    refIds = None
    # 描述分账明细信息，json格式，具体请参见“4.4 分账明细说明”。
    royaltyParameters = None
    # 卖家的分账类型，目前只支持传入ROYALTY（普通分账类型）。
    royaltyType = None
    # 卖家支付宝账号，可以为email或者手机号。
    # 如果seller_id不为空，则以seller_id的值作为卖家账号，忽略本参数。
    sellerEmail = None
    # 卖家支付宝账号对应的支付宝唯一用户号。
    # 以2088开头的纯16位数字。
    # 如果和seller_email同时为空，则本参数默认填充partner的值。
    sellerId = None
    # 收银台页面上，商品展示的超链接。
    showUrl = None
    # 商品的标题/交易标题/订单标题/订单关键字等。
    # 该参数最长为128个汉字。
    subject = None
    # 该笔订单的资金总额，取值范围[0.01,100000000]，精确到小数点后2位。
    totalFee = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAlipayCaRequest(self, alipayCaRequest):
        self.alipayCaRequest = alipayCaRequest
        self.apiParas["alipay_ca_request"] = alipayCaRequest

    def getAlipayCaRequest(self):
        return self.alipayCaRequest

    def setBody(self, body):
        self.body = body
        self.apiParas["body"] = body

    def getBody(self):
        return self.body

    def setBuyerEmail(self, buyerEmail):
        self.buyerEmail = buyerEmail
        self.apiParas["buyer_email"] = buyerEmail

    def getBuyerEmail(self):
        return self.buyerEmail

    def setBuyerId(self, buyerId):
        self.buyerId = buyerId
        self.apiParas["buyer_id"] = buyerId

    def getBuyerId(self):
        return self.buyerId

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

    def setDynamicId(self, dynamicId):
        self.dynamicId = dynamicId
        self.apiParas["dynamic_id"] = dynamicId

    def getDynamicId(self):
        return self.dynamicId

    def setDynamicIdType(self, dynamicIdType):
        self.dynamicIdType = dynamicIdType
        self.apiParas["dynamic_id_type"] = dynamicIdType

    def getDynamicIdType(self):
        return self.dynamicIdType

    def setExtendParams(self, extendParams):
        self.extendParams = extendParams
        self.apiParas["extend_params"] = extendParams

    def getExtendParams(self):
        return self.extendParams

    def setFormatType(self, formatType):
        self.formatType = formatType
        self.apiParas["format_type"] = formatType

    def getFormatType(self):
        return self.formatType

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

    def setMcardParameters(self, mcardParameters):
        self.mcardParameters = mcardParameters
        self.apiParas["mcard_parameters"] = mcardParameters

    def getMcardParameters(self):
        return self.mcardParameters

    def setOperatorId(self, operatorId):
        self.operatorId = operatorId
        self.apiParas["operator_id"] = operatorId

    def getOperatorId(self):
        return self.operatorId

    def setOperatorType(self, operatorType):
        self.operatorType = operatorType
        self.apiParas["operator_type"] = operatorType

    def getOperatorType(self):
        return self.operatorType

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

    def setRefIds(self, refIds):
        self.refIds = refIds
        self.apiParas["ref_ids"] = refIds

    def getRefIds(self):
        return self.refIds

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
        return "alipay.acquire.createandpay"

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
