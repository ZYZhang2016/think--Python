# coding: utf-8
from swampy.TurtleWorld import *

world = TurtleWorld()

def draw(t,length,n):
	if n ==0:
		return
	angle = 50
	fd(t,length*n)
	lt(t,angle)
	draw(t,length,n-1)
	rt(t,2*angle)
	draw(t,length,n-1)
	lt(t,angle)
	bk(t,length*n)

bob = Turtle()
bob.delay = 0.01

draw(bob,5,10)

wait_for_user()