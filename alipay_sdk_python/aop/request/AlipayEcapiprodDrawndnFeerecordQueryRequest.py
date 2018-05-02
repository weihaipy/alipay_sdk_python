# ALIPAY API: alipay.ecapiprod.drawndn.feerecord.query request
#
# @author auto create
# @since 1.0, 2016-03-29 11:34:27
class AlipayEcapiprodDrawndnFeerecordQueryRequest:
    # 支用编号
    drawndnNo = None
    # 费用还款记录的终止时间，终止时间与起始时间的范围不能超过31天
    end = None
    # 客户身份证号码，为18位，最后X必须为大写
    entityCode = None
    # 客户姓名
    entityName = None
    # 融资平台分配给ISV的编码
    isvCode = None
    # 融资平台分配给小贷公司的机构编码
    orgCode = None
    # 费用还款记录的起始时间（距离当前时间不能大于183天，只能在【0-183】之间）
    start = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setDrawndnNo(self, drawndnNo):
        self.drawndnNo = drawndnNo
        self.apiParas["drawndn_no"] = drawndnNo

    def getDrawndnNo(self):
        return self.drawndnNo

    def setEnd(self, end):
        self.end = end
        self.apiParas["end"] = end

    def getEnd(self):
        return self.end

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

    def setIsvCode(self, isvCode):
        self.isvCode = isvCode
        self.apiParas["isv_code"] = isvCode

    def getIsvCode(self):
        return self.isvCode

    def setOrgCode(self, orgCode):
        self.orgCode = orgCode
        self.apiParas["org_code"] = orgCode

    def getOrgCode(self):
        return self.orgCode

    def setStart(self, start):
        self.start = start
        self.apiParas["start"] = start

    def getStart(self):
        return self.start

    def getApiMethodName(self):
        return "alipay.ecapiprod.drawndn.feerecord.query"

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
