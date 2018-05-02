
 # ALIPAY API: alipay.zdatafront.datatransfered.fileupload request
 #
 # @author auto create
 # @since 1.0, 2017-05-02 14:41:11
class AlipayZdatafrontDatatransferedFileuploadRequest:

    # 合作伙伴上传文件中的各字段,使用英文半角","分隔，file_type为json_data时必选
    columns = None

    # 二进制字节数组，由文件转出，最大支持50M文件的上传
    file = None

    # 文件描述信息，非解析数据类型必选
    fileDescription = None

    # 文件摘要，算法SHA
    fileDigest = None

    # 描述上传文件的类型
    fileType = None

    # 上传数据文件的主键字段，注意该pk若出现重复则后入数据会覆盖前面的，file_type为json_data时必选
    primaryKey = None

    # 上传数据文件包含的记录数，file_type为json_data时必选
    records = None

    # 外部公司的数据源标识信息，由联接网络分配
    typeId = None
    apiParas = {}
    terminalType=None
    terminalInfo=None
    prodCode=None
    apiVersion="1.0"
    notifyUrl=None
    returnUrl=None
    needEncrypt=False

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

    def setFileDescription(self, fileDescription):
        self.fileDescription = fileDescription
        self.apiParas["file_description"] = fileDescription

    def getFileDescription(self):
        return self.fileDescription

    def setFileDigest(self, fileDigest):
        self.fileDigest = fileDigest
        self.apiParas["file_digest"] = fileDigest

    def getFileDigest(self):
        return self.fileDigest

    def setFileType(self, fileType):
        self.fileType = fileType
        self.apiParas["file_type"] = fileType

    def getFileType(self):
        return self.fileType

    def setPrimaryKey(self, primaryKey):
        self.primaryKey = primaryKey
        self.apiParas["primary_key"] = primaryKey

    def getPrimaryKey(self):
        return self.primaryKey

    def setRecords(self, records):
        self.records = records
        self.apiParas["records"] = records

    def getRecords(self):
        return self.records

    def setTypeId(self, typeId):
        self.typeId = typeId
        self.apiParas["type_id"] = typeId

    def getTypeId(self):
        return self.typeId

    def getApiMethodName(self):
        return "alipay.zdatafront.datatransfered.fileupload"

    def setNotifyUrl(self, notifyUrl):
        self.notifyUrl=notifyUrl

    def getNotifyUrl(self):
        return self.notifyUrl

    def setReturnUrl(self, returnUrl):
        self.returnUrl=returnUrl

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
        self.apiVersion=apiVersion

    def getApiVersion(self):
        return self.apiVersion

    def setNeedEncrypt(self, needEncrypt):

       self.needEncrypt=needEncrypt

    def getNeedEncrypt(self):
                   return self.needEncrypt

