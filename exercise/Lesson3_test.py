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
try:
    print("2"+2)
except TypeError:
    print("类型错误")