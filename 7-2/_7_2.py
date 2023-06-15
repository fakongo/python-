print('\u80e1\u6653\u9f99')
print('我是\u80e1\u6653\u9f99')

print('ni\hao')
print('\101')
print('\x41')

x='%s' % set(range(5))
print(x)

print("数值{0:,}在十六进制是{0:#x},在八进制是{0:#o}".format(55))
print("我的名字是{姓名},我的年龄是{年龄},我的QQ是{qq}".format(姓名="大傻",qq="114514",年龄="18"))
print('{0:_},{0:_x}'.format(10000000))

name='chougou'
age=18
print(f'我的名字是{name},我的年龄是{age}')
width=10
precisult=4
value=11/3
print(f'result:{value:{width}.{precisult}}')
