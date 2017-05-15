#coding:utf-8
class Date(object):
	'''represent time
	attribute:year,month,day
	'''

def print_date(t):
	a = '{}:{}:{}'.format(str(t.year), str(t.month).zfill(2), str(t.day).zfill(2))
	print(a)

def is_leap_year(year):
	if year%4==0 and year%100!=0:
		return True
	elif year%400==0:
		return True
	else:
		return False

def increment_date(date_object,num):
	days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
	days_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

	return

'''
leap_year=[]
for i in range(3000):
	if is_leap_year(i):
		leap_year.append(i)
print(leap_year)
'''