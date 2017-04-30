from swampy.TurtleWorld import *

world = TurtleWorld()

def square(t,angle):
	print t
	fd(t,100)
	lt(t, 90 + 0.5 * angle)

bob = Turtle()
square(bob,60)

wait_for_user()