#coding:utf-8
import math

def is_between(x,y,z):
	'''计算是否x<y<z

	x:数1
	y:数2
	z:数3
	return：返回布尔值
	'''
	if x<y<z:
		return True
	else:
		return False

print is_between(3,6,5)