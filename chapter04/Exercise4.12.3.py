# coding: utf-8
from swampy.TurtleWorld import *
import math

world = TurtleWorld()

def triangle(t,length,angle):
	'''画出小三角形

	t:turtle
	length:三角形的腰长
	angle: 三角形定焦的角度
	'''
	fd(t,length)
	lt(t,90 + 0.5*angle)
	fd(t,2*length*math.sin(math.radians(angle/2)))#sin()函数接受的参数必须是弧度，radians()函数可以吧角度转为弧度
	lt(t, 90 + 0.5*angle)
	fd(t, length)

def pie(t,n,length):
	for i in range(n):
		triangle(t,length,360.0/n)
		lt(t,180)

def move(t, length):
	"""移动乌龟，且不画轨迹

	t:turtle
	length：移动的距离
	"""
	pu(t)  # 收起笔，不再画轨迹
	fd(t, length)
	pd(t)  # 拿出笔，画轨迹


bob = Turtle()
bob.delay = 0.01

move(bob,-150)
pie(bob,5,100)
move(bob,150)
pie(bob,6,100)
move(bob,150)
pie(bob,7,100)

wait_for_user()