# ALIPAY API: alipay.mobile.code.create request
#
# @author auto create
# @since 1.0, 2017-02-28 11:13:54
class AlipayMobileCodeCreateRequest:
    # 业务关联ID。比如订单号,userId，业务连接等
    bizLinkedId = None

    # 类似产品名称，根据该值决定码存储类型；新接业务需要找码平台技术配置
    bizType = None

    # 业务自定义,码平台不用理解。一定要传json字符串。
    contextStr = None

    # 如果是True，则扫一扫下发跳转地址直接取自bizLinkedId
    # 否则，从路由信息里取跳转地址
    isDirect = None

    # 备注信息字段
    memo = None

    # 发码来源，业务自定
    sourceId = None

    # 编码启动时间（yyy-MM-dd hh:mm:ss），为空表示立即启用
    startDate = None

    # 超时时间,单位秒；若不传则为永久。发码超时时间需要找码平台技术评估
    timeout = None

    # 支付宝用户id
    userId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBizLinkedId(self, bizLinkedId):
        self.bizLinkedId = bizLinkedId
        self.apiParas["biz_linked_id"] = bizLinkedId

    def getBizLinkedId(self):
        return self.bizLinkedId

    def setBizType(self, bizType):
        self.bizType = bizType
        self.apiParas["biz_type"] = bizType

    def getBizType(self):
        return self.bizType

    def setContextStr(self, contextStr):
        self.contextStr = contextStr
        self.apiParas["context_str"] = contextStr

    def getContextStr(self):
        return self.contextStr

    def setIsDirect(self, isDirect):
        self.isDirect = isDirect
        self.apiParas["is_direct"] = isDirect

    def getIsDirect(self):
        return self.isDirect

    def setMemo(self, memo):
        self.memo = memo
        self.apiParas["memo"] = memo

    def getMemo(self):
        return self.memo

    def setSourceId(self, sourceId):
        self.sourceId = sourceId
        self.apiParas["source_id"] = sourceId

    def getSourceId(self):
        return self.sourceId

    def setStartDate(self, startDate):
        self.startDate = startDate
        self.apiParas["start_date"] = startDate

    def getStartDate(self):
        return self.startDate

    def setTimeout(self, timeout):
        self.timeout = timeout
        self.apiParas["timeout"] = timeout

    def getTimeout(self):
        return self.timeout

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.mobile.code.create"

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
