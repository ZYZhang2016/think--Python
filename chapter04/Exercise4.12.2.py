#coding: utf-8
from swampy.TurtleWorld import *
import math
world = TurtleWorld()

def polyline(t,n,length,angle):
	'''、

	t:turtle
	n:n条边边
	length:边长
	angle：转弯的角度
	'''
	for i in range(n):
		fd(t,length)
		lt(t,angle)

def arc(t,r,angle):
	'''画出一段近似的圆弧

	t:turtle
	r:圆弧所在圆的r半径
	angle:圆弧对应的角度
	'''
	circumference = 2*math.pi*r
	arc_length = circumference*angle/360
	n = int(arc_length/3)+1
	step_length = arc_length/n
	step_angle = float(angle)/n
	polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    """画出一片花瓣（两段圆弧包围）

    t: Turtle
    r: 圆弧所在圆的半径
    angle:  圆弧对应的角度
    """
    for i in range(2):
        arc(t, r, angle)
	lt(t, 180-angle)

def flower(t,n,length,angle):
	'''画有n片花瓣的花

    t:turtle
    n:n片花瓣
    length:圆弧半径
    angle：圆弧的角度
	'''
	for i in range(n):
		petal(t, length, angle)
		lt(t,360.0/n)


def move(t, length):
    """移动乌龟，且不画轨迹

    t:turtle
    length：移动的距离
    """
    pu(t)#收起笔，不再画轨迹
    fd(t, length)
    pd(t)#拿出笔，画轨迹

bob=Turtle()
bob.delay=0.01

move(bob,-100)
flower(bob,7,60.0,60.0)

move(bob,100)
flower(bob,10,40.0,80.0)

move(bob,100)
flower(bob,20,140.0,20.0)

wait_for_user()