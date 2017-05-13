#coding:utf-8
import math

class Point(object):
	'''一个二维的点
	'''

def distance(q,p):
	x_diff = q.x - p.x
	y_diff = q.y - p.y
	distance = math.sqrt(x_diff**2+y_diff**2)
	return distance

def main():
	first = Point()
	first.x,first.y = 3,7
	second = Point()
	second.x,second.y = 4,8

	print(distance(first,second))

if __name__=='__main__':
	main()