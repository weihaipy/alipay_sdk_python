# ALIPAY API: zhima.merchant.closeloop.data.upload request
#
# @author auto create
# @since 1.0, 2018-01-11 15:47:27
class ZhimaMerchantCloseloopDataUploadRequest:
    # 公用回传参数（非必填），该参数会透传给商户，商户可以用于业务逻辑处理，请使用json格式。
    bizExtParams = None
    # 单条数据的数据列，多个列以逗号隔开。
    columns = None
    # 传入的json格式的文件，其中records属性必填。json中的字段可以通过如下步骤获取：首先调用zhima.merchant.data.upload.initialize接口获取数据模板，该接口会返回一个数据模板文件的url地址，如：http:# zmxymerchant-prod.oss-cn-shenzhen.zmxy.com.cn/openApi/openDoc/信用护航-负面记录和信用足迹商户数据模板V1.0.xlsx，该数据模板文件详细列出了需要传入的字段，及各字段的要求，data中的各字段就是该文件中列出的字段编码。
    file = None
    # 文件的编码，如果文件格式是UTF-8，则填写UTF-8，如果文件格式是GBK，则填写GBK。
    fileCharset = None
    # 芝麻平台服务商模式下的二级商户标识（即二级商户PID），如果是直连商户调用该接口，不需要设置
    linkedMerchantId = None
    # 主键列使用传入字段进行组合，也可以使用传入的某个单字段（确保主键稳定，而且可以很好的区分不同的数据）。例如order_no,pay_month或者order_no,bill_month组合，对于一个order_no只会有一条数据的情况，直接使用order_no作为主键列。
    primaryKeyColumns = None
    # 文件数据记录条数，如file字段中的record数组有10条数据，那么就填10。
    records = None
    # 数据应用的场景编码，场景码和场景名称（数字或字符串为场景码）如下：
    # 8：数据反馈
    # 32：骑行
    # CAR_RENTING：租车行业解决方案
    # 每个场景码对应的数据模板不一样，请使用zhima.merchant.data.upload.initialize接口获取场景码对应的数据模板。
    sceneCode = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setBizExtParams(self, bizExtParams):
        self.bizExtParams = bizExtParams
        self.apiParas["biz_ext_params"] = bizExtParams

    def getBizExtParams(self):
        return self.bizExtParams

    def setColumns(self, columns):
        self.columns = columns
        self.apiParas["columns"] = columns

    def getColumns(self):
        return self.columns

    def setFile(self, file):
        self.file = file
        self.apiParas["file"] = file

    def getFile(self):
        return self.file

    def setFileCharset(self, fileCharset):
        self.fileCharset = fileCharset
        self.apiParas["file_charset"] = fileCharset

    def getFileCharset(self):
        return self.fileCharset

    def setLinkedMerchantId(self, linkedMerchantId):
        self.linkedMerchantId = linkedMerchantId
        self.apiParas["linked_merchant_id"] = linkedMerchantId

    def getLinkedMerchantId(self):
        return self.linkedMerchantId

    def setPrimaryKeyColumns(self, primaryKeyColumns):
        self.primaryKeyColumns = primaryKeyColumns
        self.apiParas["primary_key_columns"] = primaryKeyColumns

    def getPrimaryKeyColumns(self):
        return self.primaryKeyColumns

    def setRecords(self, records):
        self.records = records
        self.apiParas["records"] = records

    def getRecords(self):
        return self.records

    def setSceneCode(self, sceneCode):
        self.sceneCode = sceneCode
        self.apiParas["scene_code"] = sceneCode

    def getSceneCode(self):
        return self.sceneCode

    def getApiMethodName(self):
        return "zhima.merchant.closeloop.data.upload"

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
