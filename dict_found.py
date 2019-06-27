# _*_ coding=utf-8 _*_


# 字典的创建方法
# 1.直接创建
dic = {'name': 'ric', 'age': 18}

# 2.工厂方法
items = [('name', 'ric'), ('age', 18)]
dic2 = dict(items)

# 3.fromkeys方法
dic3 = {}.fromkeys(('x', 'y'), -1)
print(dic3)
dic5 = {}.fromkeys(('x', 'y'))
print(dic5)
