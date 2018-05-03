#  多媒体文件客户端
#  @author yuanwai.wang
#  @version Id: AlipayMobilePublicMultiMediaExecute.php, v 0.1 Aug 15, 2014 10:19:01 AM yuanwai.wang Exp


# namespace alipay\api
from alipay_sdk_python.Util import *


class AlipayMobilePublicMultiMediaExecute:
    code = 200
    msg = ''
    body = ''
    params = ''

    fileSuffix = {
        "image/jpeg": 'jpg',  # +
        "text/plain": 'text'
    }

    #  @header : 头部
    def __init__(self, header, body, httpCode):
        self.code = httpCode
        self.msg = ''
        self.params = header
        self.body = body

    #  @return text | bin
    def getCode(self):
        return self.code

    #  @return text | bin
    def getMsg(self):
        return self.msg

    #  @return text | bin
    def getType(self):
        subject = self.params
        pattern = '/Content\-Type:([^;]+)/'
        matches = []  # todo 测试引用的用法是否正常
        preg_match(pattern, subject, matches)
        if matches:
            type = matches[1]
        else:
            type = 'application/download'

        return str_replace(' ', '', type)

    #  @return text | bin
    def getContentLength(self):
        subject = self.params
        pattern = '/Content-Length:\s# ([^\n]+)/'
        matches = []  # todo 测试引用的用法是否正常
        preg_match(pattern, subject, matches)
        return matches[1] if matches[1] else ""

    def getFileSuffix(self, fileType):
        type = self.fileSuffix[fileType] if fileType in self.fileSuffix else 'text/plain'
        if not type:
            type = 'json'

        return type

    #  @return text | bin
    def getBody(self):
        # header('Content-type: image/jpeg')
        return self.body

    #  获取参数
    #  @return text | bin
    def getParams(self):
        return self.params
