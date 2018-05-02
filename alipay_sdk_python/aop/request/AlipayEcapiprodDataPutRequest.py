# ALIPAY API: alipay.ecapiprod.data.put request
#
# @author auto create
# @since 1.0, 2015-04-02 16:45:23
class AlipayEcapiprodDataPutRequest:
    # 数据类型
    category = None

    # 数据字符编码，默认UTF-8
    charSet = None

    # 数据采集平台生成的采集任务编号
    collectingTaskId = None

    # 身份证，工商注册号等
    entityCode = None

    # 姓名或公司名等，name和code不能同时为空
    entityName = None

    # 人或公司等
    entityType = None

    # 渠道商
    isvCode = None

    # 数据主体,以json格式传输的数据
    jsonData = None

    # 数据合作方
    orgCode = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setCategory(self, category):
        self.category = category
        self.apiParas["category"] = category

    def getCategory(self):
        return self.category

    def setCharSet(self, charSet):
        self.charSet = charSet
        self.apiParas["char_set"] = charSet

    def getCharSet(self):
        return self.charSet

    def setCollectingTaskId(self, collectingTaskId):
        self.collectingTaskId = collectingTaskId
        self.apiParas["collecting_task_id"] = collectingTaskId

    def getCollectingTaskId(self):
        return self.collectingTaskId

    def setEntityCode(self, entityCode):
        self.entityCode = entityCode
        self.apiParas["entity_code"] = entityCode

    def getEntityCode(self):
        return self.entityCode

    def setEntityName(self, entityName):
        self.entityName = entityName
        self.apiParas["entity_name"] = entityName

    def getEntityName(self):
        return self.entityName

    def setEntityType(self, entityType):
        self.entityType = entityType
        self.apiParas["entity_type"] = entityType

    def getEntityType(self):
        return self.entityType

    def setIsvCode(self, isvCode):
        self.isvCode = isvCode
        self.apiParas["isv_code"] = isvCode

    def getIsvCode(self):
        return self.isvCode

    def setJsonData(self, jsonData):
        self.jsonData = jsonData
        self.apiParas["json_data"] = jsonData

    def getJsonData(self):
        return self.jsonData

    def setOrgCode(self, orgCode):
        self.orgCode = orgCode
        self.apiParas["org_code"] = orgCode

    def getOrgCode(self):
        return self.orgCode

    def getApiMethodName(self):
        return "alipay.ecapiprod.data.put"

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
