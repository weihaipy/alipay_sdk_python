# ALIPAY API: alipay.zdatafront.datatransfered.send request
#
# @author auto create
# @since 1.0, 2017-05-18 11:27:33
class AlipayZdatafrontDatatransferedSendRequest:
    # 数据字段，identity对应的其他数据字段。使用json格式组织，且仅支持字符串类型，其他类型请转为字符串。
    data = None
    # 合作伙伴的主键数据，同一合作伙伴要保证该字段唯一，若出现重复，后入数据会覆盖先入数据。使用json格式组织，且仅支持字符串类型，其他类型请转为字符串。
    identity = None
    # 合作伙伴标识字段，用来区分数据来源。建议使用公司域名或公司名。
    typeId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setData(self, data):
        self.data = data
        self.apiParas["data"] = data

    def getData(self):
        return self.data

    def setIdentity(self, identity):
        self.identity = identity
        self.apiParas["identity"] = identity

    def getIdentity(self):
        return self.identity

    def setTypeId(self, typeId):
        self.typeId = typeId
        self.apiParas["type_id"] = typeId

    def getTypeId(self):
        return self.typeId

    def getApiMethodName(self):
        return "alipay.zdatafront.datatransfered.send"

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
