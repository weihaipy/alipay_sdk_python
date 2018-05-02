# ALIPAY API: alipay.open.public.life.msg.send request
#
# @author auto create
# @since 1.0, 2017-01-11 11:21:11
class AlipayOpenPublicLifeMsgSendRequest:
    # 消息分类，请传入对应分类编码值
    category = None
    # 消息正文，html原文或纯文本
    content = None
    # 消息背景图片（目前支持格式jpg, jpeg, bmp），需上传图片原始二进制流，图片最大1MB
    cover = None
    # 消息概述
    desc = None
    # 媒体资讯类生活号消息类型
    msgType = None
    # 消息来源方附属信息，供搜索、推荐使用
    # publish_time（int）：消息发布时间，单位秒
    # keyword_list（String）: 文章的标签列表，英文逗号分隔
    # comment（int）：消息来源处评论次数
    # reward（int）：消息来源处打赏次数
    # is_recommended（boolean）：消息在来源处是否被推荐
    # is_s（boolean）：消息是否实时性内容
    # read（int）：消息在来源处被阅读次数
    # like（int）：消息在来源处被点赞次数
    # is_hot（boolean）：消息在来源平台是否是热门内容
    # share（int）：文章在来源平台的分享次数
    # deadline（int）：文章的失效时间，单位秒
    sourceExtInfo = None
    # 消息标题
    title = None
    # 来源方消息唯一标识；若不为空，根据此id和生活号id对消息去重；若为空，不去重
    uniqueMsgId = None
    # 生活号消息视频时长，单位：秒（视频类消息必填）
    videoLength = None
    # 视频类型消息中视频抽样关键帧截图，视频类消息选填
    videoSamples = None
    # 视频大小，单位：KB（视频类消息必填）
    videoSize = None
    # 视频资源来源id（视频类消息必填），取值限定youku, miaopai, taobao, sina中的一个
    videoSource = None
    # 视频的临时链接（优酷来源的视频消息，该字段不能为空）
    videoTemporaryUrl = None
    # 生活号视频类消息视频id或url（视频类消息必填，根据来源区分）
    videoUrl = None
    apiParas = {}
    terminalType = None
    terminalInfo = None
    prodCode = None
    apiVersion = "1.0"
    notifyUrl = None
    returnUrl = None
    needEncrypt = False

    def setCategory(self, category):
        self.category = category
        self.apiParas["category"] = category

    def getCategory(self):
        return self.category

    def setContent(self, content):
        self.content = content
        self.apiParas["content"] = content

    def getContent(self):
        return self.content

    def setCover(self, cover):
        self.cover = cover
        self.apiParas["cover"] = cover

    def getCover(self):
        return self.cover

    def setDesc(self, desc):
        self.desc = desc
        self.apiParas["desc"] = desc

    def getDesc(self):
        return self.desc

    def setMsgType(self, msgType):
        self.msgType = msgType
        self.apiParas["msg_type"] = msgType

    def getMsgType(self):
        return self.msgType

    def setSourceExtInfo(self, sourceExtInfo):
        self.sourceExtInfo = sourceExtInfo
        self.apiParas["source_ext_info"] = sourceExtInfo

    def getSourceExtInfo(self):
        return self.sourceExtInfo

    def setTitle(self, title):
        self.title = title
        self.apiParas["title"] = title

    def getTitle(self):
        return self.title

    def setUniqueMsgId(self, uniqueMsgId):
        self.uniqueMsgId = uniqueMsgId
        self.apiParas["unique_msg_id"] = uniqueMsgId

    def getUniqueMsgId(self):
        return self.uniqueMsgId

    def setVideoLength(self, videoLength):
        self.videoLength = videoLength
        self.apiParas["video_length"] = videoLength

    def getVideoLength(self):
        return self.videoLength

    def setVideoSamples(self, videoSamples):
        self.videoSamples = videoSamples
        self.apiParas["video_samples"] = videoSamples

    def getVideoSamples(self):
        return self.videoSamples

    def setVideoSize(self, videoSize):
        self.videoSize = videoSize
        self.apiParas["video_size"] = videoSize

    def getVideoSize(self):
        return self.videoSize

    def setVideoSource(self, videoSource):
        self.videoSource = videoSource
        self.apiParas["video_source"] = videoSource

    def getVideoSource(self):
        return self.videoSource

    def setVideoTemporaryUrl(self, videoTemporaryUrl):
        self.videoTemporaryUrl = videoTemporaryUrl
        self.apiParas["video_temporary_url"] = videoTemporaryUrl

    def getVideoTemporaryUrl(self):
        return self.videoTemporaryUrl

    def setVideoUrl(self, videoUrl):
        self.videoUrl = videoUrl
        self.apiParas["video_url"] = videoUrl

    def getVideoUrl(self):
        return self.videoUrl

    def getApiMethodName(self):
        return "alipay.open.public.life.msg.send"

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
