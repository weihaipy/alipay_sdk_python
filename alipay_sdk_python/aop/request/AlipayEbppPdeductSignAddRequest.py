# ALIPAY API: alipay.ebpp.pdeduct.sign.add request
#
# @author auto create
# @since 1.0, 2017-10-10 14:30:21
class AlipayEbppPdeductSignAddRequest:
    # 机构签约代扣来源渠道
    # PUBLICPLATFORM：服务窗
    agentChannel = None
    # 从服务窗发起则为publicId的值
    agentCode = None
    # 户号，机构针对于每户的水、电都会有唯一的标识户号
    billKey = None
    # 业务类型。
    # JF：缴水、电、燃气、固话宽带、有线电视、交通罚款费用
    # WUYE：缴物业费
    # HK：信用卡还款
    # TX：手机充值
    bizType = None
    # 支付宝缴费系统中的出账机构ID
    chargeInst = None
    # 签约类型可为空
    deductType = None
    # 扩展字段
    extendField = None
    # 通知方式设置，可为空
    notifyConfig = None
    # 外部产生的协议ID
    outAgreementId = None
    # 户名，户主真实姓名
    ownerName = None
    # 支付工具设置，目前可为空
    payConfig = None
    # 用户签约时，跳转到支付宝独立密码校验页面，校验成功后会将token和对应的用户ID缓存下来，然后跳回到机构页面生成token带回给机构，机构签约时必须传入token
    payPasswordToken = None
    # 商户ID
    pid = None
    # 签约到期时间。空表示无限期，一期固定传空。
    signExpireDate = None
    # 业务子类型。
    # WATER：缴水费
    # ELECTRIC：缴电费
    # GAS：缴燃气费
    # COMMUN：缴固话宽带
    # CATV：缴有线电视费
    # TRAFFIC：缴交通罚款
    # WUYE：缴物业费
    # HK：信用卡还款
    # CZ：手机充值
    subBizType = None
    # 用户ID
    userId = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setAgentChannel(self, agentChannel):
        self.agentChannel = agentChannel
        self.apiParas["agent_channel"] = agentChannel

    def getAgentChannel(self):
        return self.agentChannel

    def setAgentCode(self, agentCode):
        self.agentCode = agentCode
        self.apiParas["agent_code"] = agentCode

    def getAgentCode(self):
        return self.agentCode

    def setBillKey(self, billKey):
        self.billKey = billKey
        self.apiParas["bill_key"] = billKey

    def getBillKey(self):
        return self.billKey

    def setBizType(self, bizType):
        self.bizType = bizType
        self.apiParas["biz_type"] = bizType

    def getBizType(self):
        return self.bizType

    def setChargeInst(self, chargeInst):
        self.chargeInst = chargeInst
        self.apiParas["charge_inst"] = chargeInst

    def getChargeInst(self):
        return self.chargeInst

    def setDeductType(self, deductType):
        self.deductType = deductType
        self.apiParas["deduct_type"] = deductType

    def getDeductType(self):
        return self.deductType

    def setExtendField(self, extendField):
        self.extendField = extendField
        self.apiParas["extend_field"] = extendField

    def getExtendField(self):
        return self.extendField

    def setNotifyConfig(self, notifyConfig):
        self.notifyConfig = notifyConfig
        self.apiParas["notify_config"] = notifyConfig

    def getNotifyConfig(self):
        return self.notifyConfig

    def setOutAgreementId(self, outAgreementId):
        self.outAgreementId = outAgreementId
        self.apiParas["out_agreement_id"] = outAgreementId

    def getOutAgreementId(self):
        return self.outAgreementId

    def setOwnerName(self, ownerName):
        self.ownerName = ownerName
        self.apiParas["owner_name"] = ownerName

    def getOwnerName(self):
        return self.ownerName

    def setPayConfig(self, payConfig):
        self.payConfig = payConfig
        self.apiParas["pay_config"] = payConfig

    def getPayConfig(self):
        return self.payConfig

    def setPayPasswordToken(self, payPasswordToken):
        self.payPasswordToken = payPasswordToken
        self.apiParas["pay_password_token"] = payPasswordToken

    def getPayPasswordToken(self):
        return self.payPasswordToken

    def setPid(self, pid):
        self.pid = pid
        self.apiParas["pid"] = pid

    def getPid(self):
        return self.pid

    def setSignExpireDate(self, signExpireDate):
        self.signExpireDate = signExpireDate
        self.apiParas["sign_expire_date"] = signExpireDate

    def getSignExpireDate(self):
        return self.signExpireDate

    def setSubBizType(self, subBizType):
        self.subBizType = subBizType
        self.apiParas["sub_biz_type"] = subBizType

    def getSubBizType(self):
        return self.subBizType

    def setUserId(self, userId):
        self.userId = userId
        self.apiParas["user_id"] = userId

    def getUserId(self):
        return self.userId

    def getApiMethodName(self):
        return "alipay.ebpp.pdeduct.sign.add"

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
