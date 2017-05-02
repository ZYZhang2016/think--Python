#coding:utf-8
import math
import time
def square_newton(a):
	'''用牛顿法求平方根

	:param a: 待开方的数
	:return:返回a的平方根
	'''
	x = a/2.0
	while True:
		print (x)
		y = 0.5*(x+a/x)
		if abs(y-x) < 0.0001:
			break
		x = y
square_newton(0.3)

def square_erfenfa(a):
	'''用二分法求平方根

	:param a: 待开方的数
	:return:返回a的平方根
	'''

	if (a/2.0)**2 == a:
		print (a)
	x = 0
	while True:
		y = (a+x)/2.0
		print (y)
		if y**2 > a:
			x = y
		elif x**2 < a:
			a = y

#square_erfenfa(3)