# -*- coding: utf-8 -*-
# @Time     :2021/8/22 上午 10:21
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :Lesson2.py

# 输出语句
print('hello 喻铁骑')
# 关键字
import keyword
print(keyword.kwlist)

# 语句块 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数,一般默认4个空格， ide都自动识别，快捷键tab也可以实现
# Tab+Shift 去掉缩进
flag = False
name = 'luren'
if name == 'python':         # 判断变量是否为 python
    flag = True              # 条件成立时设置标志为真
    print('welcome boss')      # 并输出欢迎信息
else:
    print(name)              # 条件不成立时输出变量名称

a = 21
b = 10
c = 0
if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")


# 注释(相当于说明)
# 单行注释 #   快捷键 ctrl + /
# 多行注释 """"我是注释""“ '''我是注释'''

# 动态语言，赋值是什么类型的数据就是什么类型
# Number（数字）
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型。
# bool (布尔),  True False。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j 每个数都是一个对象(Object)，
# 在计算机内存中都有自己的一个 “家”(即地址)，这象征着它的身份。
# i = 1
# y = 1.0
# b = True
# 多个变量赋值 a,b,c=1,2,'a'

# String（字符串）
# 单引号和双引号使用完全相同。
# 转义符 \反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 字符串可以用 + 运算符连接在一起。
# test='a\nb'#转译符 \n 表示换行
# test1=r'a\nb' #如 r'a\nb' 则\n会显示，并不是换行。
# print(test)
# print(test1)
# print('aa'+'bb') # 字符串可以用 + 运算符连接在一起。
# #split截取， replace替换
# str='abcdeaghi'
# print(str.split('a')) #结束 ['', 'bcde', 'ghi']
# print(str.replace('a','1'))
# print(str.replace('a','').replace('d','df'))

# list 列表
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
list=['abcd',786,2.23,'runoob',70.2,786];
# list[1]='ccc'#把索引为1的数，改为cccc
# print(list[0]) # abcd
# print(list[1:4])#[786, 2.23, 'runoob']
# list.append('添加元素')#在列表最后面添加一个新的元素
# print(list)
# del list[1]#删除索引为1的元素
# print(list)
# list.pop(1)#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# print(list)
# list1 = ['Google', 'Runoob', 'Taobao']
# list_pop=list1.pop(1)
# print("删除的项为 :", list_pop)
# print("列表现在为 : ", list1)
# list.remove('abcd')#删除值为abcd的元素，多个值时删除第一个
# print(list)
# print(len(list))#len() 统计列表元素个数
# list1=123,456,123
# print(max(list1))#返回列表元素最大值  int和字符串不能进行比较
# print(min(list1))#返回列表元素最小值
aList = [123, 'xyz', 'zara', 'abc', 123];
print(aList.count(123))
print(aList.count('zara'))#count() 方法用于统计某个元素在列表中出现的次数。
print(list.index(2.23))#返回2.23的索引位置
a=[1,3,2,4,6,5]
a.sort()
print(a)
#sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
# 以下实例演示了通过指定列表中的元素排序来输出列表：
# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond)
# 输出类别
print('排序列表：')
print(random)
#元组
# 元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号 ( )，列表使用方括号 [ ]。
# tup1 = ('Google', 'Runoob', 1997, 2000)

# 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2, key3 : value3 }
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
# 键必须不可变

dict={'name':"张三",'age':18}
print(dict)
dict['sex']='男'#赋值，和添加新的键
dict['name']='李只'#修改
print(dict)
print(dict)
del dict['name']# 删除键 'name’
print(dict)
print(len(dict))#函数计算字典元素个数，即键的总数。
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)#remove() 函数用于移除列表中某个值的第一个匹配项。
# 输出结果
print(dict1)
print(dict2)
print(dict3)
dict6 = {'Name': 'Zara', 'Age': 7};
print(str(dict6))# str() 函数将值转化为适于人阅读的形式，以可打印的字符串表示。
# 作业
# 一.“abcdefg”把c移动到f后面
test1='abcdefg'
print(test1.replace('c','').replace('f','fc'))
# 二.“aaccbcccc”取出aacc
test1='aaccbcccc'
print(test1[0:4])
print(test1[:4])
# 三.[1,2,3,4,5,6]在列表后添加‘7’
test2=[1,2,3,4,5,6]
test2.append('7')
print(test2)
# 四.[9,,5,6,3,545]删除3
test3=[9,5,6,3,545]
test3.remove(3)
print(test3)
# 五.['a', 'b', 'a',  '4', '6', '7']统计a出现的次数
test4=['a', 'b', 'a',  '4', '6', '7']
print(test4.count('a'))
# 六.[9,,5,6,3,545]输出列表长度
test5=[9,5,6,3,545]
print(len(test5))
