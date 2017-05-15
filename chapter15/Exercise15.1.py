#coding:utf-8

class Rectangle(object):
	'''represent a rectangle
	attribute:width,height,corner
	'''
class Point(object):
	'''represent a 2-d point
	attribute:x,y
	'''

def print_time(t):
	a = '%.2d:%.2d:%.2d' % (t.hour,t.minute,t.second)
	b = '{0}:{1}:{2}'.format(t.hour,t.minute,t.second)
	print(b)

class Time(object):
	'''represent time
	attribute:hour,minute,second
	'''

time = Time()
time.hour = 12
time.minute = 34
time.second = 48

print_time(time)