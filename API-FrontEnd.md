# genEncodings
- 功能: 生成编码
## Params
- Null
## Return
- 'encodedNum':int - 编码的人数 

# faceIdentification
- 功能：人脸识别
## Params
- img:cv2 img - 图片
- location:[top,right,bottom,left] - 人脸的位置，若已知
## Return
- 'person%d': a person dict,have keys&values below
    + 'ID':str - 此人ID
    + 'name':str -此人名字
    + 'dis':float - 此人计算出来的与被搜索人图片的距离
    
 # faceVerification
- 功能：人脸确认
## Params
- imgList: list of cv2 img
## Return
- 'same':bool - 是否为同一个人

# FaceTracker.track
- 功能：检测式追踪人脸
# Params
- img:cv2 img - 视频帧
# Return
- img:框好的追踪结果图像

# SiamFaceTracker.track
- 功能：追踪式追踪人脸
# Params
- img:cv2 img - 视频帧
# Return
- img:框好的追踪结果图像

# SiamBodyTracker.track
- 功能：追踪式追踪人体
# Params
- img:cv2 img - 视频帧
# Return
- img:框好的追踪结果图像

# faceCaper.cap
- 功能：捕获人脸
# Params
- img:cv2 img - 图片或者视频帧
# Return
- img:框好的捕获结果图像

# assement
- 功能：图像质量评价
## Params
- img:cv2 img - 图片
## Return
- 'score':float - 评测分数

# checkEmotion
- 功能：表情检测
## Params
- frame:cv2 img - 检测的一帧图像
- expectEmotion:str - 正确的表情预期
- useTimeLimit:bool - 是否使用超时检测
## Return
- 'predict':str - 在expectEmotion为None时，返回预测结果
- 'pass':bool - 检测结果是否与预期表情一致
- 'error':str - 超时警示信息