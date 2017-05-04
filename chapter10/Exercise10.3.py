#coding:utf-8
def is_sorted(list):
	'''如果列表中的对象升序排列，则返回True

	:param list:对象可排序的列表
	:return: 布尔值
	'''
	i = 0
	while i < len(list)-1:
		if list[i] > list[i+1]:
			return False
		i += 1
	return True

print is_sorted([1,2,3,1])