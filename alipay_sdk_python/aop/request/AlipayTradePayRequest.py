# ALIPAY API: alipay.trade.pay request
#
# @author auto create
# @since 1.0, 2018-03-23 19:15:33
class AlipayTradePayRequest:


    # 用于在线下场景交易一次创建并支付掉
    # 修改路由策略到R
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
        return "alipay.trade.pay"


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
