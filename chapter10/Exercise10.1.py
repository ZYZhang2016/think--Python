#coding:utf-8
def sumlst(list):
	sumlist = []
	sumlist.append(list[0])
	i = 0
	while i<len(list)-1:
		print i
		total = sumlist[i] + list[i+1]
		print total
		sumlist.append(total)
		print sumlist
		i += 1
	return sumlist
sumlst([1,2,3,4,5,6])