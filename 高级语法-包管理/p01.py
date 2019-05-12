# 包含一个学生类
# 一个sahello函数
# 一个打印语句
class Student():
    def __init__(self,name='gaoi',age=18):
        self.name = name
        self.age = age


    def say(self):
        print('My name is {0},age{1}'.format(self.name,self.age))
def sayhello():
    print('sahello')
print('我是p01模块，你叫我做什么')