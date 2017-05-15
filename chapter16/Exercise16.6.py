#coding:utf-8

class Time(object):
	'''represent time
	attribute:hour,minute,second
	'''

def print_time(t):
	a = '{}:{}:{}'.format(str(t.hour).zfill(2), str(t.minute).zfill(2), str(t.second).zfill(2))
	print(a)

def time_to_int(time_obj):
	minute = time_obj.hour*60+time_obj.minute
	second = minute*60+time_obj.second
	return second
def int_to_time(seconds):
	time = Time()
	minutes,time.second = divmod(seconds,60)
	time.hour,time.minute = divmod(minutes,60)
	return time

def mul_time1(time_obj,num):
	return int_to_time(time_to_int(time_obj)*num)

def mul_time2(time_obj,dis):
	return dis/time_to_int(time_obj)

def main():
	time1 = Time()
	time1.hour = 3
	time1.minute = 56
	time1.second = 31

	print_time(mul_time1(time1,4))
	print(mul_time2(time1, 100))

if __name__=='__main__':
	main()