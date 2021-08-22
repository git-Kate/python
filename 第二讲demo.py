import keyword
print(keyword.kwlist)

print(1, "aaa", [0, '11'])


if True:
    print("True")
else:
    print("False")
print("11")
""""我是注释"""
'''我是注释'''

print('aaaaa\\naaaa')
print(r'this is a line with \n')
i = 1
y = 1.0
b = True
c = 1 + 2j

a = b = c = 1
a, b, c = 1, 2, "runoob"


str = 'abcdeafghi'


print(str.split('a'))
print(str.replace('b','1' ))
# list列表
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print(list[0])
print(list[1:2])
list[1]='cccc'   #把索引为1的数，改为cccc
list.append('1111')  #在列表最后面添加一个新的元素
list.remove()
list.insert(3, "1111")   #在列表索引3插入数据

del list[1] #删除索引为1的元素
list.pop(1) #删除索引为1的元素,并且返回该元素的值，不添加索引值，则默认删除列表中的最后一个元素
list.remove('abcd')   #删除值为adbc的元素，多个值时删除第一个
len(list)   #列表元素个数
max(list)  #返回列表元素最大值
min(list)  #返回列表元素最小值
list.count('abcd') #统计abcd在列表中出现的次数
list.index(786)   #返回786的索引
list.sort()  #排序
tup1 = ('Google', 'Runoob', 1997, 2000)
print(list)

dict2 = { 'name': 'xiaowang', 'name': 'zhangshan' }
print(dict2)
dict = {'name': 'zhangshan', 'age': 25, 'sex':"男","information": {'height':'180',"weight":160}}
print(dict['name'])
print(dict['information']['height'])
dict['alias']="xiaozhang"
del dict['name'] # 删除键 'name'
dict['parameter']="1111111"
with open("./utils/test.json",'r',encoding='utf8') as load_f:
  dict = json.load(load_f)
json_data=open("./utils/test.json",'r',encoding='utf8')
dict1=json.load(json_data)
print(dict1) #json.load把json转换成python 字典类型
str1=json.dumps(dict1)  #json.dumps把python 字典转换成json,json其实就是字符串

f = open("./utils/test.json", "w", encoding='utf8')
json1 = {
    "name": "王五",
            "age": 18,
            "sex": "男"
}
json.dump(json1, f, ensure_ascii=False)
print("aaa"+"bbbbb")
print("aaa"*2)
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
list = [ 'abcd', '111' , '2.23', 'runoob', '70.2' ]

print(list.count("abcd"))
print(list.index("abcd"))
list.sort()
print(list)
print(29//10 )
list=['111',1,2.0,"ccc"]
print(list[0])
print(list[1:3])
list.append("222")
print(list.pop(0))
print(list)
list.remove("111")
print(list)
list=[1,3,2,5,6,9]
list.sort()
print(list)
dict1={"name":"xiaowang"}
dict1['name']="zhangshan"
dict1["age"]=25
print(dict1)
print(1+2.0)
print("aaa">"bbb")
a, b = 1, 5
a = a+b
print(a)
a = ['1', "aaa", "ccc"]
print(1==2 or 2==2)
print(not(1==1))
list=[1,2,3,4]
print('c' in "aabb")
print("c" not in "ccaa")
print(1 in list)
dict1={"name":"xiaowang"}
print("name" in dict1)

a=[1,2,3,4,5]
if (n:=len(a)):
    print(a)

