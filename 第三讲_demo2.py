import json

# json_data=open("./test.json","r",encoding='utf8')
# json1=json.load(json_data)
# json1['name']="zhangshan"
# print(json1)
# str='{"name":"xiaowang","age":23}'
# print(json.loads(str))
# print(type(json.loads(str)))
# dict1={"name":"xiaowang","age":23}
# print(type(dict1))
# print(type(json.dumps(dict1)))

# json_data=open("./test.json","r",encoding='utf8')
# json1=json.load(json_data)
# json1['name']="zhangshan"
# new_json_data=open("./test.json","w",encoding='utf8')
# json.dump(json1,new_json_data)

# print("aaa{0}{1}".format("zhao",111))
# name="xiaowen"
# print(f"{name}")

# i=10
# if i==9:
#     print("这不是9")
# elif i==8 and i==7:
#     print("不是8，7")
# else:
#     print(f"{i}")

# list=["aaa","bbb","ccc","ddd"]
# for i in list:
#     print(i)
#     if i=="ccc":
#         print(f"我是:{i}")
#         break;
# dict1={
#     "name": "zhangshan",
#     "age": 25
# }

# for key in dict1:
#     print(f"{key}:{dict1[key]}")

# for i in range(1,11):
#     print(i)

# list=[9,8,7,6,5,4,3,1]
# l=len(list)-1
# for y in range(l):
#     for i in range(l-y):
#         if list[i]>list[i+1]:
#             list[i],list[i+1]=list[i+1],list[i]
#     print(list)
# try:
#     print(list[len(list)])
# except Exception as e:
#     print("下标太长了",e)


# json_data = open("./test.json", 'r', encoding='utf8')
# json1=json.load(json_data)
# json1['user'][0]['name']="xiaoli"
# print(type(json1))


# f= open("./test2.json",'w', encoding='utf8')
# json.dump(json1,f)

# str='{"name":"xiaowang"}'
# json.loads(str)
# str=json.dumps({"name":"zhaowen"})
# print(type(str))
# i=10
# if i==8:
#     print("这是8")
# elif i==9:
#     print("这是9")
# else:
#     print("不是8也不是9")

# list1=["aaa","ccc","ccca","dddd"]
# for i in list1:
#     print(i)

# dict1={"name":"王五","age":18,"sex":"男"}
# for key in dict1:
#     print("{0}：{1}".format(key,dict1[key]))
#     print(f"{key}:{dict1[key]}")

# for i in range(1,10):
#     print(i)


# try:
#     print("2"+2)
# except TypeError:
#     print("数字与字符串不能相加")


# try:
#     print("2"+2)
# except Exception as e:
#     print("数字与字符串不能相加",e)

# def ride(i,y):
#     m=i*y
#     return m

# def ride(i,y=10):
#     m=i*y
#     return m

# def ride(*i):
#     m=i[0]*i[1]
#     return m

# def ride(**i):
#     m=i['name']+i['age']
#     return m

def test(i):
    def deom():
        i()
        print("test方法")
    return deom


@test
def get():
    print("111")


# def output(i):
#     print(i)
#     i += 1
#     if i < 10:
#         output(i)

# def test(i,y):
#     print(i+y)

# def test2(i,y):
#     sum=i+y
#     return sum

# def test3(*i):
#     print(i)

# def test4(**dict):
#     print(dict)
def test5(i):
    print(i)
    i+=1
    if i<10:
        test5(i)



if __name__ == '__main__':
    # sum=test2(1,10)
    # print(sum)
    # test3(1,2,3,45)
    # test4(name="xiao",age="18")
    test5(1)

    # get()
    # list=[1,2,4,9,7,5,3]
    # l=len(list)
    # for i in range(l-1):
    #     for y in range(l-1-i):
    #         if list[y]>list[y+1]:
    #             list[y],list[y+1]=list[y+1],list[y]
    # print(list)
    # output(1)
    # json_data = open("./utils/test.json", 'r', encoding='utf8')
    # print(json.load(json_data))

    # json_data=open("./utils/test.json",'r',encoding='utf8')
    # dict1=json.load(json_data)
    # print(dict1) #json.load把json转换成python 字典类型
    # str1=json.dumps(dict1)  #json.dumps把python 字典转换成json,json其实就是字符串

    # f = open("./utils/test.json", "w", encoding='utf8')
    # json1 = {
    #     "name": "王五",
    #             "age": 18,
    #             "sex": "男"
    # }
    # json.dump(json1, f, ensure_ascii=False)
    pass