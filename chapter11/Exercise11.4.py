#coding:utf-8
def reverse_lookup(dic,val):
	'''通过键值查询键

	:param dic:字典
	:param val: 键值
	:return: 返回包含键值的列表
	'''
	lst = []
	for key in dic:
		if dic[key] == val:
			lst.append(key)
	return lst

dic = {'name':'Holase','age':25,'degree':'Master'}
print(reverse_lookup(dic,24))
