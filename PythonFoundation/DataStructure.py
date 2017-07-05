# 列表
a=[23,45,-1,987,728723,45]
a.append(10)
print(a)
a.insert(1,111) #在索引1处插入元素111
print(a)
print(a.count(45)) #45元素出现次数
a.remove(987)
print(a)
a.reverse()
print(a)
b=[55,55,65]
a.extend(b) #向a末尾添加b
print(a)
a.sort()
print(a)

#栈 后进先出
print(a.pop()) 
print(a)
print(a.pop()) 
print(a)

#队列 先进先出
print(a.pop(0))
print(a)

#列表推导式
squares=[]
for x in range(1,10):
	squares.append(x**2)
print(squares)

squares.clear()
squares=[x**2 for x in range(1,10)]
print(squares)

#元组 不可变类型，不能对其中元素进行任何操作
a=(12,)
print(type(a),len(a))

#集合 一个无序不重复元素的集。 基本功能包括测试和消除重复元素
#创建集合
basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} #会除去重复元素
print(basket)
a=set('abcdrasgcja')
b=set('abctyadcb')
print(a,a-b,a|b,a&b,a^b) #可进行运算符操作

#字典 无序的键值对集合。其中键必须是不可变类型，如元祖
data = {'kushal':'Fedora', 'kart_':'Debian', 'Jace':'Mac'}
print(data)
data['parthan']='Ubuntu' #增加新的键值对
print(data)
del data['kushal'] #删除键值对
print(data)
#遍历字典
for x,y in data.items():
	print(x,y)

#获取索引
for i,j in enumerate(['a','b','c']):
	print(i,j)

#同时 遍历两个序列类型zip(),匹配每个序列相同索引的元素
a=['pp','aa']
b=['jj','bb']
for x,y in zip(a,b):
	print(x,y)

s='1234567'
print(s[::-1])

# 过滤出数字并且打印
ss='ajsd112herho44;asd;d178djdkslajdanf2u9ajda2ufkabadjk239kdnk2'
dig=[]
for s in ss:
	if s.isdigit():
		dig.append(s)
print(''.join(dig)[::-1])
