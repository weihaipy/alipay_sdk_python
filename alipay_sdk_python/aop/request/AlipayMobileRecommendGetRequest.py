# ALIPAY API: alipay.mobile.recommend.get request
#
# @author auto create
# @since 1.0, 2015-03-11 15:19:54
class AlipayMobileRecommendGetRequest:
    # 请求上下文扩展信息，需要与接口负责人约定。格式为json对象。
    extInfo = None

    # 期望获取的最多推荐数量, 默认获取一个推荐内容, 0表示获取所有推荐内容
    limit = None

    # 所使用的场景id，请向接口负责人申请
    sceneId = None

    # 获取推荐信息的开始位置, 默认从0开始
    startIdx = None

    # 用户openid
    userId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setExtInfo(self, extInfo):
        self.extInfo = extInfo
        self.apiParas["ext_info"] = extInfo

    def getExtInfo(self):
        return self.extInfo

    def setLimit(self, limit):
        self.limit = limit
        self.apiParas["limit"] = limit

    def getLimit(self):
        return self.limit

    def setSceneId(self, sceneId):
        self.sceneId = sceneId
        self.apiParas["scene_id"] = sceneId

    def getSceneId(self):
        return self.sceneId

    def setStartIdx(self, startIdx):
        self.startIdx = startIdx
        self.apiParas["start_idx"] = startIdx

    def getStartIdx(self):
        return self.startIdx

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.mobile.recommend.get"

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
