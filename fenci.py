# encoding=utf-8
import jieba

filename = "ciyunmoban.txt"
stopwords_file = "baidu_stopwords.txt"
jieba.load_userdict("dict.txt")
stop_f = open(stopwords_file, "r", encoding='utf-8')
stop_words = list()
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

with open("gp2.txt", "w", encoding='utf-8') as fw:
    for sentence in result:
        sentence.encode('utf-8')
        data = sentence.strip()
        if len(data) != 0:
            fw.write(data)
            fw.write("\n")

print("end")