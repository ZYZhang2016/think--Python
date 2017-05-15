#coding:utf-8

import copy

class Time(object):
	'''represent time
	attribute:hour,minute,second
	'''

def print_time(t):
	a = '%.2d:%.2d:%.2d' % (t.hour,t.minute,t.second)
	b = '{0}:{1}:{2}'.format(t.hour,t.minute,t.second)
	print(b)

def increment(time_obj,seconds):
	new_time_obj = copy.deepcopy(time_obj)
	new_time_obj.second += seconds
	if new_time_obj.second >= 60:
		add_minutes,new_time_obj.second = divmod(new_time_obj.second,60)
		new_time_obj.minute += add_minutes
	if new_time_obj.minute >= 60:
		add_hour,new_time_obj.minute = divmod(new_time_obj.minute,60)
		new_time_obj.hour += add_hour
	return new_time_obj
def main():
	#定义一个实例
	time1 = Time()
	time1.hour = 3
	time1.minute = 56
	time1.second = 31
	#增加500s
	new_time1 = increment(time1,3601)
	print_time(new_time1)

if __name__=='__main__':
	main()