#coding:utf-8
import math

class Point(object):
	'''represent a 2-d point
	attribute:x,y
	'''

def distance(point1,point2):
	x_differ = point1.x - point2.x
	y_differ = point1.y - point2.y
	return math.sqrt(x_differ**2+y_differ**2)

def main():
	first = Point()
	first.x = 4
	first.y = 18
	second = Point()
	second.x = 76
	second.y = 32
	print distance(first,second)

if __name__=='__main__':
	main()