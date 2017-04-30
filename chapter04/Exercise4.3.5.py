#coding: utf-8
from swampy.TurtleWorld import *
import math
world = TurtleWorld()

def polyline(t,n,length,angle):#t:turtle;n:n边正多边型
	print t
	for i in range(n):
		fd(t,length)
		lt(t,angle)

def polygon(t,n,length):
	angle = 360.0/n
	polyline(t,n,length,angle)

def arc(t,r,angle):#t:turtle;r:r半径;angle:圆弧的角度
	circumference = 2*math.pi*r
	arc_length = circumference*angle/360
	n = int(arc_length/3)+1
	step_length = arc_length/n
	step_angle = float(angle)/n
	polyline(t, n, step_length, step_angle)

bob=Turtle()
bob.delay=0.01
arc(bob,100,90 )
wait_for_user()