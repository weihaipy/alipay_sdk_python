# alipay-sdk_python
基于支付宝官方 alipay-sdk-PHP-3.0.0 翻译 python 版本

# 注意,翻译尚未完成 

**欢迎参与翻译** **欢迎 star** **欢迎 fork** 

## 缘由:
* 我热爱 python
* 官方提供 php ,二没有python 版本
* php 和 python 都是动态类型语言
* php 转换为 python 相对比较容易

# 目标
* 基本按 php 版本的结构逐行进行翻译,尽量少修改代码结构,便于同步更新 php 版本
* 方法和变量名保持不变
* 除特别的地方外,用法几乎和官方的一样
* 做成有通用意义的 python 模块,不依赖特定 web 框架

# 感谢
* www.php2python.com 提供了大量的 php 转python 的函数,简化了很多工作

## 翻译原则
* 基本语法
* 替换可直接替代的函数
* 不能直接替代的手写一个 python 版的同功能函数

## 区别
* php 中很多使用指针的情况,在python 中有所不同,有的时候需要修改实现形式
    
# 建议
    

# 进度
* [*]复制文件结构
* [*]语法翻译
* [ ]替换同名函数
* [ ]实现逻辑,目前有些没完成
* [ ]测试

# 问题:
* 由于注释太多,没有全部改为 python 标准的 docstring 形式

# TODO
替换同名函数
AlipayMobilePublicMultiMediaClient.py
AlipayMobilePublicMultiMediaExecute.py
AopClient.py
AopSdk.py


# 吐槽
文件太多了,翻译起来比较麻烦

# demo 参照 https://docs.open.alipay.com/54/103419/
用法和 php 版本的一样,,只是由于目录结构的原因导致导入的时候代码较长,仅以普通调用为例:

```python
import alipay_sdk_python
c =  alipay_sdk_python.aop.AopClient.AopClient()
c.gatewayUrl = "https://openapi.alipay.com/gateway.do"
c.appId = "app_id"
c.rsaPrivateKey = '请填写开发者私钥去头去尾去回车，一行字符串' 
c.format = "json"
c.charset= "GBK"
c.signType= "RSA2"
c.alipayrsaPublicKey = '请填写支付宝公钥，一行字符串'
#实例化具体API对应的request类,类名称和接口名称对应,当前调用接口名称：alipay.open.public.template.message.industry.modify
request = alipay_sdk_python.aop.request.AlipayOpenPublicTemplateMessageIndustryModifyRequest.AlipayOpenPublicTemplateMessageIndustryModifyRequest()
#SDK已经封装掉了公共参数，这里只需要传入业务参数
#此次只是参数展示，未进行字符串转义，实际情况下请转义
request.bizContent = "{" +
"    \"primary_industry_name\":\"IT科技/IT软件与服务\"," + \
"    \"primary_industry_code\":\"10001/20102\"," + \
"    \"secondary_industry_code\":\"10001/20102\"," + \
"    \"secondary_industry_name\":\"IT科技/IT软件与服务\"" + \
" }"
response= c.execute(request)
```