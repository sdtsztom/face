# genEncodings
- 功能: 生成编码
## Params
- Null
## Return
- `encodedNum`:int - 编码的人数 

# faceSearchCompare
## Params
- img: 图片
- location：人脸的位置，若已知格式为[top,right,bottom,left]
## Return
- 'person%d': a person dict,have keys&values below
    + 'ID':str - 此人ID
    + 'name':str -此人名字
    + 'dis':float - 此人计算出来的与被搜索人图片的距离