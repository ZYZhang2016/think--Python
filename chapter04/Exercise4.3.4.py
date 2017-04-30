#coding: utf-8
from swampy.TurtleWorld import *
import math
world = TurtleWorld()

def polygon(t,length,n):#t:turtle;n:n边正多边型
	print t
	for i in range(n):
		fd(t,length)
		angle = 360.0/n
		lt(t,angle)

def circle(t,r):#t:turtle;r:r半径
	circumference = 2*math.pi*r
	n = int(circumference/3)+1
	length = circumference/n
	polygon(t, length, n)

bob=Turtle()
bob.delay=0.01
circle(bob,100)
wait_for_user()