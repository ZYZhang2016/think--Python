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
