age = 18
name = "邢烨锴"
weight = 75.5
stu_id = 1
# 1.今年我的年龄是X岁---整数%d
print('今年我的年龄是%d岁' % age)
# 我的名字是x --字符串%s
print("我的名字是%s" % name)
# 3.我的体重是x公斤 --浮点数%f
print("我的体重是%.2f公斤" % weight)
# 4.我的学号是x
print('我的学号是%d' % stu_id)
# 4.1我的学号是001
print('我的学号是%03d' % stu_id)
# 5.我的名字是x，今年x岁了
print('我的名字是%s,今年%d岁了' % (name,age))
# 5.1我的名字是x，明年x岁了
print('我的名字是%s，明年%d岁了' % (name , age + 1))
# 6.我的名字是x，今年x岁了,体重x公斤，学号是X
print('我的名字是%s，今年%d岁了,体重%.2f公斤，学号是%03d' %(name,age,weight,stu_id))
# 7.拓展，我的名字是x，今年x岁了，体重x斤
print(f'我的名字是{name}，今年{age}岁了，明年{age+1}岁了，体重{weight}斤')
