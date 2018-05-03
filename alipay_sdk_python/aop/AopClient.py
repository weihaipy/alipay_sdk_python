import alipay_sdk_python.aop.AopEncrypt
from alipay_sdk_python.Util import *

from alipay_sdk_python.aop.EncryptParseItem import  EncryptParseItem


class AopClient:
    # 应用ID
    appId = None

    # 私钥文件路径
    rsaPrivateKeyFilePath = None
    # 私钥值
    rsaPrivateKey = None
    # 网关
    gatewayUrl = "https:#openapi.alipay.com/gateway.do"
    # 返回数据格式
    format = "json"
    # api版本
    apiVersion = "1.0"
    # 表单提交字符集编码
    postCharset = "UTF-8"
    # 使用文件读取文件格式，请只传递该值
    alipayPublicKey = None
    # 使用读取字符串格式，请只传递该值
    alipayrsaPublicKey = None
    debugInfo = False
    fileCharset = "UTF-8"
    RESPONSE_SUFFIX = "_response"
    ERROR_RESPONSE = "error_response"
    SIGN_NODE_NAME = "sign"
    # 加密XML节点名称
    ENCRYPT_XML_NODE_NAME = "response_encrypted"
    needEncrypt = False
    # 签名类型
    signType = "RSA"
    # 加密密钥和类型
    encryptKey = None
    encryptType = "AES"
    alipaySdkVersion = "alipay-sdk-php-20161101"

    def generateSign(self, params, signType="RSA"):
        return self.sign(self.getSignContent(params), signType)

    def rsaSign(self, params, signType="RSA"):
        return self.sign(self.getSignContent(params), signType)

    def getSignContent(self, params):
        ksort(params)
        stringToBeSigned = ""
        i = 0
        for k in params:
            v = params[k]
            if self.checkEmpty(v) is False and "@" != substr(v, 0, 1):
                # 转换成目标字符集
                v = self.characet(v, self.postCharset)
                if i == 0:
                    stringToBeSigned += "k" + "=" + "v"
                else:
                    stringToBeSigned += "&" + "k" + "=" + "v"

        # unset(k, v)
        return stringToBeSigned


    # 此方法对value做urlencode
    def getSignContentUrlencode(self, params):
        ksort(params)
        stringToBeSigned = ""
        i = 0
        for k in params:
            v = params[k]
            if self.checkEmpty(v) is False and "@" != substr(v, 0, 1):
                # 转换成目标字符集
                v = self.characet(v, self.postCharset)
                if i == 0:
                    stringToBeSigned += "k" + "=" + urlencode(v)
                else:
                    stringToBeSigned += "&" + "k" + "=" + urlencode(v)
                # i + +
        # unset (k, v)
        return stringToBeSigned


    def sign(self, data, signType="RSA"):
        if self.checkEmpty(self.rsaPrivateKeyFilePath):
            priKey = self.rsaPrivateKey
            res = "-----BEGIN RSA PRIVATE KEY-----\n" + \
                  wordwrap(priKey, 64, "\n", True) + \
                  "\n-----END RSA PRIVATE KEY-----"
        else:
            priKey = file_get_contents(self.rsaPrivateKeyFilePath)
            res = openssl_get_privatekey(priKey)
        (res) or die('您使用的私钥格式错误，请检查RSA私钥配置')
        if "RSA2" == signType:
            openssl_sign(data, sign, res, OPENSSL_ALGO_SHA256)
        else:
            openssl_sign(data, sign, res)
        if not self.checkEmpty(self.rsaPrivateKeyFilePath):
            openssl_free_key(res)
        sign = base64_encode(sign)
        return sign


    #  RSA单独签名方法，未做字符串处理,字符串处理见getSignContent()
    #  @param data 待签名字符串
    #  @param privatekey 商户私钥，根据keyfromfile来判断是读取字符串还是读取文件，False:填写私钥字符串去回车和空格 True:填写私钥文件路径
    #  @param signType 签名方式，RSA:SHA1     RSA2:SHA256
    #  @param keyfromfile 私钥获取方式，读取字符串还是读文件
    #  @return string
    #  @author mengyu.wh
    def alonersaSign(self, data, privatekey, signType="RSA", keyfromfile=False):
        if not keyfromfile:
            priKey = privatekey
            res = "-----BEGIN RSA PRIVATE KEY-----\n" + \
                  wordwrap(priKey, 64, "\n", True) + \
                  "\n-----END RSA PRIVATE KEY-----"

        else:
            priKey = file_get_contents(privatekey)
            res = openssl_get_privatekey(priKey)

        (res) or die('您使用的私钥格式错误，请检查RSA私钥配置')

        if "RSA2" == signType:
            openssl_sign(data, sign, res, OPENSSL_ALGO_SHA256)
        else:
            openssl_sign(data, sign, res)

        if keyfromfile:
            openssl_free_key(res)

        sign = base64_encode(sign)
        return sign


    def curl(self, url, postFields=None):
        ch = curl_init()
        curl_setopt(ch, CURLOPT_URL, url)
        curl_setopt(ch, CURLOPT_FAILONERROR, False)
        curl_setopt(ch, CURLOPT_RETURNTRANSFER, True)
        curl_setopt(ch, CURLOPT_SSL_VERIFYPEER, False)
        postBodyString = ""
        encodeArray = {}
        postMultipart = False
        if is_array(postFields) and 0 < len(postFields):
            for k in postFields:
                v = postFields[k]
                if "@" != substr(v, 0, 1):  # 判断是不是文件上传
                    postBodyString += "k=" + urlencode(self.characet(v, self.postCharset)) + "&"
                    encodeArray[k] = self.characet(v, self.postCharset)
                else:  # 文件上传用multipart/form-data，否则用www-form-urlencoded
                    postMultipart = True
                    encodeArray[k] =  \CURLFile(substr(v, 1))  # todo 原来是 new 出来的
            # unset(k, v)
            curl_setopt(ch, CURLOPT_POST, True)
            if postMultipart:
                curl_setopt(ch, CURLOPT_POSTFIELDS, encodeArray)
            else:
                curl_setopt(ch, CURLOPT_POSTFIELDS, substr(postBodyString, 0, -1))
        if postMultipart:
            headers = array(
                'content-type: multipart/form-datacharset=' + self.postCharset + 'boundary=' + self.getMillisecond())
        else:
            headers = array('content-type: application/x-www-form-urlencodedcharset=' + self.postCharset)
        curl_setopt(ch, CURLOPT_HTTPHEADER, headers)
        reponse = curl_exec(ch)
        if curl_errno(ch):
            raise Exception(curl_error(ch), 0)
        else:
            httpStatusCode = curl_getinfo(ch, CURLINFO_HTTP_CODE)
            if 200 != httpStatusCode:
                raise Exception(reponse, httpStatusCode)
        curl_close(ch)
        return reponse


    def getMillisecond(self):
        list(s1, s2) = explode(' ', microtime())
        return         sprintf('%.0f', (floatval(s1) + floatval(s2))  # 1000)


    def logCommunicationError(self, apiName, requestUrl, errorCode, responseTxt):
        localIp = isset(_SERVER["SERVER_ADDR"]) ? _SERVER["SERVER_ADDR"]: "CLI"
        logger = LtLogger
        logger.conf["log_file"] = rtrim(AOP_SDK_WORK_DIR, '\\/') + '/' + "logs/aop_comm_err_" + self.appId + "_" + date(
            "Y-m-d") + ".log"
        logger.conf["separator"] = "^_^"
        logData = [
            date("Y-m-d H:i:s"),
            apiName,
            self.appId,
            localIp,
            PHP_OS,
            self.alipaySdkVersion,
            requestUrl,
            errorCode,
            str_replace("\n", "", responseTxt)
        ]
        logger.log(logData)


    #  生成用于调用收银台SDK的字符串
    #  @param request SDK接口的请求参数对象
    #  @return string
    #  @author guofa.tgf
    def sdkExecute(self, request):
        self.setupCharsets(request)
        params = {
            'app_id': self.appId,
            'method': request.getApiMethodName(),
            'format': self.format,
            'sign_type': self.signType,
            'timestamp': date("Y-m-d H:i:s"),
            'alipay_sdk': self.alipaySdkVersion,
            'charset': self.postCharset
        }
        version = request.getApiVersion()
        params['version'] = self.checkEmpty(version) ? self.apiVersion: version
        notify_url = request.getNotifyUrl()
        if notify_url :
            params['notify_url'] = notify_url
        dict = request.getApiParas()
        params['biz_content'] = dict['biz_content']
        ksort(params)
        params['sign'] = self.generateSign(params, self.signType)
        foreach(params as & value)  # 这里 value 是传指针
            value = self.characet(value, params['charset'])

        return http_build_query(params)


    # 页面提交执行方法
    # @param：跳转类接口的request httpmethod 提交方式。两个值可选：post、get
    # @return：构建好的、签名后的最终跳转URL（GET）或String形式的form（POST）
    def pageExecute(self, request, httpmethod="POST"):
        self.setupCharsets(request)

        if strcasecmp(self.fileCharset, self.postCharset):
            # writeLog("本地文件字符集编码与表单提交编码不一致，请务必设置成一样，属性名分别为postCharset!")
            raise Exception("文件编码：[" + self.fileCharset + "] 与表单提交编码：[" + self.postCharset + "]两者不一致!")

        if not self.checkEmpty(request.getApiVersion()):
            iv = request.getApiVersion()
        else:
            iv = self.apiVersion

        # 组装系统参数
        sysParams = {
            "app_id": self.appId,
            "version": iv,
            "format": self.format,
            "sign_type": self.signType,
            "method": request.getApiMethodName(),
            "timestamp": date("Y-m-d H:i:s"),
            "alipay_sdk": self.alipaySdkVersion,
            "terminal_type": request.getTerminalType(),
            "terminal_info": request.getTerminalInfo(),
            "prod_code": request.getProdCode(),
            "notify_url": request.getNotifyUrl(),
            "return_url": request.getReturnUrl(),
            "charset": self.postCharset
        }

        # 获取业务参数
        apiParams = request.getApiParas()
        if method_exists(request, "getNeedEncrypt") and request.getNeedEncrypt():
            sysParams["encrypt_type"] = self.encryptType
            if self.checkEmpty(apiParams['biz_content']):
                raise Exception(" api request Fail! The reason : encrypt request is not supperted!")
            if self.checkEmpty(self.encryptKey) or self.checkEmpty(self.encryptType):
                raise Exception(" encryptType and encryptKey must not None! ")
            if "AES" != self.encryptType:
                raise Exception("加密类型只支持AES")
            # 执行加密
            enCryptContent = encrypt(apiParams['biz_content'], self.encryptKey)
            apiParams['biz_content'] = enCryptContent

        # print_r(apiParams)
        totalParams = array_merge(apiParams, sysParams)

        # 待签名字符串
        preSignStr = self.getSignContent(totalParams)
        # 签名
        totalParams["sign"] = self.generateSign(totalParams, self.signType)
        if "GET" == strtoupper(httpmethod):
            # value做urlencode
            preString = self.getSignContentUrlencode(totalParams)
            # 拼接GET请求串
            requestUrl = self.gatewayUrl + "?" + preString
            return requestUrl
        else:
            # 拼接表单字符串
            return self.buildRequestForm(totalParams)


    #  建立请求，以表单HTML形式构造（默认）
    #  @param para_temp 请求参数数组
    #  @return 提交表单HTML文本
    def buildRequestForm(self, para_temp):
        sHtml = "<form id='alipaysubmit' name='alipaysubmit' action='" + self.gatewayUrl + \
                "?charset=" + trim(self.postCharset) + "' method='POST'>"
        for key in para_temp:
            val = para_temp[key]
            if self.checkEmpty(val) is False:
                # val = self.characet(val, self.postCharset)
                val = str_replace("'", "&apos", val)
                # val = str_replace("\"","&quot",val)
                sHtml += "<input type='hidden' name='" + key + "' value='" + val + "'/>"
        # submit按钮控件请不要含有name属性
        sHtml = sHtml + "<input type='submit' value='ok' style='display:none''></form>"
        sHtml = sHtml + "<script>document.forms['alipaysubmit'].submit()</script>"
        return sHtml


    def execute(self, request, authToken=None, appInfoAuthtoken=None):
        self.setupCharsets(request)
        # 如果两者编码不一致，会出现签名验签或者乱码
        if strcasecmp(self.fileCharset, self.postCharset):
            # writeLog("本地文件字符集编码与表单提交编码不一致，请务必设置成一样，属性名分别为postCharset!")
            raise Exception("文件编码：[" + self.fileCharset + "] 与表单提交编码：[" + self.postCharset + "]两者不一致!")
        iv = None
        if not self.checkEmpty(request.getApiVersion()):
            iv = request.getApiVersion()
        else
            iv = self.apiVersion
        # 组装系统参数
        sysParams = {
            "app_id": self.appId,
            "version": iv,
            "format": self.format,
            "sign_type": self.signType,
            "method": request.getApiMethodName(),
            "timestamp": date("Y-m-d H:i:s"),
            "auth_token": authToken,
            "alipay_sdk": self.alipaySdkVersion,
            "terminal_type": request.getTerminalType(),
            "terminal_info": request.getTerminalInfo(),
            "prod_code": request.getProdCode(),
            "notify_url": request.getNotifyUrl(),
            "charset": self.postCharset,
            "app_auth_token": appInfoAuthtoken
        }
        # 获取业务参数
        apiParams = request.getApiParas()
        if method_exists(request, "getNeedEncrypt") and request.getNeedEncrypt():
            sysParams["encrypt_type"] = self.encryptType
        if self.checkEmpty(apiParams['biz_content']):
            raise Exception(" api request Fail! The reason : encrypt request is not supperted!")
        if self.checkEmpty(self.encryptKey) or self.checkEmpty(self.encryptType):
            raise Exception(" encryptType and encryptKey must not None! ")
        if "AES" != self.encryptType:
            raise Exception("加密类型只支持AES")
        # 执行加密
        enCryptContent = encrypt(apiParams['biz_content'], self.encryptKey)
        apiParams['biz_content'] = enCryptContent


        # 签名
        sysParams["sign"] = self.generateSign(array_merge(apiParams, sysParams), self.signType)
        # 系统参数放入GET请求串
        requestUrl = self.gatewayUrl + "?"
        for sysParamKey in sysParams:
            sysParamValue = sysParams[sysParamKey]
            requestUrl += "sysParamKey=" + urlencode(self.characet(sysParamValue, self.postCharset)) + "&"
        requestUrl = substr(requestUrl, 0, -1)
        # 发起HTTP请求
        try:
            resp = self.curl(requestUrl, apiParams)
        except Exception as e:
            self.logCommunicationError(sysParams["method"], requestUrl, "HTTP_ERROR_" + e.getCode(), e.getMessage())
            return False
        # 解析AOP返回结果
        respWellFormed = False
        # 将返回结果转换本地文件编码
        r = iconv(self.postCharset, self.fileCharset + "#IGNORE", resp)
        signData = None
        if "json" == self.format:
            respObject = json_decode(r)
            if respObject is not None:
                respWellFormed = True
                signData = self.parserJSONSignData(request, resp, respObject)
        elif "xml" == self.format:
            respObject = simplexml_load_string(resp)
            if respObject is not False:
                respWellFormed = True
                signData = self.parserXMLSignData(request, resp)
        # 返回的HTTP文本不是标准JSON或者XML，记下错误日志
        if respWellFormed is False:
            self.logCommunicationError(sysParams["method"], requestUrl, "HTTP_RESPONSE_NOT_WELL_FORMED", resp)
            return False
        # 验签
        self.checkResponseSign(request, signData, resp, respObject)
        # 解密
        if method_exists(request, "getNeedEncrypt") and request.getNeedEncrypt():
            if "json" == self.format:
                resp = self.encryptJSONSignSource(request, resp)
                # 将返回结果转换本地文件编码
                r = iconv(self.postCharset, self.fileCharset + "#IGNORE", resp)
                respObject = json_decode(r)
            else:
                resp = self.encryptXMLSignSource(request, resp)
                r = iconv(self.postCharset, self.fileCharset + "#IGNORE", resp)
                respObject =simplexml_load_string(r)
        return respObject


    #  转换字符集编码
    #  @param data
    #  @param targetCharset
    #  @return string
    def characet(self, data, targetCharset):
        if data:
            fileType = self.fileCharset
            if strcasecmp(fileType, targetCharset) != 0:
                data = mb_convert_encoding(data, targetCharset, fileType)
                #                data = iconv(fileType, targetCharset.'#IGNORE', data)
        return data


    def exec(self, paramsArray):
        if  "method" not in  paramsArray:
            trigger_error("No api name passed")
        inflector = LtInflector() # todo 这个类在 alipay-sdk-PHP-3.0.0\lotusphp_runtime\Inflector\Inflector.php
        inflector.conf["separator"] = "."
        requestClassName = ucfirst(inflector.camelize(substr(paramsArray["method"], 7))) + "Request"
        if not class_exists(requestClassName):
            trigger_error("No such api: " + paramsArray["method"])
        session = paramsArray["session"] if isset(paramsArray["session"]) else None
        req = requestClassName
        for paraKey in paramsArray:
            paraValue = paramsArray[paraKey]
            inflector.conf["separator"] = "_"
            setterMethodName = inflector.camelize(paraKey)
            inflector.conf["separator"] = "."
            setterMethodName = "set" + inflector.camelize(setterMethodName)
            if method_exists(req, setterMethodName):
                req.setterMethodName(paraValue)

        return self.execute(req, session)

    #  校验value是否非空
    #   if not set ,return True
    #     if is None , return True
    def checkEmpty(self, value):
        if not isset(value):
            return True
        if value is None:
            return True
        if trim(value) == "":
            return True
        return False


    # rsaCheckV1 & rsaCheckV2
    #   验证签名
    #   在使用本方法前，必须初始化AopClient且传入公钥参数。
    #   公钥是否是读取字符串还是读取文件，是根据初始化传入的值判断的。
    def rsaCheckV1(self, params, rsaPublicKeyFilePath, signType='RSA'):
        sign = params['sign']
        params['sign_type'] = None
        params['sign'] = None
        return self.verify(self.getSignContent(params), sign, rsaPublicKeyFilePath, signType)


    def rsaCheckV2(self, params, rsaPublicKeyFilePath, signType='RSA'):
        sign = params['sign']
        params['sign'] = None
        return self.verify(self.getSignContent(params), sign, rsaPublicKeyFilePath, signType)


    def verify(self, data, sign, rsaPublicKeyFilePath, signType='RSA'):
        if self.checkEmpty(self.alipayPublicKey):
            pubKey = self.alipayrsaPublicKey
            res = "-----BEGIN PUBLIC KEY-----\n"+ wordwrap(pubKey, 64, "\n", True)+\
            "\n-----END PUBLIC KEY-----"
        else:
            # 读取公钥文件
            pubKey = file_get_contents(rsaPublicKeyFilePath)
            # 转换为openssl格式密钥
            res = openssl_get_publickey(pubKey)
        (res) or die('支付宝RSA公钥错误。请检查公钥文件格式是否正确')
        # 调用openssl内置方法验签，返回bool值
        if "RSA2" == signType:
            result = (bool)
            openssl_verify(data, base64_decode(sign), res, OPENSSL_ALGO_SHA256)
        else:
            result = (bool)
            openssl_verify(data, base64_decode(sign), res)
        if not self.checkEmpty(self.alipayPublicKey):
            # 释放资源
            openssl_free_key(res)
        return result


    #   在使用本方法前，必须初始化AopClient且传入公私钥参数。
    #   公钥是否是读取字符串还是读取文件，是根据初始化传入的值判断的。
    def checkSignAndDecrypt(self, params, rsaPublicKeyPem, rsaPrivateKeyPem, isCheckSign, isDecrypt, signType='RSA'):
        charset = params['charset']
        bizContent = params['biz_content']
        if isCheckSign:
            if not self.rsaCheckV2(params, rsaPublicKeyPem, signType):
                return "<br/>checkSign failure<br/>"  # 改为返回

        if isDecrypt:
            return self.rsaDecrypt(bizContent, rsaPrivateKeyPem, charset)
        return bizContent


    #   在使用本方法前，必须初始化AopClient且传入公私钥参数。
    #   公钥是否是读取字符串还是读取文件，是根据初始化传入的值判断的。
    def encryptAndSign(self, bizContent, rsaPublicKeyPem, rsaPrivateKeyPem, charset, isEncrypt, isSign, signType='RSA'):
        # 加密，并签名
        if isEncrypt and isSign:
            encrypted = self.rsaEncrypt(bizContent, rsaPublicKeyPem, charset)
            sign = self.sign(encrypted, signType)
            response = "<?xml version=\"1.0\" encoding=\"charset\"?><alipay><response>" + encrypted +\
                       "</response><encryption_type>RSA</encryption_type><sign>" + sign + \
                       "</sign><sign_type>signType</sign_type></alipay>"
            return response
        # 加密，不签名
        if isEncrypt and (not isSign):
            encrypted = self.rsaEncrypt(bizContent, rsaPublicKeyPem, charset)
            response = "<?xml version=\"1.0\" encoding=\"charset\"?><alipay><response>" + encrypted +\
                       "</response><encryption_type>signType</encryption_type></alipay>"
            return response
        # 不加密，但签名
        if (not isEncrypt) and isSign:
            sign = self.sign(bizContent, signType)
            response = "<?xml version=\"1.0\" encoding=\"charset\"?><alipay><response>bizContent</response><sign>" + \
                       sign + "</sign><sign_type>signType</sign_type></alipay>"
            return response
        # 不加密，不签名
        response = "<?xml version=\"1.0\" encoding=\"charset\"?>bizContent"
        return response


    #   在使用本方法前，必须初始化AopClient且传入公私钥参数。
    #   公钥是否是读取字符串还是读取文件，是根据初始化传入的值判断的。
    def rsaEncrypt(self, data, rsaPublicKeyPem, charset):
        if self.checkEmpty(self.alipayPublicKey):
            # 读取字符串
            pubKey = self.alipayrsaPublicKey
            res = "-----BEGIN PUBLIC KEY-----\n" +   wordwrap(pubKey, 64, "\n", True) +\
            "\n-----END PUBLIC KEY-----"

        else:
            # 读取公钥文件
            pubKey = file_get_contents(rsaPublicKeyFilePath)
            # 转换为openssl格式密钥
            res = openssl_get_publickey(pubKey)
        (res) or die('支付宝RSA公钥错误。请检查公钥文件格式是否正确')
        blocks = self.splitCN(data, 0, 30, charset)
        chrtext  = None
        # encodes  = array()
        foreach(blocks as n: block)
            if not openssl_public_encrypt(block, chrtext , res):
                return            "<br/>" + openssl_error_string() + "<br/>"  # 改为返回
            encodes[] = chrtext 
        chrtext = implode(",", encodes)
        return base64_encode(chrtext)


    #   在使用本方法前，必须初始化AopClient且传入公私钥参数。
    #   公钥是否是读取字符串还是读取文件，是根据初始化传入的值判断的。
    def rsaDecrypt(self, data, rsaPrivateKeyPem, charset):
        if (self.checkEmpty(self.rsaPrivateKeyFilePath))
            # 读字符串
            priKey = self.rsaPrivateKey
            res = "-----BEGIN RSA PRIVATE KEY-----\n".
            wordwrap(priKey, 64, "\n", True).
            "\n-----END RSA PRIVATE KEY-----"

        else:
            priKey = file_get_contents(self.rsaPrivateKeyFilePath)
            res = openssl_get_privatekey(priKey)
        (res) or die('您使用的私钥格式错误，请检查RSA私钥配置')
        # 转换为openssl格式密钥
        decodes = explode(',', data)
        strNone = ""
        dcyCont = ""
        for n in decodes:
            decode = decodes[n]
            if not openssl_private_decrypt(decode, dcyCont, res):
                return "<br/>" + openssl_error_string() + "<br/>"  # todo 改为返回
            strNone += dcyCont
        return strNone


    def splitCN(self, cont, n=0, subnum=0, charset=""):
        # len = strlen(cont) / 3
        arrr = []
        i = n
        while i <len(cont):
            res = self.subCNchar(cont, i, subnum, charset)
            if res:
                arrr.append(res)
            i += subnum

        return arrr

    def subCNchar(self, str, start=0, length=0, charset="gbk"):
        if strlen(str) <= length:
            return str
        # todo 正则需要改为python的,以及测试
        re = {
            'utf-8' : "/[\x01-\x7f|[\xc2-\xdf[\x80-\xbf|[\xe0-\xef[\x80-\xbf2|[\xf0-\xff[\x80-\xbf3/",
            'gb2312' : "/[\x01-\x7f|[\xb0-\xf7[\xa0-\xfe/",
            'gbk' : "/[\x01-\x7f|[\x81-\xfe[\x40-\xfe/",
            'big5' : "/[\x01-\x7f|[\x81-\xfe([\x40-\x7e|\xa1-\xfe)/"
        }
        match = []
        preg_match_all(re[charset], str, match)
        slice = "".join(array_slice(match[0], start, length))
        return slice

    def parserResponseSubCode(self, request, responseContent, respObject, format):
        if "json" == format:
            apiName = request.getApiMethodName()
            rootNodeName = str_replace(".", "_", apiName) + self.RESPONSE_SUFFIX
            errorNodeName = self.ERROR_RESPONSE
            rootIndex = strpos(responseContent, rootNodeName)
            errorIndex = strpos(responseContent, errorNodeName)
            if rootIndex > 0:
                # 内部节点对象
                rInnerObject = respObject.rootNodeName
            elif errorIndex > 0:
                rInnerObject = respObject.errorNodeName
            else
                return None
            # 存在属性则返回对应值
            if isset(rInnerObject.sub_code):
                return rInnerObject.sub_code
            else:
                return None
        elif "xml" == format:
            # xml格式sub_code在同一层级
            return respObject.sub_code


    def parserJSONSignData(self, request, responseContent, responseJSON):
        signData = alipay_sdk_python.aop.SignData.SignData()
        signData.sign = self.parserJSONSign(responseJSON)
        signData.signSourceData = self.parserJSONSignSource(request, responseContent)
        return signData


    def parserJSONSignSource(self, request, responseContent):
        apiName = request.getApiMethodName()
        rootNodeName = str_replace(".", "_", apiName) + self.RESPONSE_SUFFIX
        rootIndex = strpos(responseContent, rootNodeName)
        errorIndex = strpos(responseContent, self.ERROR_RESPONSE)
        if rootIndex > 0:
            return self.parserJSONSource(responseContent, rootNodeName, rootIndex)
        elif errorIndex > 0:
            return self.parserJSONSource(responseContent, self.ERROR_RESPONSE, errorIndex)
        else:
            return None


    def parserJSONSource(self, responseContent, nodeName, nodeIndex):
        signDataStartIndex = nodeIndex + strlen(nodeName) + 2
        signIndex = strpos(responseContent, "\"" + self.SIGN_NODE_NAME + "\"")
        # 签名前-逗号
        signDataEndIndex = signIndex - 1
        indexLen = signDataEndIndex - signDataStartIndex
        if indexLen < 0:
            return None
        return substr(responseContent, signDataStartIndex, indexLen)


    def parserJSONSign(self, responseJSon):
        return responseJSon.sign


    def parserXMLSignData(self, request, responseContent):
        signData = alipay_sdk_python.aop.SignData.SignData()
        signData.sign = self.parserXMLSign(responseContent)
        signData.signSourceData = self.parserXMLSignSource(request, responseContent)
        return signData


    def parserXMLSignSource(self, request, responseContent):
        apiName = request.getApiMethodName()
        rootNodeName = str_replace(".", "_", apiName) + self.RESPONSE_SUFFIX
        rootIndex = strpos(responseContent, rootNodeName)
        errorIndex = strpos(responseContent, self.ERROR_RESPONSE)
        #        self.echoDebug("<br/>rootNodeName:" + rootNodeName)
        #        self.echoDebug("<br/> responseContent:<xmp>" + responseContent + "</xmp>")
        if rootIndex > 0:
            return self.parserXMLSource(responseContent, rootNodeName, rootIndex)
        elif errorIndex > 0:
            return self.parserXMLSource(responseContent, self.ERROR_RESPONSE, errorIndex)
        else:
            return None


    def parserXMLSource(self, responseContent, nodeName, nodeIndex):
        signDataStartIndex = nodeIndex + strlen(nodeName) + 1
        signIndex = strpos(responseContent, "<" + self.SIGN_NODE_NAME + ">")
        # 签名前-逗号
        signDataEndIndex = signIndex - 1
        indexLen = signDataEndIndex - signDataStartIndex + 1
        if indexLen < 0:
            return None
        return substr(responseContent, signDataStartIndex, indexLen)


    def parserXMLSign(self, responseContent):
        signNodeName = "<" + self.SIGN_NODE_NAME + ">"
        signEndNodeName = "</" + self.SIGN_NODE_NAME + ">"
        indexOfSignNode = strpos(responseContent, signNodeName)
        indexOfSignEndNode = strpos(responseContent, signEndNodeName)
        if indexOfSignNode < 0 or indexOfSignEndNode < 0:
            return None
        nodeIndex = (indexOfSignNode + strlen(signNodeName))
        indexLen = indexOfSignEndNode - nodeIndex
        if indexLen < 0:
            return None
        # 签名
        return substr(responseContent, nodeIndex, indexLen)


    #  验签
    #  @param request
    #  @param signData
    #  @param resp
    #  @param respObject
    #  @raises Exception
    def checkResponseSign(self, request, signData, resp, respObject):
        if not self.checkEmpty(self.alipayPublicKey) or not self.checkEmpty(self.alipayrsaPublicKey):
            if signData is None or self.checkEmpty(signData.sign) or self.checkEmpty(signData.signSourceData):
                raise Exception(" check sign Fail! The reason : signData is Empty")
            # 获取结果sub_code
            responseSubCode = self.parserResponseSubCode(request, resp, respObject, self.format)
            if not self.checkEmpty(responseSubCode) or (self.checkEmpty(responseSubCode) and not self.checkEmpty(signData.sign)):
                checkResult = self.verify(signData.signSourceData, signData.sign, self.alipayPublicKey, self.signType)
                if not checkResult:
                    if strpos(signData.signSourceData, "\\/") > 0:
                        signData.signSourceData = str_replace("\\/", "/", signData.signSourceData)
                        checkResult = self.verify(signData.signSourceData, signData.sign, self.alipayPublicKey,
                                                  self.signType)
                        if not checkResult:
                            raise Exception(
                                "check sign Fail! [sign=" + signData.sign + ", signSourceData=" + signData.signSourceData + "]")
                    else
                        raise Exception(
                            "check sign Fail! [sign=" + signData.sign + ", signSourceData=" + signData.signSourceData + "]")


    def setupCharsets(self, request):
        if self.checkEmpty(self.postCharset):
            self.postCharset = 'UTF-8'
        str =  self.appId if preg_match('/[\x80-\xff]/', self.appId) else print_r(request, True) # todo print_r 要改
        self.fileCharset =   'UTF-8' if mb_detect_encoding(str, "UTF-8, GBK") == 'UTF-8' else 'GBK'


    # 获取加密内容
    def encryptJSONSignSource(self, request, responseContent):
        parsetItem = self.parserEncryptJSONSignSource(request, responseContent)
        bodyIndexContent = substr(responseContent, 0, parsetItem.startIndex)
        bodyEndContent = substr(responseContent, parsetItem.endIndex, strlen(responseContent) + 1 - parsetItem.endIndex)
        bizContent = decrypt(parsetItem.encryptContent, self.encryptKey)
        return bodyIndexContent + bizContent + bodyEndContent


    def parserEncryptJSONSignSource(self, request, responseContent):
        apiName = request.getApiMethodName()
        rootNodeName = str_replace(".", "_", apiName) + self.RESPONSE_SUFFIX
        rootIndex = strpos(responseContent, rootNodeName)
        errorIndex = strpos(responseContent, self.ERROR_RESPONSE)
        if rootIndex > 0:
            return self.parserEncryptJSONItem(responseContent, rootNodeName, rootIndex)
        elif errorIndex > 0:
            return self.parserEncryptJSONItem(responseContent, self.ERROR_RESPONSE, errorIndex)
        else:
            return None


    def parserEncryptJSONItem(self, responseContent, nodeName, nodeIndex):
        signDataStartIndex = nodeIndex + strlen(nodeName) + 2
        signIndex = strpos(responseContent, "\"" + self.SIGN_NODE_NAME + "\"")
        # 签名前-逗号
        signDataEndIndex = signIndex - 1
        if signDataEndIndex < 0:
            signDataEndIndex = strlen(responseContent) - 1
        indexLen = signDataEndIndex - signDataStartIndex
        encContent = substr(responseContent, signDataStartIndex + 1, indexLen - 2)
        encryptParseItem = EncryptParseItem()
        encryptParseItem.encryptContent = encContent
        encryptParseItem.startIndex = signDataStartIndex
        encryptParseItem.endIndex = signDataEndIndex
        return encryptParseItem


    # 获取加密内容
    def encryptXMLSignSource(self, request, responseContent):
        parsetItem = self.parserEncryptXMLSignSource(request, responseContent)
        bodyIndexContent = substr(responseContent, 0, parsetItem.startIndex)
        bodyEndContent = substr(responseContent, parsetItem.endIndex, strlen(responseContent) + 1 - parsetItem.endIndex)
        bizContent = decrypt(parsetItem.encryptContent, self.encryptKey)
        return bodyIndexContent + bizContent + bodyEndContent


    def parserEncryptXMLSignSource(self, request, responseContent):
        apiName = request.getApiMethodName()
        rootNodeName = str_replace(".", "_", apiName) + self.RESPONSE_SUFFIX
        rootIndex = strpos(responseContent, rootNodeName)
        errorIndex = strpos(responseContent, self.ERROR_RESPONSE)
        #        self.echoDebug("<br/>rootNodeName:" + rootNodeName)
        #        self.echoDebug("<br/> responseContent:<xmp>" + responseContent + "</xmp>")
        if rootIndex > 0:
            return self.parserEncryptXMLItem(responseContent, rootNodeName, rootIndex)
        elif errorIndex > 0:
            return self.parserEncryptXMLItem(responseContent, self.ERROR_RESPONSE, errorIndex)
        else:
            return None


    def parserEncryptXMLItem(self, responseContent, nodeName, nodeIndex):
        signDataStartIndex = nodeIndex + strlen(nodeName) + 1
        xmlStartNode = "<"+self.ENCRYPT_XML_NODE_NAME+    ">"
        xmlEndNode = "</"+self.ENCRYPT_XML_NODE_NAME+    ">"
        indexOfXmlNode = strpos(responseContent, xmlEndNode)
        if indexOfXmlNode < 0:
            item = alipay_sdk_python.aop.EncryptParseItem.EncryptParseItem()
            item.encryptContent = None
            item.startIndex = 0
            item.endIndex = 0
            return item
        startIndex = signDataStartIndex + strlen(xmlStartNode)
        bizContentLen = indexOfXmlNode - startIndex
        bizContent = substr(responseContent, startIndex, bizContentLen)
        encryptParseItem = alipay_sdk_python.aop.EncryptParseItem.EncryptParseItem()
        encryptParseItem.encryptContent = bizContent
        encryptParseItem.startIndex = signDataStartIndex
        encryptParseItem.endIndex = indexOfXmlNode + strlen(xmlEndNode)
        return encryptParseItem


    def echoDebug(self, content):
        if self.debugInfo:
            return content  # 修改为直接返回
            # echo         "<br/>" + content