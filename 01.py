class XueSheng():
    def __init__(self,name='dasag',age=24):
        self.name=name
        self.age=age
    def jiesao(self):
        print('你好我叫{}，我今年{}岁了，欢迎你来调用我'.format(self.name,self.age))
def function():
    print('我和类同级，我是一个函数')
print('我也和类同级')