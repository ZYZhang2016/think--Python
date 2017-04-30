from swampy.TurtleWorld import *

world = TurtleWorld()

def square(turtle,length):
	print turtle
	for i in range(4):
		fd(turtle,length)
		lt(turtle)

bob=Turtle()
square(bob,200)
wait_for_user()