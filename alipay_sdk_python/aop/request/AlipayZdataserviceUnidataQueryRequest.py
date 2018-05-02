# ALIPAY API: alipay.zdataservice.unidata.query request
#
# @author auto create
# @since 1.0, 2017-04-26 16:20:03
class AlipayZdataserviceUnidataQueryRequest:
    # 通用的查询入参
    queryCondition = None
    # 返回数据的类型，内部业务系统分配
    uniqKey = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setQueryCondition(self, queryCondition):
        self.queryCondition = queryCondition
        self.apiParas["query_condition"] = queryCondition

    def getQueryCondition(self):
        return self.queryCondition

    def setUniqKey(self, uniqKey):
        self.uniqKey = uniqKey
        self.apiParas["uniq_key"] = uniqKey

    def getUniqKey(self):
        return self.uniqKey

    def getApiMethodName(self):
        return "alipay.zdataservice.unidata.query"

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
