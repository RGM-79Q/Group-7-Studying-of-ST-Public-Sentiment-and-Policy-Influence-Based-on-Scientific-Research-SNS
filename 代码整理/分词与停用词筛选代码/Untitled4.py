#!/usr/bin/env python
# coding: utf-8

# In[22]:


import jieba
import xlsxwriter

# 待分词的文本路径
sourceTxt = 'D:/txt/First 5.txt'
# 分好词后的文本路径
targetTxt = 'D:/txt/First 5B.txt'

# 对文本进行操作
with open(sourceTxt, 'r', encoding = 'utf-8') as sourceFile, open(targetTxt, 'a+', encoding = 'utf-8') as targetFile:
    for line in sourceFile:
        seg = jieba.cut(line.strip(' '), cut_all = False)
        # 分好词之后之间用空格隔断
        output = ' '.join(seg)
        targetFile.write(output)
        targetFile.write('\n')
    print('写入成功！')


# In[ ]:





# In[26]:


stop = []
standard_stop = []
text = []
after_text = []
file_stop = r'D:/txt/stopword.txt'  # 停用词表
file_text = r'D:/txt/First 5B.txt'  # 要处理的文本集合
with open(file_stop,'r',encoding='utf-8') as f :
    lines = f.readlines()  # lines是list类型
    for line in lines:
        lline  = line.strip('\n')     # line 是str类型
        stop.append(lline)        # 将stop 是列表形式

# stop 的元素是一行一行的 句子,需要进行转化为一个词一行,即下面:
for i in range(0,len(stop)):
    for word in stop[i].split():
        standard_stop.append(word)
# print(standard_stop)
 

# 读取文本集,
with open(file_text,'r',encoding='utf-8') as f :
    lines = f.readlines()
    print(lines)
    for line  in lines:
        # lline = line.strip('\n')
        # print(lline)
        lline = line.split(' ')
        # print(lline)
        for i in lline:
            if i not in  standard_stop:
                after_text.append(i)
                after_text.append(';')

                
                
print(after_text)
 
# 将结果保存在txt中
with open(r'D:/txt/First 5B result.txt','w+',encoding='utf-8')as f :
    for i in after_text:
        f.write(i)


# In[ ]:





# In[ ]:





# In[ ]:




