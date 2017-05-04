#coding:utf-8
def chop(list):
	del list[0]
	del list[len(list)-1]
	return None

lst=[1,2,3,4]
print chop(lst)
print lst