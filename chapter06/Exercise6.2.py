#coding:utf-8
import math
def xiebian(a,b):
	'''计算直角三角形的斜边长

	a:一条直角边长
	b:另外一条直角边长
	return：返回斜边的长
	'''
	return math.sqrt(a**2+b**2)

print xiebian(3,4)