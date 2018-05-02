# ALIPAY API: alipay.security.risk.detect request
#
# @author auto create
# @since 1.0, 2016-03-04 14:55:25
class AlipaySecurityRiskDetectRequest:
    # 买家账户编号
    buyerAccountNo = None

    # 买家绑定银行卡号
    buyerBindBankcard = None

    # 买家绑定银行卡的卡类型
    buyerBindBankcardType = None

    # 买家绑定手机号
    buyerBindMobile = None

    # 买家账户在商家的等级，范围：VIP（高级买家）, NORMAL(普通买家）。为空默认NORMAL
    buyerGrade = None

    # 买家证件号码
    buyerIdentityNo = None

    # 买家证件类型
    buyerIdentityType = None

    # 买家真实姓名
    buyerRealName = None

    # 买家注册时间
    buyerRegDate = None

    # 买家注册时留的Email
    buyerRegEmail = None

    # 买家注册手机号
    buyerRegMobile = None

    # 买家业务处理时使用的银行卡号
    buyerSceneBankcard = None

    # 买家业务处理时使用的银行卡类型
    buyerSceneBankcardType = None

    # 买家业务处理时使用的邮箱
    buyerSceneEmail = None

    # 买家业务处理时使用的手机号
    buyerSceneMobile = None

    # 币种
    currency = None

    # 客户端的基带版本
    envClientBaseBand = None

    # 客户端连接的基站信息,格式为：CELLID^LAC
    envClientBaseStation = None

    # 客户端的经纬度坐标,格式为：精度^维度
    envClientCoordinates = None

    # 操作的客户端的imei
    envClientImei = None

    # 操作的客户端IMSI识别码
    envClientImsi = None

    # IOS设备的UDID
    envClientIosUdid = None

    # 操作的客户端ip
    envClientIp = None

    # 操作的客户端mac
    envClientMac = None

    # 操作的客户端分辨率，格式为：水平像素^垂直像素；如：800^600
    envClientScreen = None

    # 客户端设备的统一识别码UUID
    envClientUuid = None

    # 订单产品数量，购买产品的数量（不可为小数）
    itemQuantity = None

    # 订单产品单价，取值范围为[0.01,100000000.00]，精确到小数点后两位。 curren...
    itemUnitPrice = None

    # JS SDK生成的 tokenID
    jsTokenId = None

    # 订单总金额，取值范围为[0.01,100000000.00]，精确到小数点后两位。
    orderAmount = None

    # 订单商品所在类目
    orderCategory = None

    # 订单下单时间
    orderCredateTime = None

    # 订单商品所在城市
    orderItemCity = None

    # 订单产品名称
    orderItemName = None

    # 商户订单唯一标识号
    orderNo = None

    # 签约的支付宝账号对应的支付宝唯一用户号
    partnerId = None

    # 订单收货人地址
    receiverAddress = None

    # 订单收货人地址城市
    receiverCity = None

    # 订单收货人地址所在区
    receiverDistrict = None

    # 订单收货人邮箱
    receiverEmail = None

    # 订单收货人手机
    receiverMobile = None

    # 订单收货人姓名
    receiverName = None

    # 订单收货人地址省份
    receiverState = None

    # 订单收货人地址邮编
    receiverZip = None

    # 场景编码
    sceneCode = None

    # 卖家账户编号
    sellerAccountNo = None

    # 卖家绑定银行卡号
    sellerBindBankcard = None

    # 卖家绑定的银行卡的卡类型
    sellerBindBankcardType = None

    # 卖家绑定手机号
    sellerBindMobile = None

    # 卖家证件号码
    sellerIdentityNo = None

    # 卖家证件类型
    sellerIdentityType = None

    # 卖家真实姓名
    sellerRealName = None

    # 卖家注册时间,格式为：yyyy-MM-dd。
    sellerRegDate = None

    # 卖家注册Email
    sellerRegEmail = None

    # 卖家注册手机号
    sellerRegMoile = None

    # 订单物流方式
    transportType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBuyerAccountNo(self, buyerAccountNo):
        self.buyerAccountNo = buyerAccountNo
        self.apiParas["buyer_account_no"] = buyerAccountNo

    def getBuyerAccountNo(self):
        return self.buyerAccountNo

    def setBuyerBindBankcard(self, buyerBindBankcard):
        self.buyerBindBankcard = buyerBindBankcard
        self.apiParas["buyer_bind_bankcard"] = buyerBindBankcard

    def getBuyerBindBankcard(self):
        return self.buyerBindBankcard

    def setBuyerBindBankcardType(self, buyerBindBankcardType):
        self.buyerBindBankcardType = buyerBindBankcardType
        self.apiParas["buyer_bind_bankcard_type"] = buyerBindBankcardType

    def getBuyerBindBankcardType(self):
        return self.buyerBindBankcardType

    def setBuyerBindMobile(self, buyerBindMobile):
        self.buyerBindMobile = buyerBindMobile
        self.apiParas["buyer_bind_mobile"] = buyerBindMobile

    def getBuyerBindMobile(self):
        return self.buyerBindMobile

    def setBuyerGrade(self, buyerGrade):
        self.buyerGrade = buyerGrade
        self.apiParas["buyer_grade"] = buyerGrade

    def getBuyerGrade(self):
        return self.buyerGrade

    def setBuyerIdentityNo(self, buyerIdentityNo):
        self.buyerIdentityNo = buyerIdentityNo
        self.apiParas["buyer_identity_no"] = buyerIdentityNo

    def getBuyerIdentityNo(self):
        return self.buyerIdentityNo

    def setBuyerIdentityType(self, buyerIdentityType):
        self.buyerIdentityType = buyerIdentityType
        self.apiParas["buyer_identity_type"] = buyerIdentityType

    def getBuyerIdentityType(self):
        return self.buyerIdentityType

    def setBuyerRealName(self, buyerRealName):
        self.buyerRealName = buyerRealName
        self.apiParas["buyer_real_name"] = buyerRealName

    def getBuyerRealName(self):
        return self.buyerRealName

    def setBuyerRegDate(self, buyerRegDate):
        self.buyerRegDate = buyerRegDate
        self.apiParas["buyer_reg_date"] = buyerRegDate

    def getBuyerRegDate(self):
        return self.buyerRegDate

    def setBuyerRegEmail(self, buyerRegEmail):
        self.buyerRegEmail = buyerRegEmail
        self.apiParas["buyer_reg_email"] = buyerRegEmail

    def getBuyerRegEmail(self):
        return self.buyerRegEmail

    def setBuyerRegMobile(self, buyerRegMobile):
        self.buyerRegMobile = buyerRegMobile
        self.apiParas["buyer_reg_mobile"] = buyerRegMobile

    def getBuyerRegMobile(self):
        return self.buyerRegMobile

    def setBuyerSceneBankcard(self, buyerSceneBankcard):
        self.buyerSceneBankcard = buyerSceneBankcard
        self.apiParas["buyer_scene_bankcard"] = buyerSceneBankcard

    def getBuyerSceneBankcard(self):
        return self.buyerSceneBankcard

    def setBuyerSceneBankcardType(self, buyerSceneBankcardType):
        self.buyerSceneBankcardType = buyerSceneBankcardType
        self.apiParas["buyer_scene_bankcard_type"] = buyerSceneBankcardType

    def getBuyerSceneBankcardType(self):
        return self.buyerSceneBankcardType

    def setBuyerSceneEmail(self, buyerSceneEmail):
        self.buyerSceneEmail = buyerSceneEmail
        self.apiParas["buyer_scene_email"] = buyerSceneEmail

    def getBuyerSceneEmail(self):
        return self.buyerSceneEmail

    def setBuyerSceneMobile(self, buyerSceneMobile):
        self.buyerSceneMobile = buyerSceneMobile
        self.apiParas["buyer_scene_mobile"] = buyerSceneMobile

    def getBuyerSceneMobile(self):
        return self.buyerSceneMobile

    def setCurrency(self, currency):
        self.currency = currency
        self.apiParas["currency"] = currency

    def getCurrency(self):
        return self.currency

    def setEnvClientBaseBand(self, envClientBaseBand):
        self.envClientBaseBand = envClientBaseBand
        self.apiParas["env_client_base_band"] = envClientBaseBand

    def getEnvClientBaseBand(self):
        return self.envClientBaseBand

    def setEnvClientBaseStation(self, envClientBaseStation):
        self.envClientBaseStation = envClientBaseStation
        self.apiParas["env_client_base_station"] = envClientBaseStation

    def getEnvClientBaseStation(self):
        return self.envClientBaseStation

    def setEnvClientCoordinates(self, envClientCoordinates):
        self.envClientCoordinates = envClientCoordinates
        self.apiParas["env_client_coordinates"] = envClientCoordinates

    def getEnvClientCoordinates(self):
        return self.envClientCoordinates

    def setEnvClientImei(self, envClientImei):
        self.envClientImei = envClientImei
        self.apiParas["env_client_imei"] = envClientImei

    def getEnvClientImei(self):
        return self.envClientImei

    def setEnvClientImsi(self, envClientImsi):
        self.envClientImsi = envClientImsi
        self.apiParas["env_client_imsi"] = envClientImsi

    def getEnvClientImsi(self):
        return self.envClientImsi

    def setEnvClientIosUdid(self, envClientIosUdid):
        self.envClientIosUdid = envClientIosUdid
        self.apiParas["env_client_ios_udid"] = envClientIosUdid

    def getEnvClientIosUdid(self):
        return self.envClientIosUdid

    def setEnvClientIp(self, envClientIp):
        self.envClientIp = envClientIp
        self.apiParas["env_client_ip"] = envClientIp

    def getEnvClientIp(self):
        return self.envClientIp

    def setEnvClientMac(self, envClientMac):
        self.envClientMac = envClientMac
        self.apiParas["env_client_mac"] = envClientMac

    def getEnvClientMac(self):
        return self.envClientMac

    def setEnvClientScreen(self, envClientScreen):
        self.envClientScreen = envClientScreen
        self.apiParas["env_client_screen"] = envClientScreen

    def getEnvClientScreen(self):
        return self.envClientScreen

    def setEnvClientUuid(self, envClientUuid):
        self.envClientUuid = envClientUuid
        self.apiParas["env_client_uuid"] = envClientUuid

    def getEnvClientUuid(self):
        return self.envClientUuid

    def setItemQuantity(self, itemQuantity):
        self.itemQuantity = itemQuantity
        self.apiParas["item_quantity"] = itemQuantity

    def getItemQuantity(self):
        return self.itemQuantity

    def setItemUnitPrice(self, itemUnitPrice):
        self.itemUnitPrice = itemUnitPrice
        self.apiParas["item_unit_price"] = itemUnitPrice

    def getItemUnitPrice(self):
        return self.itemUnitPrice

    def setJsTokenId(self, jsTokenId):
        self.jsTokenId = jsTokenId
        self.apiParas["js_token_id"] = jsTokenId

    def getJsTokenId(self):
        return self.jsTokenId

    def setOrderAmount(self, orderAmount):
        self.orderAmount = orderAmount
        self.apiParas["order_amount"] = orderAmount

    def getOrderAmount(self):
        return self.orderAmount

    def setOrderCategory(self, orderCategory):
        self.orderCategory = orderCategory
        self.apiParas["order_category"] = orderCategory

    def getOrderCategory(self):
        return self.orderCategory

    def setOrderCredateTime(self, orderCredateTime):
        self.orderCredateTime = orderCredateTime
        self.apiParas["order_credate_time"] = orderCredateTime

    def getOrderCredateTime(self):
        return self.orderCredateTime

    def setOrderItemCity(self, orderItemCity):
        self.orderItemCity = orderItemCity
        self.apiParas["order_item_city"] = orderItemCity

    def getOrderItemCity(self):
        return self.orderItemCity

    def setOrderItemName(self, orderItemName):
        self.orderItemName = orderItemName
        self.apiParas["order_item_name"] = orderItemName

    def getOrderItemName(self):
        return self.orderItemName

    def setOrderNo(self, orderNo):
        self.orderNo = orderNo
        self.apiParas["order_no"] = orderNo

    def getOrderNo(self):
        return self.orderNo

    def setPartnerId(self, partnerId):
        self.partnerId = partnerId
        self.apiParas["partner_id"] = partnerId

    def getPartnerId(self):
        return self.partnerId

    def setReceiverAddress(self, receiverAddress):
        self.receiverAddress = receiverAddress
        self.apiParas["receiver_address"] = receiverAddress

    def getReceiverAddress(self):
        return self.receiverAddress

    def setReceiverCity(self, receiverCity):
        self.receiverCity = receiverCity
        self.apiParas["receiver_city"] = receiverCity

    def getReceiverCity(self):
        return self.receiverCity

    def setReceiverDistrict(self, receiverDistrict):
        self.receiverDistrict = receiverDistrict
        self.apiParas["receiver_district"] = receiverDistrict

    def getReceiverDistrict(self):
        return self.receiverDistrict

    def setReceiverEmail(self, receiverEmail):
        self.receiverEmail = receiverEmail
        self.apiParas["receiver_email"] = receiverEmail

    def getReceiverEmail(self):
        return self.receiverEmail

    def setReceiverMobile(self, receiverMobile):
        self.receiverMobile = receiverMobile
        self.apiParas["receiver_mobile"] = receiverMobile

    def getReceiverMobile(self):
        return self.receiverMobile

    def setReceiverName(self, receiverName):
        self.receiverName = receiverName
        self.apiParas["receiver_name"] = receiverName

    def getReceiverName(self):
        return self.receiverName

    def setReceiverState(self, receiverState):
        self.receiverState = receiverState
        self.apiParas["receiver_state"] = receiverState

    def getReceiverState(self):
        return self.receiverState

    def setReceiverZip(self, receiverZip):
        self.receiverZip = receiverZip
        self.apiParas["receiver_zip"] = receiverZip

    def getReceiverZip(self):
        return self.receiverZip

    def setSceneCode(self, sceneCode):
        self.sceneCode = sceneCode
        self.apiParas["scene_code"] = sceneCode

    def getSceneCode(self):
        return self.sceneCode

    def setSellerAccountNo(self, sellerAccountNo):
        self.sellerAccountNo = sellerAccountNo
        self.apiParas["seller_account_no"] = sellerAccountNo

    def getSellerAccountNo(self):
        return self.sellerAccountNo

    def setSellerBindBankcard(self, sellerBindBankcard):
        self.sellerBindBankcard = sellerBindBankcard
        self.apiParas["seller_bind_bankcard"] = sellerBindBankcard

    def getSellerBindBankcard(self):
        return self.sellerBindBankcard

    def setSellerBindBankcardType(self, sellerBindBankcardType):
        self.sellerBindBankcardType = sellerBindBankcardType
        self.apiParas["seller_bind_bankcard_type"] = sellerBindBankcardType

    def getSellerBindBankcardType(self):
        return self.sellerBindBankcardType

    def setSellerBindMobile(self, sellerBindMobile):
        self.sellerBindMobile = sellerBindMobile
        self.apiParas["seller_bind_mobile"] = sellerBindMobile

    def getSellerBindMobile(self):
        return self.sellerBindMobile

    def setSellerIdentityNo(self, sellerIdentityNo):
        self.sellerIdentityNo = sellerIdentityNo
        self.apiParas["seller_identity_no"] = sellerIdentityNo

    def getSellerIdentityNo(self):
        return self.sellerIdentityNo

    def setSellerIdentityType(self, sellerIdentityType):
        self.sellerIdentityType = sellerIdentityType
        self.apiParas["seller_identity_type"] = sellerIdentityType

    def getSellerIdentityType(self):
        return self.sellerIdentityType

    def setSellerRealName(self, sellerRealName):
        self.sellerRealName = sellerRealName
        self.apiParas["seller_real_name"] = sellerRealName

    def getSellerRealName(self):
        return self.sellerRealName

    def setSellerRegDate(self, sellerRegDate):
        self.sellerRegDate = sellerRegDate
        self.apiParas["seller_reg_date"] = sellerRegDate

    def getSellerRegDate(self):
        return self.sellerRegDate

    def setSellerRegEmail(self, sellerRegEmail):
        self.sellerRegEmail = sellerRegEmail
        self.apiParas["seller_reg_email"] = sellerRegEmail

    def getSellerRegEmail(self):
        return self.sellerRegEmail

    def setSellerRegMoile(self, sellerRegMoile):
        self.sellerRegMoile = sellerRegMoile
        self.apiParas["seller_reg_moile"] = sellerRegMoile

    def getSellerRegMoile(self):
        return self.sellerRegMoile

    def setTransportType(self, transportType):
        self.transportType = transportType
        self.apiParas["transport_type"] = transportType

    def getTransportType(self):
        return self.transportType

    def getApiMethodName(self):
        return "alipay.security.risk.detect"

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
