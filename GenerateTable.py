import os
# L = []
# # x代表百位数，y代表十位数，z代表个位数
# for x in range(1,10):  # 百位数最小数为1,
#     for y in range(0,10):
#         for z in range(1,10): # 对称的3位数是101，所以各位数要从1开始
#             if x == z:
#                 L.append(x * 100 + y * 10 + z)
# print(L) # python3 需要print打印到控制台
#
# # -*- coding: utf-8 -*-
#
# print (u'''静夜思
# 床前明月光，
# 疑是地上霜。
# 举头望明月，
# 低头思故乡。''')
#
# 方法一
# originfile=open(r'D:\Study\PyEden\Files\baba.txt') #打开储存数据的文件
# myset=set() #建立集合myset
# for line in originfile.readlines(): #读取文件每一行
#     line = line.strip() #去掉每行前面和后面的空格和换行符
#     myset.add(line) #将数字加入集合，由于集合的唯一性，已有值不会添加
#     result = '","'.join(myset) #逗号隔开，合并集合为一个字符串
# targetfile=open(r'D:\Study\PyEden\Files\son1.txt','w') #打开目标文件写入
# targetfile.write(result) #将结果写入目标文件
# originfile.close() #关闭原始文件
# targetfile.close() #关闭目标文件


# 读入一个多行的文件，给每行的数据加双引号并保存为一行输出
yy = ''
with open(r'D:\Study\PyEden\Files\baba.txt','rb') as lines:
    for line in lines:
        line = "'" + line.decode().replace(os.linesep,"")+"',"+ os.linesep
        yy += line
b = ''.join(yy.split())
with open(r'D:\Study\PyEden\Files\son4.txt','wb') as outfile:
    outfile.write(str.encode(b))

#
# 方法二
# read data from file
# with open(r"D:\Study\PyEden\Files\baba.txt", 'rt') as src:
#     data = [ln.strip() for ln in src]
#
# # distinct data and write to file with ', ' join
# with open(r"D:\Study\PyEden\Files\son2.txt", 'wt') as sto:
#     sto.write('","'.join(list(set(data))))
#
# 方法三
# def hebing2(infile,outfile):
#     with open(infile,'r') as _in_,open(outfile,'w') as _out_:
#         outlist=[]
#         newlist=[l.strip() for l in _in_ ]
#         for item in newlist:
#             if item not in outlist:
#                 outlist.append(item)
#                 outlist=','.join(outlist)
#                 print(outlist,file=_out_)
# hebing2(r"D:\Study\PyEden\Files\baba.txt",r"D:\Study\PyEden\Files\son3.txt")