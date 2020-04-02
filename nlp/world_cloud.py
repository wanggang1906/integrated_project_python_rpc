# -*- coding: utf-8 -*-

# 词云
# 导入分词库
import jieba
# 导入词云库
import wordcloud
import imageio

# 读取本地图片，做为词云的形状图片
mk = imageio.imread("../DataSet/nlp/image/xin.png")
# 构建词云对象w,设置词云图片宽，高，字体，背景颜色等
w = wordcloud.WordCloud(width = 1000,
                        height = 700,
                        background_color = 'white',
                        font_path = 'msyh.ttc',
                        scale = 15,
                        stopwords = {"麦田","守望"})

f = open("../DataSet/nlp/麦田里的守望者.txt",encoding='utf-8')
print(f.read(10))
txt = f.read()

# 对文本进行分词，得到string
txtList = jieba.lcut(txt)
string = "".join(txtList)

#string = " ".join(txtList) # 生成的词云不同

# 将string变量传入w的generate方法，给词云输入汉字
w.generate(string)
# 导出词云图片
w.to_file('../DataSet/nlp/out_img/output71-xin.png')