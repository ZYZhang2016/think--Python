#coding:utf-8
def bigger(a,b):
	if a>=b:
		return a
	else:
		return b
def smaller(a,b):
	if a<=b:
		return a
	else:
		return b

def remider(a,b):
	return a%b

def gcd(a,b):
	'''计算出a与b的最大公约数
		原理：欧几里得算法:1.gcd(a,b) = gcd(a,r);2.gcd(a,0) = a/
		r是a除以b的余数

	:param a: 数1
	:param b: 数2
	:return:返回a与b的最大公约数
	'''
	if b==0:
		return a
	r = remider(bigger(a,b),smaller(a,b))
	#print ('r',r)
	return gcd(smaller(a,b),r)
print (gcd(12,18))
