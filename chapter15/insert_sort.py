#coding:utf-8
def insert_sorted(lst):
	count = len(lst)
	for i in range(1,count):
		print 'i: ',i
		temp = lst[i]
		print 'lst[i]: ', lst[i]
		j = i-1
		while j>=0:
			print 'j: ', j
			print 'lst[j]: ',lst[j]
			if lst[j]>temp:
				lst[j+1] = lst[j]
				lst[j] = temp
			j -= 1
			print '-----'
			print lst
		print '-----------------------'
	return lst

lst = [10,9,8,7,6,5,4,3,2,1]
a = insert_sorted(lst)
print(a)