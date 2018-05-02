# ALIPAY API: alipay.user.account.search request
# 
# @author auto create
# @since 1.0, 2016-08-11 18:02:23
class AlipayUserAccountSearchRequest:
    # 查询的结束时间
    endTime = None
    # 需要过滤的字符
    fields = None
    # 查询的页数
    pageNo = None
    # 每页的条数
    pageSize = None
    # 查询的开始时间
    startTime = None
    # 查询账务的类型
    type = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setEndTime(self, endTime):
        self.endTime = endTime
        self.apiParas["end_time"] = endTime

    def getEndTime(self):
        return self.endTime

    def setFields(self, fields):
        self.fields = fields
        self.apiParas["fields"] = fields

    def getFields(self):
        return self.fields

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

    def setType(self, type):
        self.type = type
        self.apiParas["type"] = type

    def getType(self):
        return self.type

    def getApiMethodName(self):
        return "alipay.user.account.search"

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
