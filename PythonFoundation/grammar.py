# 计算1/x+1/(x+1)+1(x+2)+...+1/n
sum = 0
for i in range(1,11):
	sum+=1/i
	print("{:2d} {:6.4f}".format(i,sum))


import math
def caculate_quadratice(a,b,c):
	d=b*b-4*a*c
	if d<0:
		print('error')
	else:
		root1=(-b+math.sqrt(d))/(2*a)
		root2=(-b-math.sqrt(d))/(2*a)
		print("root1= ",root1)
		print("root2= ",root2)

caculate_quadratice(5,-4,0)

def calcu_circle_area(r):
	print("circle area:" ,'{:.10f}'.format(math.pi*r*r))
calcu_circle_area(2)

# 循环
a,b=0,1
while b<100:
	print(b,end='  ')
	a,b=b,a+b

i=1
print('-'*50)
while i<11:
	n=1
	while n<10:
		print('{:4d}'.format(i*n),end='  ')
		n+=1
	print()
	i+=1
print('-'*50)

a=['I','Love','U']
for x in a:
	print(x,end=' ')
else:
	print('bye')

print()
print(list(range(1,5)))
print(list(range(1,15,2)))
print(list(range(4,20,3)))