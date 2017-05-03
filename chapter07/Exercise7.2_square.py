#coding:utf-8
import math
import time
def square_newton(a,epsilon=0.001):
	'''用牛顿法求平方根

	:param a: 待开方的数
	:return:返回a的平方根
	'''
	assert a >= 0,'a应该为非负数'
	x = a/2
	count = 0
	while True:
		print (count,x)
		y = 0.5*(x+a/x)
		count += 1
		if abs(y-x) < epsilon:
			break
		x = y
	return x
print(square_newton(3000))
#print(math.sqrt(3))

def square_erfenfa(a,epsilon=0.001):
	'''用二分法求平方根

	:param a: 待开方的数
	:return:返回a的平方根
	'''
	floor = 0
	ceiling = a
	count = 0
	x = (floor+ceiling)/2
	if x*x == a:
		return x
	while abs(a-x*x)>epsilon:
		print(count,x)
		count += 1
		if x*x > a:
			ceiling = x
			x = (floor+ceiling)/2
		else:
			floor = x
			x = (floor+ceiling)/2
	return x
print(square_erfenfa(3000))
