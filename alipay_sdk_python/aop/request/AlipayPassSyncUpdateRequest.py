# ALIPAY API: alipay.pass.sync.update request
#
# @author auto create
# @since 1.0, 2017-12-07 20:19:03
"""
修改:
-----
pass 属性修改为 pass_
"""


class AlipayPassSyncUpdateRequest:
    # 代理商代替商户发放卡券后，再代替商户更新卡券时，此值为商户的pid/appid；商户自己发券时，此值为空或者商户appId
    channelId = None
    # 用来传递外部交易号等扩展参数信息，格式为json
    extInfo = None
    # 需要修改的pass信息，可以更新全部pass信息，也可以斤更新某一节点。pass信息中的pass.json中的数据格式，如果不需要更新该属性值，设置为None即可。
    pass_ = None  # 修改: 把 pass 修改为 pass_
    # Alipass唯一标识
    serialNumber = None
    # Alipass状态，目前仅支持CLOSED及USED两种数据。status为USED时，verify_type即为核销时的核销方式。
    status = None
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

    def setExtInfo(self, extInfo):
        self.extInfo = extInfo
        self.apiParas["ext_info"] = extInfo

    def getExtInfo(self):
        return self.extInfo

    def setPass(self, pass_):
        self.pass_ = pass_
        self.apiParas["pass"] = pass_  # 修改: 把 pass 修改为 pass_

    def getPass(self):
        return self.pass_  # 修改: 把 pass 修改为 pass_

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
        return "alipay.pass.sync.update"

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
