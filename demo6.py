class HumanBeings:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def run(self):
        print(self.name+"正在跑")

    def run_and_jump(self):
        self.run()
        print(self.name+"正在跳")

h = HumanBeings("zhangshan",25,180)


class Scientist:
    def demo(self):
        print(self.name+"科学家")

class Man(HumanBeings,Scientist):
    
    def test(self):
        print(self.name+"正在测试")


if __name__ == '__main__':
    # h = HumanBeings("zhangshan",25,180)
    # h.run()
    m = Man("zhangshan",25,180)
    m.run()
    m.test()
    m.demo()
# class People:
#     def __init__(self, name, age, height, width):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = width

#     def run(self):
#         print(f"{self.name}正在跑")

#     def jump_run(self):
#         self.run()
#         print(f"{self.name}正在跳")


# class Athletes:

#     def high_jump(self):
#         print("跳高")


# class Man(People, Athletes):

#     def boxing(self):
#         print(f"{self.name}")

# m = Man("张三", 25, 180, 160)     #实例化后引用 m 


# if __name__ == '__main__':
#     m = Man("张三", 25, 180, 160)         #虽然引用的都是Man，名字也都是张三，但m 和m2不是同一个对象
#     m2 = Man("张三", 25, 180, 160)

#     m.jump_run()
#     m.high_jump()

#     # p=People("张三",25,180,160)
#     # p.run()
#     # p.jump_run()
#     # print(p.height)
