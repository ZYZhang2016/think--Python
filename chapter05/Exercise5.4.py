# coding: utf-8
from swampy.TurtleWorld import *
import math

world = TurtleWorld()

def koch(t,length):
	'''柯霍曲线

	t: 乌龟
	length:长
	'''
	if length < 3:
		fd(t,length)
		return
	step = length/3.0
	koch(t,step)
	lt(t,60)
	koch(t, step)
	rt(t, 120)
	koch(t, step)
	lt(t, 60)
	koch(t, step)

def snowflake(t,length):
	'''三条柯霍曲线构成一个雪花

	t:乌龟
	length: 长
	'''
	for i in range(3):
		koch(t,length)
		rt(t,120)

bob = Turtle()
bob.delay = 0.01

snowflake(bob,200)

wait_for_user()