# 异常处理
# 不能保证程序正常运行
# 但是，必须保证程序在最坏的情况下得到的问题被妥善处理
# python的异常处理模块全部语法为：
# 简单异常案例
try:
    num = int(input("Plz input your number:"))
    rst = 100 / num
    print("计算结果是： {0}".format(rst))
except:
    print("你特娘的输入的啥玩意儿")
    # exit是退出程序的意思
    num = int(input("Plz input your number:"))
    rst = 100 / num
    print("计算结果是： {0}".format(rst))
    exit()
