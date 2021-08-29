# -*- coding: utf-8 -*-
# @Time     :2021/8/28 下午 8:10
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :Lesson3_test.py
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
#     print('如果 表达式为真，则执行')
# if 1==1:
#     print('1==1为真，所以执行')
# if 1==2:#1==2为假，所以不执行
#     print('1==2为假，所以不执行')
# if 1==1 and 2==2:#and 代表并且, 为真，所以执行print('111’)
#     print('111')
# if 1==1 and 2==3:#and 代表并且, 为假，所以不执行print
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
i=10
if i==8:
    print('这是8')#因为不等于8所以不打印
elif i>9:
    print('大于9')
