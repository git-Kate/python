# -*- coding: utf-8 -*-
# @Time     :2021/8/28 下午 8:10
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :Lesson3.py
# i=10
# if i==10:
#     print('为真')
#冒泡排序
# list=[1,2,3,4,5,6,7,8]
# l=len(list)
# for y in range(l-1):
#     for i in range(l-1-y):
#         if list[i]<list[i+1]:
#             list[i],list[i+1]=list[i+1],list[i]
#         print(list)
#捕获异常写法打印报错信息
# try:
#     print("2"+2)
# except TypeError:
#     print("类型错误")

# if True:
#     print('如果表达式为真，则执行')
# if 1==1:
#     print('1==1为真，所以执行')
# if 1==2:#1==2为假，所以不执行
#     print('1==2为假，所以不执行')
# if 1==1 and 2==2:#and代表并且,为真，所以执行print('111’)
#     print('111')
# if 1==1 and 2==3:#and代表并且,为假，所以不执行print
#     print('222')
# if 1==1 or 1==2:
#     print('or一个为真打印')
# if 1!=2:
#     print('不等于时为真打印')
# if 'a' in 'aaaa':
#     print('in表示包含，aaaa包含a为真时打印')
# if 'a' not in 'aaaa':
#     print('not in表示不包含，不打印')
# list=['aaa','bbb','ccc']
# if 'a' in list:#不包含，为假，所以不执行print('包含')
#     print('包含')
# list = ['aaa', 'bbb', 'ccc']
# if 'aaa' in list:  # 不包含，为假，所以不执行print('包含')
#     print('为真')
# #if条件控制语句
# dict ={'name':'xiaoweng','age':'25'}
# if 'name' in dict:#key打印
#     print('dict为真')
# dict ={'name':'xiaoweng','age':'25'}
# if 'xiaoweng' in dict.values():#value打印
#     print('values值方法打印')
# i=10
# if i==8:
#     print('这是8')#因为不等于8所以不打印
# elif i>9:
#     print('大于9')
# 循环结构是在一定条件下反复执行某段程序的流程结构，被反复执行的程序被称为循环体
# 循环语句是由循环体及循环的终止条件两部分组成的
# 简单来讲，就是重复做一件事
# 例一：输出1到100
# print(1)
# print(2)
# ....
# print(100)
#
# foriinrange(1,101):#循环输出1到100，初始值为1，当i等于101时循环终止
# print(i)
#
# for i in range(1,101):# for in rang(范围值)语法  循环输出1到100，初始值为1，当i等于101时循环终止
#     print(i)
    #遍历列表
# list1=["aaa","ccc","ccca","dddd"]
# for i in list1:
#     print(i)
# 2.
# 遍历字典
# dict1 = {"name": "王五", "age": 18, "sex": "男"}
# for key in dict1:
#     print("{0}：{1}".format(key, dict1[key]))
# print(f"{key}:{dict1[key]}")
# dict1 = {"name": "王五", "age": 18, "sex": "男"}
# for key in dict1.keys():
#     print(key,dict1[key]) 字典取值的方式[]
#     # print(f'{key}{dict1[key]}')  #print(key)  print(dict1[key])

# 例二：求和
# sum=0
# foriinrange(1,51):#1到50的和
# sum=sum+i
# print(sum)
# sum=0
# for i in range(1,51):#1到50的和
#     print(f"{sum}+{i}")#看到计算过程
#     sum=sum+i
#     print(sum)

# 例三：统计列表中重复的数，并打印出下标的方法
# list=[1,3,4,3,3,5,6,7]
# for i in list:
#     if list.count(i)>1:#count统计元素出现次数，如果次数大于1，则说明有重复的数
#         print(list.index(i))
##第一次循环取1，count统计次数等于一，不满足>1的条件，所以不执行print(list.index(i))
#第二次循环取3，count统计次数大于一，满足>1的条件，所以执行print(list.index(i))输出3的下标1
#第三次循环取4，count统计次数等于一，不满足>1的条件，所以不执行print(list.index(i))
#第三次循环取3，count统计次数大于一，满足>1的条件，所以执行print(list.index(i))输出3的下标1
#冒泡排序
# list=[1,2,3,4,5,6,7,8]
# l=len(list)
# for y in range(l-1):
#     print(f"{l}-{1}")
#     for i in range(l-1-y):
#         print(f"{l}-{1}-{y}")
#         if list[i]<list[i+1]:
#             print(list)
#             list[i],list[i+1]=list[i+1],list[i]
# print(list)

#测试
# if 'a' in 'abc':
#     print('包含a')
# list=[1,2,3,4,5,6]
# if 1 in list:
#     print('list包含1')
# dict ={'name':'xiaowemg','age':'25'}
# if 'name' in dict:
#     print(f"{dict['name']}")

# list = ['aaa', 'bbb', 'ccc']
# if 'aaa' in list:  # 不包含，为假，所以不执行print('包含')
#     print('为真')
# list=[1,2,3,4,5,6]
# for i in list:
#     print(i)
# dict ={'name':'xiaoweng','age':'25'}
# for key in dict:
#     print(f"{key}:{dict[key]}")
# sum=0
# for i in range(1,5):
#     sum=sum+1
#     print(sum)
# Python index()
# 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
# 则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# Python count() 方法用于统计字符串里某个字符或子字符串出现的次数。可选参数为在字符串搜索的开始与结束位置。
# list=[1,3,4,3,3,5,6,7]#统计列表中重复的数，并打印出下标的方法
# for i in list:
# # print(list.count(3))
#     if list.count(i)>1:#统计字符串出现次数
#         print(list.index(i))

# Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
# #冒泡排序
# list=[1,2,3,4,5,6,7,8]
# l=len(list)
# for i in range(l - 1):
#     for y in range(l-1-i):
#             if list[y]<list[y+1]:
#                 list[y],list[y+1]=list[y+1],list[y]
# print(list)
# 异常处理
# 捕捉异常可以使用try/except语句。
# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 如果你不想在异常发生时结束你的程序，只需在try里捕获它。
# 语法：
# 以下为简单的try....except...else的语法：
# try:
# <语句>        #运行别的代码
# except <名字>：
# <语句>        #如果在try部份引发了'name'异常
# except <名字>，<数据>:
# <语句>        #如果引发了'name'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生
# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print("Error: 没有找到文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()
# try:
#     print("2"+2)
# except TypeError:#如果发生TypeError异常，则执行下面的语句
#     print('数字与字符串不能相加')
# try:
#     print("2"+2)
# except Exception as e:#统计所有的异常
#     print('统计所有的异常',e)
