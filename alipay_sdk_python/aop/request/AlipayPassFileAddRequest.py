# ALIPAY API: alipay.pass.file.add request
#
# @author auto create
# @since 1.0, 2017-12-07 20:13:48
class AlipayPassFileAddRequest:
    # 支付宝pass文件二进制Base64加密字符串
    fileContent = None
    # 支付宝用户识别信息：
    # 当 recognition_type=1时， recognition_info=“partner_id”:”2088102114633762”,“out_trade_no”:”1234567”；
    # 当recognition_type=2时， recognition_info=“user_id”:”2088102114633761“
    # 当recognition_type=3时，recognition_info=“mobile”:”136XXXXXXXX“
    recognitionInfo = None
    # Alipass添加对象识别类型【1--订单信息；2--支付宝userId3--支付宝绑定手机号】
    recognitionType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setFileContent(self, fileContent):
        self.fileContent = fileContent
        self.apiParas["file_content"] = fileContent

    def getFileContent(self):
        return self.fileContent

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

    def getApiMethodName(self):
        return "alipay.pass.file.add"

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
