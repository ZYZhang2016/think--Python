#coding:utf-8
dic = {'name':'Holase','age':25,'degree':'Master'}
def sorted_keys(dictionary):
	'''升序输出key

	:param dictionary: 字典
	'''
	keys = dictionary.keys()
	lst = sorted(keys)
	for i in lst:
		print(i,dictionary[i])
sorted_keys(dic)