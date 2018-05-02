# ALIPAY API: alipay.zdatafront.common.query request
# 
# @author auto create
# @since 1.0, 2018-03-21 11:14:39
class AlipayZdatafrontCommonQueryRequest:
    # 如果cacheInterval<=0,就直接从外部获取数据；
    # 如果cacheInterval>0,就先判断cache中的数据是否过期，如果没有过期就返回cache中的数据，如果过期再从外部获取数据并刷新cache，然后返回数据。
    # 单位：秒
    cacheInterval = None
    # 通用查询的入参
    queryConditions = None
    # 服务名称请与相关开发负责人联系
    serviceName = None
    # 访问该服务的业务
    visitBiz = None
    # 访问该服务的业务线
    visitBizLine = None
    # 访问该服务的部门名称
    visitDomain = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setCacheInterval(self, cacheInterval):
        self.cacheInterval = cacheInterval
        self.apiParas["cache_interval"] = cacheInterval

    def getCacheInterval(self):
        return self.cacheInterval

    def setQueryConditions(self, queryConditions):
        self.queryConditions = queryConditions
        self.apiParas["query_conditions"] = queryConditions

    def getQueryConditions(self):
        return self.queryConditions

    def setServiceName(self, serviceName):
        self.serviceName = serviceName
        self.apiParas["service_name"] = serviceName

    def getServiceName(self):
        return self.serviceName

    def setVisitBiz(self, visitBiz):
        self.visitBiz = visitBiz
        self.apiParas["visit_biz"] = visitBiz

    def getVisitBiz(self):
        return self.visitBiz

    def setVisitBizLine(self, visitBizLine):
        self.visitBizLine = visitBizLine
        self.apiParas["visit_biz_line"] = visitBizLine

    def getVisitBizLine(self):
        return self.visitBizLine

    def setVisitDomain(self, visitDomain):
        self.visitDomain = visitDomain
        self.apiParas["visit_domain"] = visitDomain

    def getVisitDomain(self):
        return self.visitDomain

    def getApiMethodName(self):
        return "alipay.zdatafront.common.query"

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
