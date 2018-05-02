# ALIPAY API: alipay.system.oauth.token request
#
# @author auto create
# @since 1.0, 2017-09-25 16:00:34
class AlipaySystemOauthTokenRequest:
    # 授权码，用户对应用授权后得到。
    code = None
    # 值为authorization_code时，代表用code换取；值为refresh_token时，代表用refresh_token换取
    grantType = None
    # 刷新令牌，上次换取访问令牌时得到。见出参的refresh_token字段
    refreshToken = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setCode(self, code):
        self.code = code
        self.apiParas["code"] = code

    def getCode(self):
        return self.code

    def setGrantType(self, grantType):
        self.grantType = grantType
        self.apiParas["grant_type"] = grantType

    def getGrantType(self):
        return self.grantType

    def setRefreshToken(self, refreshToken):
        self.refreshToken = refreshToken
        self.apiParas["refresh_token"] = refreshToken

    def getRefreshToken(self):
        return self.refreshToken

    def getApiMethodName(self):
        return "alipay.system.oauth.token"

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
