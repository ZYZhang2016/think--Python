#coding:utf-8
def remove_duplicate(lst):
	'''返回列表中唯一的元素

	:param list:一个列表
	:return: 返回一个列表
	'''
	newlst = []
	for ele in lst:
		if lst.count(ele) == 1:
			newlst.append(ele)
	return newlst
lst = ['1','1','2','3','1']
print remove_duplicate(lst)