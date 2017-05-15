#coding:utf-8
class Time(object):
	'''represent time
	attribute:hour,minute,second
	'''

def cal_time(time_obj):
	return time_obj.hour+time_obj.minute/60+time_obj.second/3600

def is_after(t1,t2):
	'''比较t1与t2，如果t1在t2后，返回True,否则返回False

	:param t1: Time1
	:param t2: Time2
	:return: 布尔值
	'''
	time1 = cal_time(t1)
	time2 = cal_time(t2)
	return time1>time2

def main():
	time1 = Time()
	time1.hour = 3
	time1.minute = 56
	time1.second = 31
	time2 = Time()
	time2.hour = 2
	time2.minute = 53
	time2.second = 36
	print(is_after(time1,time2))

if __name__=='__main__':
	main()