from os import path
from scipy.misc import imread
import imageio
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import time
stop_words = list()
jieba.load_userdict('ciyunmoban.txt')  # 加载自定义词典
filename = "19baogao.txt"    #需要分词的文本
#sentence_depart = jieba.cut(sentence)  # 分词
stop_f = open(filename, "r", encoding='utf-8') # 创建停用词列表
out_str = ''

# 去停用词
'''with open("fenci1.txt", "w", encoding='utf-8') as fw:
    for word in sentence_depart:
        if word not in stop_words:
            if word != '\t':
                out_str += word
                out_str += " "
                if len(out_str) != 0:
                    fw.write(out_str)
fw.close()
print("end")
'''
for line in stop_f.readlines():
    line = line.strip()
    if not len(line):
        continue

    stop_words.append(line)
stop_f.close

# print(len(stop_words))

f = open(filename, "r", encoding='utf-8')
result = list()
for line in f.readlines():
    line = line.strip()
    if not len(line):
        continue
    outstr = ''
    seg_list = jieba.cut(line, cut_all=False)
    for word in seg_list:
        if word not in stop_words:
            if word != '\t':
                outstr += word
                outstr += " "
                # seg_list = " ".join(seg_list)
    result.append(outstr.strip())
f.close
newfm = filename.strip('.txt') + '2' + ".txt"
with open(newfm, "w", encoding='utf-8') as fw:
    for sentence in result:
        sentence.encode('utf-8')
        data = sentence.strip()
        if len(data) != 0:
            fw.write(data)
            fw.write("\n")

print("end")
time.sleep(4)
d = path.dirname(__file__)  # 返回当前运行脚本下的绝对路径
back_coloring_path = "15.jpg"  # 随意准备一张图片，用来设置词云形状
back_coloring = imageio.imread(path.join(d, back_coloring_path))  # 读取图片

f = open(newfm, 'r', encoding='utf-8').read()  # newfm.txt已经处理好的分词数据
tags = jieba.analyse.extract_tags(f, topK=100, withWeight=False)  # 关键词提取 topK=100 提取TF-IDF权重最大的前100个关键词
text = " ".join(tags)
print(text)

wordcloud = WordCloud(background_color='white',
                      width=2000,
                      height=1000,
                      margin=2,
                      max_words=100,  # 设置最多显示的词数
                      mask=back_coloring,  # 设置词云形状
                      font_path="simhei.ttf",  # 中文词图必须设置字体格式，否则会乱码，这里加载的是黑体
                      random_state=10)  # 设置有多少种随机生成状态，即有多少种配色方案
w = wordcloud.generate(text)  # 传入需画词云图的文本
plt.imshow(w)
plt.axis('off')  # 关闭坐标轴1
plt.show()
