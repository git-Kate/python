# dict1 ={"name":"xiaowang","age":25,"sex":"男"}
# dict2 ={"name":"xiaowang","age":25}       #对比json
# for key in dict2:
#     if key in dict1:
#         if dict1[key]==dict2[key]:
#             print("包含")
#         else:
#             print("不包含")


def test():  #没有返回值，没有参数
    print(111)

def test0(i):  #闭包
    def demo(y):
        print(i+y)
    return demo

def test2(i,y):  #有参数有返回值
    return i*y

def test3(i,y=10,s=10):  #带默认值
    return i*y*s

None

def test4(*i):  #元组
    print(i)

@test0
def test5(**i):  #字典
    print(i)


def my_sum(i,y):
    sum=0
    for p in range(i,y):
        sum=sum+p
    return sum

def sum_of_two_numbers(sum,list):  #例 y=7 list=[1,3,5,4,7,8]  找出list中相加等于7的数
    for i in list:
        if sum-i in list:  #如果7-i 结果包含在list中
            return i,sum-i



if __name__ == '__main__':
    # test()
    # s=test2(10,2)
    # print(s)
    # print(test3(1))
    # print(test3(1,3))
    # print(test3(1,s=10))
    # print(test4(10,2,4,5))
    print(test5(name="333",test="222"))
    # print(test([10,2,4,5]))
    # print(my_sum(1,50))
    # i,y=sum_of_two_numbers(7,[1,3,5,4,7,8])
    # print(i)
    # print(y)


# def summation(x,y):    #求和
#     sum=0
#     for i in range(x,y):
#         sum =sum+i
#     return sum

# def two_sum(y,list):  #例 y=7 list=[1,3,5,4,7,8]  找出list中相加等于7的数
#     for i in list:   
#         if y-i in list:  #如果 7-i 包含在list中   7-3=4 4在list中
#             print(i,y-i)





