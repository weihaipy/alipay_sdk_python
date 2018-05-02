
 # ALIPAY API: alipay.ecapiprod.drawndn.paymentschedule.get request
 #
 # @author auto create
 # @since 1.0, 2016-03-29 11:34:20
class AlipayEcapiprodDrawndnPaymentscheduleGetRequest:

    # 支用编号
    drawndnNo = None

    # 身份证
    entityCode = None

    # 客户姓名
    entityName = None

    # 融资平台分配给ISV的编码
    isvCode = None

    # 融资平台分配给小贷公司的机构编码
    orgCode = None
    apiParas = {}
    terminalType=None
    terminalInfo=None
    prodCode=None
    apiVersion="1.0"
    notifyUrl=None
    returnUrl=None
    needEncrypt=False

    def setDrawndnNo(self, drawndnNo):
        self.drawndnNo = drawndnNo
        self.apiParas["drawndn_no"] = drawndnNo

    def getDrawndnNo(self):
        return self.drawndnNo

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

    def getApiMethodName(self):
        return "alipay.ecapiprod.drawndn.paymentschedule.get"

    def setNotifyUrl(self, notifyUrl):
        self.notifyUrl=notifyUrl

    def getNotifyUrl(self):
        return self.notifyUrl

    def setReturnUrl(self, returnUrl):
        self.returnUrl=returnUrl

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
        self.apiVersion=apiVersion

    def getApiVersion(self):
        return self.apiVersion

    def setNeedEncrypt(self, needEncrypt):

       self.needEncrypt=needEncrypt

    def getNeedEncrypt(self):
                   return self.needEncrypt

