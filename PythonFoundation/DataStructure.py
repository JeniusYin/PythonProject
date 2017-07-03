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