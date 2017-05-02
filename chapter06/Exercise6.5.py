#coding:utf-8
import math

def ack(m,n):
	'''计算Ackerman公式

	m:数1
	n:数2
	return:返回计算值
	'''
	if m==0:
		return n+1
	elif m>0 and n==0:
		return ack(m-1,1)
	elif m>0 and n>0:
		return ack(m-1,ack(m,n-1))

print ack(3,4)
