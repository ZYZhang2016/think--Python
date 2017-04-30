#coding: utf-8
from swampy.TurtleWorld import *

world = TurtleWorld()

def polygon(t,length,n):#t:turtle;n:n边正多边型
	print t
	for i in range(n):
		fd(t,length)
		angle = 360.0/n
		lt(t,angle)

bob=Turtle()
polygon(bob,100,6)
wait_for_user()