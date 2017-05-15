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

def increment(t1,t2):
	t = time_to_int(t1)+time_to_int(t2)
	return int_to_time(t)

def main():
	time1 = Time()
	time1.hour = 3
	time1.minute = 56
	time1.second = 31
	time2 = Time()
	time2.hour = 2
	time2.minute = 53
	time2.second = 36
	print_time(increment(time1,time2))

if __name__=='__main__':
	main()