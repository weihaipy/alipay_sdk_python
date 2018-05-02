# ALIPAY API: alipay.member.coupon.querylist request
#
# @author auto create
# @since 1.0, 2017-04-14 11:46:40
class AlipayMemberCouponQuerylistRequest:
    # 红包发放者商户信息，json格式。商户可以传自己的PID，平台商可以传其它商户的PID用于查询指定商户的信息
    # 目前仅支持如下key：
    # unique：商户唯一标识
    # unique_type：支持以下1种取值。
    # PID：商户所在平台商的partner
    # id[唯一]
    merchantInfo = None

    # 翻页页码：翻页查询时使用，表明当前要查询第几页，若page_size为0，则此字段不生效
    pageNo = None

    # 翻页每页条数：翻页查询时使用，表明每页返回的记录数量，范围为1至20；为空或者为0时表示不使用翻页查询，返回所有数量
    pageSize = None

    # 优惠券状态列表，如果指定则只返回指定状态的优惠券.
    # 目前状态主要有以下几种：
    # VALID：可使用
    # WRITED_OFF：已核销,
    # EXPIRED：已过期
    # CLOSED：已关闭
    # 注意：
    # 多个状态以逗号隔开
    status = None

    # 劵所有者买家用户信息，必须是支付宝的用户，json格式。
    # 目前仅支持如下key：
    # unique：用户唯一标识
    # unique_type：支持以下1种取值。
    # UID：用户支付宝账户的唯一ID
    # OPENID：用户支付宝账户在某商户下的唯一ID
    userInfo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setMerchantInfo(self, merchantInfo):
        self.merchantInfo = merchantInfo
        self.apiParas["merchant_info"] = merchantInfo

    def getMerchantInfo(self):
        return self.merchantInfo

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

    def setStatus(self, status):
        self.status = status
        self.apiParas["status"] = status

    def getStatus(self):
        return self.status

    def setUserInfo(self, userInfo):
        self.userInfo = userInfo
        self.apiParas["user_info"] = userInfo

    def getUserInfo(self):
        return self.userInfo

    def getApiMethodName(self):
        return "alipay.member.coupon.querylist"

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
