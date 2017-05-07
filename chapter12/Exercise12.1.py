#coding:utf-8
def sumall(*args):
	'''尝试操作任意数量参数

	:param args: 任意个数字
	:return: 返回全部参数的和
	'''
	tol = 0
	for i in args:
		tol += i
	return tol
print(sumall(1,2,3,4))