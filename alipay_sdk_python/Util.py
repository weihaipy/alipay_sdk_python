# 替换 php 的同名函数,实现一样的功能
import ast
import base64
import hashlib
import json
import math
import numbers
import pprint
import random
import re
import sys
import textwrap
import time

try:
    from io import BytesIO as StringIO  # python3
except ImportError:  # python2
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

    StringIO = StringIO.StringIO()

try:
    import urllib  # python2

    quote_plus = urllib.quote_plus
except ImportError:  # python3
    import urllib.parse

    quote_plus = urllib.parse.quote_plus

import pycurl

md5 = lambda var: hashlib.md5(var).hexdigest()
strtoupper = lambda var: var.upper()
is_array = lambda var: isinstance(var, (list, tuple))
is_string = lambda var: isinstance(var, str)
strlen = lambda var: len(var)
print_r = pprint.pprint


def array_key_exists(key, dict_arr):
    return key in dict_arr.keys()


def is_numeric(obj):
    if isinstance(obj, numbers.Number):
        return True
    elif is_string(obj):
        nodes = list(ast.walk(ast.parse(obj)))[1:]
        if not isinstance(nodes[0], ast.Expr):
            return False
        if not isinstance(nodes[-1], ast.Num):
            return False
        nodes = nodes[1:-1]
        for i in range(len(nodes)):
            if i % 2 == 0:
                if not isinstance(nodes[i], ast.UnaryOp):
                    return False
            else:
                if not isinstance(nodes[i], (ast.USub, ast.UAdd)):
                    return False
        return True
    else:
        return False


def json_decode(string, assoc, depth, options):
    # 这个php函数可接收多个参数 todo
    return json.loads(string)


def json_encode(string, assoc, depth, options):
    # 这个php函数可接收多个参数 todo
    return json.dumps(string)


def ksort(d):
    return [(k, d[k]) for k in sorted(d.keys())]


def microtime(get_as_float=False):
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())


def mt_rand(low=0, high=0):
    if high == 0:
        try:
            high = sys.maxsize  # python3
        except:
            high = sys.maxint  # python2
    return random.randint(low, high)


def simplexml_load_string(string, classname, options, ns, is_prefix):
    # todo ,基本就是解析 xml
    # 转换形式良好的 XML 字符串为 SimpleXMLElement 对象
    pass


def substr(string, start, length):
    return string[start:start + length]


# 下面注释的是不需要的
CURLOPT_HEADER = pycurl.HEADER
CURLINFO_HTTP_CODE = pycurl.HTTP_CODE
CURLOPT_POST = pycurl.POST
CURLOPT_POSTFIELDS = pycurl.POSTFIELDS
CURLOPT_PROXY = pycurl.PROXY
CURLOPT_PROXYPORT = pycurl.PROXYPORT
# CURLOPT_RETURNTRANSFER = pycurl.RETURNTRANSFER
CURLOPT_SSL_VERIFYPEER = pycurl.SSL_VERIFYPEER
CURLOPT_SSL_VERIFYHOST = pycurl.SSL_VERIFYHOST
CURLOPT_SSLCERTTYPE = pycurl.SSLCERTTYPE
CURLOPT_SSLCERT = pycurl.SSLCERT
CURLOPT_SSLKEYTYPE = pycurl.SSLKEYTYPE
CURLOPT_SSLKEY = pycurl.SSLKEY
CURLOPT_TIMEOUT = pycurl.TIMEOUT
CURLOPT_URL = pycurl.URL


# FALSE = pycurl.FALSE
# TRUE = pycurl.TRUE


def curl_init(url=""):
    c = pycurl.Curl()

    if url:
        c.setopt(c.URL, url)
    return c


def curl_setopt(curl, option, value):
    curl.setopt(option, value)


def curl_exec(curl):
    response = None
    try:
        b = StringIO()
        curl.setopt(pycurl.WRITEFUNCTION, b.write)
        curl.perform()
        response = b.getvalue()
    except Exception as e:
        setattr(curl, "errno", e)
    return response


def curl_errno(curl):
    return getattr(curl, "errno")


def curl_close(curl):
    return curl.close()


def curl_getinfo(curl, *args, **kwargs):
    return


def openssl_sign():
    pass


def openssl_free_key():
    pass


def openssl_get_privatekey():
    pass


def openssl_pkey_get_private():
    pass


def wordwrap(text, width=75, *args, **kwargs):
    return textwrap.wrap(text, width)


def str_replace(find, replace, string, count):
    string.replace(find, replace, count)


def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array + second_array
    elif isinstance(first_array, dict) and isinstance(second_array, dict):
        return dict(list(first_array.items()) + list(second_array.items()))
    elif isinstance(first_array, set) and isinstance(second_array, set):
        return first_array.union(second_array)
    return False


urlencode = quote_plus


def explode(delimiter, string, limit=0):
    if limit:
        return string.split(delimiter, limit)
    else:
        return string.split(delimiter)


def stripos(string, find, start=0):
    return string.find(find, beg=start, end=len(string))


def base64_encode(string):
    try:  # Python 2
        return string.b64encode('base64')
    except:  # Python 3
        return base64.b64encode(string.encode("utf-8"))


def method_exists(class_obj, method_name):
    return hasattr(class_obj, method_name) and callable(getattr(class_obj, method_name))


def trim(string, char=" "):
    return string.strip(char)


def iconv(in_charset, out_charset, string):
    return string.decode(in_charset).encode(out_charset)


def mb_convert_encoding(in_charset, out_charset, string):
    return string.decode(in_charset).encode(out_charset)


def trigger_error(text):
    # todo 用 raise 不太好
    raise ValueError(text)


def class_exists(class_name, autoload):
    # 判断类是否存在怎么搞?  todo
    pass


def preg_match(pattern, string, matches=None, flags=None, offset=0):
    # todo 有的参数没用上
    res = re.search(pattern, string, flags)
    if matches:
        matches = res
    else:
        return res


def preg_match_all(pattern, string, matches, flags, offset):
    # todo 有的参数没用上
    res = re.findall(pattern, string, flags)
    if matches:
        matches = res
    else:
        return res


def implode(separator="", array=None):
    return separator.join(array)


def date(format, timestamp=time.localtime(time.time())):
    return time.strftime(format, timestamp)


def isset(val):
    try:
        if [val]:
            return True
    except Exception:
        return False


def strpos(string, find, start):
    try:
        if start:
            string = string[start:]
        return string.index(find)
    except IndexError:
        return -1


def array_slice(array, offset, length=None):
    if is_array(array) and not isinstance(array, dict):
        if isinstance(array, set):
            array = list(array)
            return set(array[offset:length])
        return array[offset:length]
    return False


def strcasecmp(string1, string2):
    # 比较字符串
    string1 = string1.lower()
    string2 = string2.lower()
    if string1 == string2:
        return 0
    else:
        return len(string1) - len(string2)


def ucfirst(string):
    # 首字母大写
    return string.capitalize()


def mb_detect_encoding(text, encoding_list=None):
    '''Return first matched encoding in encoding_list, otherwise return None.
    See [url]http://docs.python.org/2/howto/unicode.html#the-unicode-type[/url] for more info.
    See [url]http://docs.python.org/2/library/codecs.html#standard-encodings[/url] for encodings.'''
    if not encoding_list:
        encoding_list = ['ascii']
    for best_enc in encoding_list:
        try:
            unicode(text, best_enc)
        except:
            best_enc = None
        else:
            break
    return best_enc
