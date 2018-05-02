


 #  多媒体文件客户端
 #  @author yikai.hu
 #  @version Id: AlipayMobilePublicMultiMediaClient.php, v 0.1 Aug 15, 2014 10:19:01 AM yikai.hu Exp


#namespace alipay\api
from alipay_sdk_python.aop.request import AlipayMobilePublicMultiMediaExecute
from alipay_sdk_python.Util import  *


class AlipayMobilePublicMultiMediaClient:
    DEFAULT_CHARSET = 'UTF-8'
    METHOD_POST     = "POST"
    METHOD_GET      = "GET"
    SIGN            = 'sign' #get name
    timeout = 10 # 超时时间
    serverUrl=None
    appId=None
    privateKey=None
    prodCode=None
    format          = 'json' #todo
    sign_type       = 'RSA' #todo
    charset=None
    apiVersion    = "1.0"
    apiMethodName = "alipay.mobile.public.multimedia.download"
    media_id = "L21pZnMvVDFQV3hYWGJKWFhYYUNucHJYP3Q9YW13ZiZ4c2lnPTU0MzRhYjg1ZTZjNWJmZTMxZGJiNjIzNDdjMzFkNzkw575"
    # 此处写死的，实际开发中，请传入
    connectTimeout  = 3000
    readTimeout     = 15000

    def __init__(self, serverUrl = '', appId = '', partner_private_key = '', format = '', charset = 'GBK'):
        self.serverUrl = serverUrl
        self.appId = appId
        self.privateKey = partner_private_key
        self.format = format
        self.charset = charset

    #  getContents 获取网址内容
    #  @param request
    #  @return text | bin
    def getContents(self):
        #自己的服务器如果没有 curl，可用：fsockopen() 等
        #1:
        #2： 私钥格式
        datas = {
            "app_id"         : self.appId,
            "method"         : self.METHOD_POST,
            "sign_type"     : self.sign_type,
            "version"         : self.apiVersion,
            "timestamp"     : date('Y-m-d H:i:s')  ,#yyyy-MM-dd HH:mm:ss
            "biz_content"     : '"mediaId":"'+ self.media_id  +'"',
            "charset"         : self.charset
        }

        #要提交的数据
        data_sign = self.buildGetUrl( datas )

        post_data = data_sign
        #初始化 curl
        ch = curl_init()
        #设置目标服务器
        curl_setopt(ch, CURLOPT_URL, self.serverUrl )
        curl_setopt(ch, CURLOPT_HEADER, True)
        # curl_setopt(ch, CURLOPT_RETURNTRANSFER, 1)
        #超时时间
        curl_setopt(ch, CURLOPT_TIMEOUT, self.timeout)

        if  self.METHOD_POST == 'POST':
            # post数据
            curl_setopt(ch, CURLOPT_POST, 1)
            # post的变量
            curl_setopt(ch, CURLOPT_POSTFIELDS, post_data)
        output = curl_exec(ch)
        httpCode = curl_getinfo(ch, CURLINFO_HTTP_CODE)
        curl_close(ch)

        echo output  # todo 这个又要改为返回字典

        #分离头部
        #list(header, body) = explode("\r\n\r\n", output, 2)
        datas = explode("\r\n\r\n", output, 2)
        header = datas[0]

        if httpCode == '200':
            body = datas[1]
        else:
            body = ''
        return self.execute( header, body, httpCode )

     #  @param request
     #  @return text | bin
    def execute(self,header = '', body = '', httpCode = '' ):
        exe =  AlipayMobilePublicMultiMediaExecute( header, body, httpCode )
        return exe

    def buildGetUrl(self,query = None ):
        # query 应该是字典类型
        if not is_array( query ) :
            pass

        #排序参数，
        data = self.buildQuery( query )

        # 私钥密码
        passphrase = ''
        key_width = 64

        #私钥
        privateKey = self.privateKey
        p_key = []  # 改 没用上
        # 如果私钥是 1行
        if not stripos(privateKey, "\n") :
            i = 0
            while key_str = substr( privateKey , i *  key_width , key_width) :
                p_key.append(key_str)
                i ++
        else:
            #echo '一行？'
			pass

        privateKey = "-----BEGIN RSA PRIVATE KEY-----\n" + implode("\n", p_key)
        privateKey = privateKey ."\n-----END RSA PRIVATE KEY-----"

        #        echo "\n\n私钥:\n"
        #        echo( privateKey )
        #        echo "\n\n\n"

        #私钥
        private_id = openssl_pkey_get_private( privateKey , passphrase)
        # 签名
        signature = ''
        if "RSA2"==self.sign_type:
            openssl_sign(data, signature, private_id, OPENSSL_ALGO_SHA256 )
        else:
            openssl_sign(data, signature, private_id, OPENSSL_ALGO_SHA1 )

        openssl_free_key( private_id )

        #加密后的内容通常含有特殊字符，需要编码转换下
        signature = base64_encode(signature)
        signature = urlencode( signature )
        #signature = 'XjUN6YM1Mc9HXebKMv7GTLy7gmyhktyOgKk2/Jf+cz4DtP6udkzTdpkjW2j/Z4ZSD7xD6CNYI1Spz4yS93HPT0a5X9LgFWYY8SaADqe+ArXg+FBSiTwUz49SE#Xd9+LEiIRsSFkbpkuiGoO6mqJmB7vXjlD5lx6qCM3nb41wb8='
        out = data + '&'+ self.SIGN +'='+ signature
        #        echo "\n\n 加密后:\n"
        #        echo( out )
        #        echo "\n\n\n"
        return out

    #  查询参数排序 a-z
    def buildQuery(self,query ):
        if  not query :
            return None

        #将要 参数 排序
        ksort( query )
        #重新组装参数
        params = []
        for key in query:
            value = query[key]
            params.append(key +'='+ value)
        data = '&'.join(params)
        return data

















