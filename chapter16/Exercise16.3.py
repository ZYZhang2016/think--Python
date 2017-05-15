#coding:utf-8

class Time(object):
	'''represent time
	attribute:hour,minute,second
	'''

def print_time(t):
	a = '%.2d:%.2d:%.2d' % (t.hour,t.minute,t.second)
	b = '{0}:{1}:{2}'.format(t.hour,t.minute,t.second)
	print(b)

def increment(time_obj,seconds):
	time_obj.second += seconds
	if time_obj.second >= 60:
		add_minutes,time_obj.second = divmod(time_obj.second,60)
		time_obj.minute += add_minutes
	if time_obj.minute >= 60:
		add_hour,time_obj.minute = divmod(time_obj.minute,60)
		time_obj.hour += add_hour

def main():
	#定义一个实例
	time1 = Time()
	time1.hour = 3
	time1.minute = 56
	time1.second = 31
	#增加500s
	increment(time1,3600)
	print_time(time1)

if __name__=='__main__':
	main()