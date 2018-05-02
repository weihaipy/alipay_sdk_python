# ALIPAY API: alipay.operator.mobile.bind request
#
# @author auto create
# @since 1.0, 2017-05-03 16:48:39
class AlipayOperatorMobileBindRequest:
    # 标识该运营商是否需要验证用户的手机号绑定过快捷卡
    # 1：需要
    # 0：不需要
    checkSigncard = None
    # 支付宝处理完请求后，如验证失败，当前页面自动跳转到商户网站里指定页面的http路径。
    fReturnUrl = None
    # 标识该运营商是否提供了查询手机归属的spi接口。
    # 1：提供了
    # 0：没提供
    hasSpi = None
    # 标识该运营商名称
    operatorName = None
    # 标识该运营商所在省份
    provinceName = None
    # 支付宝处理完请求后，如验证成功，当前页面自动跳转到商户网站里指定页面的http路径。
    sReturnUrl = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setCheckSigncard(self, checkSigncard):
        self.checkSigncard = checkSigncard
        self.apiParas["check_signcard"] = checkSigncard

    def getCheckSigncard(self):
        return self.checkSigncard

    def setfReturnUrl(self, fReturnUrl):
        self.fReturnUrl = fReturnUrl
        self.apiParas["f_return_url"] = fReturnUrl

    def getfReturnUrl(self):
        return self.fReturnUrl

    def setHasSpi(self, hasSpi):
        self.hasSpi = hasSpi
        self.apiParas["has_spi"] = hasSpi

    def getHasSpi(self):
        return self.hasSpi

    def setOperatorName(self, operatorName):
        self.operatorName = operatorName
        self.apiParas["operator_name"] = operatorName

    def getOperatorName(self):
        return self.operatorName

    def setProvinceName(self, provinceName):
        self.provinceName = provinceName
        self.apiParas["province_name"] = provinceName

    def getProvinceName(self):
        return self.provinceName

    def setsReturnUrl(self, sReturnUrl):
        self.sReturnUrl = sReturnUrl
        self.apiParas["s_return_url"] = sReturnUrl

    def getsReturnUrl(self):
        return self.sReturnUrl

    def getApiMethodName(self):
        return "alipay.operator.mobile.bind"

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
