# ALIPAY API: zhima.data.batch.feedback request
#
# @author auto create
# @since 1.0, 2017-05-02 14:40:53
class ZhimaDataBatchFeedbackRequest:
    # 扩展参数
    bizExtParams = None
    # 单条数据的数据列，多个列以逗号隔开
    columns = None
    # 反馈的json格式文件，其中"records":  是每个文件的固定开头，文件中的字段名请使用数据反馈模板（该模板是通过“获取数据反馈模板”接口获得）中字段编码列的英文字段来组装
    file = None
    # 是反馈文件的数据编码，如果文件格式是UTF-8，则填写UTF-8，如果文件格式是GBK，则填写GBK
    fileCharset = None
    # 文件描述信息
    fileDescription = None
    # 反馈的数据类型
    fileType = None
    # 主键列使用反馈字段进行组合，也可以使用反馈的某个单字段（确保主键稳定，而且可以很好的区分不同的数据）。例如order_no,pay_month或者order_no,bill_month组合，对于一个order_no只会有一条数据的情况，直接使用order_no作为主键列
    primaryKeyColumns = None
    # 文件数据记录条数
    records = None
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

    def setFileDescription(self, fileDescription):
        self.fileDescription = fileDescription
        self.apiParas["file_description"] = fileDescription

    def getFileDescription(self):
        return self.fileDescription

    def setFileType(self, fileType):
        self.fileType = fileType
        self.apiParas["file_type"] = fileType

    def getFileType(self):
        return self.fileType

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

    def getApiMethodName(self):
        return "zhima.data.batch.feedback"

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
