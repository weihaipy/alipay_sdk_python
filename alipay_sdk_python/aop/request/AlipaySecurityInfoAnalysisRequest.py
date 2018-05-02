# ALIPAY API: alipay.security.info.analysis request
#
# @author auto create
# @since 1.0, 2016-03-04 14:55:20
class AlipaySecurityInfoAnalysisRequest:
    # 客户端的基带版本
    envClientBaseBand = None
    # 客户端连接的基站信息
    envClientBaseStation = None
    # 客户端的经纬度坐标
    envClientCoordinates = None
    # 操作的客户端的imei
    envClientImei = None
    # 操作的客户端的imsi
    envClientImsi = None
    # IOS设备的UDID
    envClientIosUdid = None
    # 操作的客户端ip
    envClientIp = None
    # 操作的客户端mac
    envClientMac = None
    # 操作的客户端分辨率，格式为：水平像素^垂直像素；如：800^600
    envClientScreen = None
    # 客户端设备的统一识别码UUID
    envClientUuid = None
    # JS SDK生成的 tokenID
    jsTokenId = None
    # 签约的支付宝账号对应的支付宝唯一用户号
    partnerId = None
    # 场景编码
    sceneCode = None
    # 卖家账户ID
    userAccountNo = None
    # 用户绑定银行卡号
    userBindBankcard = None
    # 用户绑定银行卡的卡类型
    userBindBankcardType = None
    # 用户绑定手机号
    userBindMobile = None
    # 用户证件类型
    userIdentityType = None
    # 用户真实姓名
    userRealName = None
    # 用户注册时间
    userRegDate = None
    # 用户注册Email
    userRegEmail = None
    # 用户注册手机号
    userRegMobile = None
    # 用户证件号码
    userrIdentityNo = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setEnvClientBaseBand(self, envClientBaseBand):
        self.envClientBaseBand = envClientBaseBand
        self.apiParas["env_client_base_band"] = envClientBaseBand

    def getEnvClientBaseBand(self):
        return self.envClientBaseBand

    def setEnvClientBaseStation(self, envClientBaseStation):
        self.envClientBaseStation = envClientBaseStation
        self.apiParas["env_client_base_station"] = envClientBaseStation

    def getEnvClientBaseStation(self):
        return self.envClientBaseStation

    def setEnvClientCoordinates(self, envClientCoordinates):
        self.envClientCoordinates = envClientCoordinates
        self.apiParas["env_client_coordinates"] = envClientCoordinates

    def getEnvClientCoordinates(self):
        return self.envClientCoordinates

    def setEnvClientImei(self, envClientImei):
        self.envClientImei = envClientImei
        self.apiParas["env_client_imei"] = envClientImei

    def getEnvClientImei(self):
        return self.envClientImei

    def setEnvClientImsi(self, envClientImsi):
        self.envClientImsi = envClientImsi
        self.apiParas["env_client_imsi"] = envClientImsi

    def getEnvClientImsi(self):
        return self.envClientImsi

    def setEnvClientIosUdid(self, envClientIosUdid):
        self.envClientIosUdid = envClientIosUdid
        self.apiParas["env_client_ios_udid"] = envClientIosUdid

    def getEnvClientIosUdid(self):
        return self.envClientIosUdid

    def setEnvClientIp(self, envClientIp):
        self.envClientIp = envClientIp
        self.apiParas["env_client_ip"] = envClientIp

    def getEnvClientIp(self):
        return self.envClientIp

    def setEnvClientMac(self, envClientMac):
        self.envClientMac = envClientMac
        self.apiParas["env_client_mac"] = envClientMac

    def getEnvClientMac(self):
        return self.envClientMac

    def setEnvClientScreen(self, envClientScreen):
        self.envClientScreen = envClientScreen
        self.apiParas["env_client_screen"] = envClientScreen

    def getEnvClientScreen(self):
        return self.envClientScreen

    def setEnvClientUuid(self, envClientUuid):
        self.envClientUuid = envClientUuid
        self.apiParas["env_client_uuid"] = envClientUuid

    def getEnvClientUuid(self):
        return self.envClientUuid

    def setJsTokenId(self, jsTokenId):
        self.jsTokenId = jsTokenId
        self.apiParas["js_token_id"] = jsTokenId

    def getJsTokenId(self):
        return self.jsTokenId

    def setPartnerId(self, partnerId):
        self.partnerId = partnerId
        self.apiParas["partner_id"] = partnerId

    def getPartnerId(self):
        return self.partnerId

    def setSceneCode(self, sceneCode):
        self.sceneCode = sceneCode
        self.apiParas["scene_code"] = sceneCode

    def getSceneCode(self):
        return self.sceneCode

    def setUserAccountNo(self, userAccountNo):
        self.userAccountNo = userAccountNo
        self.apiParas["user_account_no"] = userAccountNo

    def getUserAccountNo(self):
        return self.userAccountNo

    def setUserBindBankcard(self, userBindBankcard):
        self.userBindBankcard = userBindBankcard
        self.apiParas["user_bind_bankcard"] = userBindBankcard

    def getUserBindBankcard(self):
        return self.userBindBankcard

    def setUserBindBankcardType(self, userBindBankcardType):
        self.userBindBankcardType = userBindBankcardType
        self.apiParas["user_bind_bankcard_type"] = userBindBankcardType

    def getUserBindBankcardType(self):
        return self.userBindBankcardType

    def setUserBindMobile(self, userBindMobile):
        self.userBindMobile = userBindMobile
        self.apiParas["user_bind_mobile"] = userBindMobile

    def getUserBindMobile(self):
        return self.userBindMobile

    def setUserIdentityType(self, userIdentityType):
        self.userIdentityType = userIdentityType
        self.apiParas["user_identity_type"] = userIdentityType

    def getUserIdentityType(self):
        return self.userIdentityType

    def setUserRealName(self, userRealName):
        self.userRealName = userRealName
        self.apiParas["user_real_name"] = userRealName

    def getUserRealName(self):
        return self.userRealName

    def setUserRegDate(self, userRegDate):
        self.userRegDate = userRegDate
        self.apiParas["user_reg_date"] = userRegDate

    def getUserRegDate(self):
        return self.userRegDate

    def setUserRegEmail(self, userRegEmail):
        self.userRegEmail = userRegEmail
        self.apiParas["user_reg_email"] = userRegEmail

    def getUserRegEmail(self):
        return self.userRegEmail

    def setUserRegMobile(self, userRegMobile):
        self.userRegMobile = userRegMobile
        self.apiParas["user_reg_mobile"] = userRegMobile

    def getUserRegMobile(self):
        return self.userRegMobile

    def setUserrIdentityNo(self, userrIdentityNo):
        self.userrIdentityNo = userrIdentityNo
        self.apiParas["userr_identity_no"] = userrIdentityNo

    def getUserrIdentityNo(self):
        return self.userrIdentityNo

    def getApiMethodName(self):
        return "alipay.security.info.analysis"

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
