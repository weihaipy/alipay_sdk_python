# 加密工具类
#
#  User: jiehua
#  Date: 16/3/30
#  Time: 下午3:25
#
from alipay_sdk_python.Util import *


#
#  todo 这里的加密解密需要用 pycryptodome 完全重写

#  加密方法
#  @param string str
#  @return string
def encrypt(str, screct_key):
    # AES, 128 模式加密数据 CBC
    screct_key = base64_decode(screct_key)
    str = trim(str)
    str = addPKCS7Padding(str)
    iv = mcrypt_create_iv(mcrypt_get_iv_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC), 1)
    encrypt_str = mcrypt_encrypt(MCRYPT_RIJNDAEL_128, screct_key, str, MCRYPT_MODE_CBC)
    return base64_encode(encrypt_str)


#  解密方法
#  @param string str
#  @return string
def decrypt(str, screct_key):
    # AES, 128 模式加密数据 CBC
    str = base64_decode(str)
    screct_key = base64_decode(screct_key)
    iv = mcrypt_create_iv(mcrypt_get_iv_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC), 1)
    encrypt_str = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, screct_key, str, MCRYPT_MODE_CBC)
    encrypt_str = trim(encrypt_str)

    encrypt_str = stripPKSC7Padding(encrypt_str)
    return encrypt_str


#  填充算法
# todo 应该只是获取块大小,和字符串长度进行计算,得出要填充的长度
#  @param string source
#  @return string
def addPKCS7Padding(source):
    source = trim(source)
    block = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC)

    pad = block - (strlen(source) % block)
    if pad <= block:
        char = chr(pad)
        source += str_repeat(char, pad)

    return source


#  移去填充算法
#  @param string source
#  @return string
def stripPKSC7Padding(source):
    source = trim(source)
    char = substr(source, -1)
    num = ord(char)
    if num == 62:
        return source
    source = substr(source, 0, -num)
    return source


# 下面的是尝试测试上面的功能


from Crypto.Cipher import AES
import Crypto.Random
import base64

"""
参考
https://blog.csdn.net/sevenlater/article/details/50317999
https://blog.csdn.net/s740556472/article/details/78778522
https://gist.github.com/forkd/168c9d74b988391e702aac5f4aa69e41  
"""

pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * \
                chr(AES.block_size - len(s) % AES.block_size)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESUtil:
    """
    todo 目前仅测试 AES, 128 模式加密数据 CBC,未成功
    """

    def __init__(self, mode="ECB"):
        mode = {
            "ECB": AES.MODE_ECB,
            "CBC": AES.MODE_CBC,
            "CFB": AES.MODE_CFB,
            "OFB": AES.MODE_OFB,
            "CTR": AES.MODE_CTR,
            "OPENPGP": AES.MODE_OPENPGP,
            "CCM": AES.MODE_CCM,
            "EAX": AES.MODE_EAX,
            "SIV": AES.MODE_SIV,
            "GCM": AES.MODE_GCM,
            "OCB": AES.MODE_OCB,
        }.get(mode.upper(), None)
        if not mode:
            raise ValueError("请输入 AES 模式")
        self.mode = mode

        self.pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * \
                             chr(AES.block_size - len(s) % AES.block_size)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encryt(self, string, key):
        """加密并返回base64"""
        # key = pad(key)
        if isinstance(key, str):
            key = key.encode("utf-8")

        iv = Crypto.Random.new().read(AES.block_size)
        cipher = AES.new(key, self.mode, iv)

        # x = AES.block_size - (len(string) % AES.block_size)
        # if x != 0:
        #     string = string + chr(x) * x
        string = self.pad(string)

        string = string.encode("utf-8")
        msg = cipher.encrypt(string)
        print("加密的 bytes::", msg)
        msg = base64.b64encode(msg).decode("utf-8")
        return msg

    def decrypt(self, enStr, key):
        key = pad(key)
        if isinstance(key, str):
            key = key.encode("utf-8")

        iv = Crypto.Random.new().read(AES.block_size)
        cipher = AES.new(key, self.mode, iv, nonce=nonce)
        # enStr += (len(enStr) % 4) * "="
        decryptByts = base64.b64decode(enStr)
        # decryptByts = b'\xbc\x06\xa3\xdb|o&x\xaf1\xd5A\xd9K\xf2m'
        print("decryptByts::", decryptByts)

        msg = cipher.decrypt(decryptByts)
        try:
            cipher.verify(tag)
            print("The message is authentic:", msg)
        except ValueError:
            print("Key incorrect or message corrupted")

        print("msg::", msg, len(msg) - 1, msg[len(msg) - 1])

        paddingLen = msg[len(msg) - 1]
        return msg[0:-paddingLen]


if __name__ == "__main__":
    a = AESUtil(mode="CBC")
    print("加密结果:", a.encryt("512345", "1234567812345678"))  # G27DdpctVcUjNDjC8imD8Q==
    print("解密结果:", a.decrypt("DIsAmb5xV5n6AbrggU2w2g==", "1234567812345678"))
