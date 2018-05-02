# ALIPAY API: alipay.pass.tpl.content.add request
#
# @author auto create
# @since 1.0, 2017-12-07 16:32:21
class AlipayPassTplContentAddRequest:
    # 支付宝用户识别信息：
    # 当 recognition_type=1时， recognition_info=“partner_id”:”2088102114633762”,“out_trade_no”:”1234567”；
    # 当recognition_type=3时，recognition_info=“mobile”:”136XXXXXXXX“
    # 当recognition_type=4时， recognition_info=“open_id”:”afbd8d9bb12fc02c5094d8ea89d1fae8“
    recognitionInfo = None
    # Alipass添加对象识别类型【1--订单信息3--支付宝用户绑定手机号；4--支付宝OpenId】
    recognitionType = None
    # 支付宝pass模版ID
    tplId = None
    # 模版动态参数信息【支付宝pass模版参数键值对JSON字符串】
    tplParams = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setRecognitionInfo(self, recognitionInfo):
        self.recognitionInfo = recognitionInfo
        self.apiParas["recognition_info"] = recognitionInfo

    def getRecognitionInfo(self):
        return self.recognitionInfo

    def setRecognitionType(self, recognitionType):
        self.recognitionType = recognitionType
        self.apiParas["recognition_type"] = recognitionType

    def getRecognitionType(self):
        return self.recognitionType

    def setTplId(self, tplId):
        self.tplId = tplId
        self.apiParas["tpl_id"] = tplId

    def getTplId(self):
        return self.tplId

    def setTplParams(self, tplParams):
        self.tplParams = tplParams
        self.apiParas["tpl_params"] = tplParams

    def getTplParams(self):
        return self.tplParams

    def getApiMethodName(self):
        return "alipay.pass.tpl.content.add"

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
