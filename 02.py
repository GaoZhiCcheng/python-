# 借助于importlib 导入以数字开头的模块
import importlib
# 相当于导入了一个01的模块 赋值给gis
gis = importlib.import_module('01')

stu = gis.XueSheng('sfga',28)

stu.jiesao()