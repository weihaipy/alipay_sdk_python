# ALIPAY API: alipay.pass.tpl.content.update request
#
# @author auto create
# @since 1.0, 2017-12-07 16:33:36
class AlipayPassTplContentUpdateRequest:
    # 代理商代替商户发放卡券后，再代替商户更新卡券时，此值为商户的pid/appid
    channelId = None
    # 支付宝pass唯一标识
    serialNumber = None
    # 券状态,支持更新为USED,CLOSED两种状态
    status = None
    # 模版动态参数信息【支付宝pass模版参数键值对JSON字符串】
    tplParams = None
    # 核销码串值【当状态变更为USED时，建议传入】
    verifyCode = None
    # 核销方式，目前支持：wave（声波方式）、qrcode（二维码方式）、barcode（条码方式）、input（文本方式，即手工输入方式）。pass和verify_type不能同时为空
    verifyType = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False
    def setChannelId(self, channelId):
        self.channelId = channelId
        self.apiParas["channel_id"] = channelId
    def getChannelId(self):
        return self.channelId
    def setSerialNumber(self, serialNumber):
        self.serialNumber = serialNumber
        self.apiParas["serial_number"] = serialNumber
    def getSerialNumber(self):
        return self.serialNumber
    def setStatus(self, status):
        self.status = status
        self.apiParas["status"] = status
    def getStatus(self):
        return self.status
    def setTplParams(self, tplParams):
        self.tplParams = tplParams
        self.apiParas["tpl_params"] = tplParams
    def getTplParams(self):
        return self.tplParams
    def setVerifyCode(self, verifyCode):
        self.verifyCode = verifyCode
        self.apiParas["verify_code"] = verifyCode
    def getVerifyCode(self):
        return self.verifyCode
    def setVerifyType(self, verifyType):
        self.verifyType = verifyType
        self.apiParas["verify_type"] = verifyType
    def getVerifyType(self):
        return self.verifyType
    def getApiMethodName(self):
        return "alipay.pass.tpl.content.update"
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
