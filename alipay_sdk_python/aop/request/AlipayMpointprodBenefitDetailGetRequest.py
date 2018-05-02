# ALIPAY API: alipay.mpointprod.benefit.detail.get request
#
# @author auto create
# @since 1.0, 2015-01-29 15:46:36
class AlipayMpointprodBenefitDetailGetRequest:

    # 消息体内容，JSON格式，不含换行、空格
    # 参数:
    # userId: 支付用户ID, 可以直接传递openId
    # benefitType: 权益类型, 支持(MemberGrade: 会员等级)
    # benefitStatus: 状态只支持(VALID:生效、WAIT: 待生效、INVALID: 失效), 默认: 全部
    bizContent = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBizContent(self, bizContent):
        self.bizContent = bizContent
        self.apiParas["biz_content"] = bizContent

    def getBizContent(self):
        return self.bizContent

    def getApiMethodName(self):
        return "alipay.mpointprod.benefit.detail.get"

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
