#coding:utf-8
class Point(object):
	'''一个二维的点
	'''

class Rectangle(object):
	'''定义一个矩形的点和长宽
	attribute：height，width,corner
	'''

def move_corner(box,dx,dy):
	'''移动矩形boxde1corner

	:param box: Recyangle()对象
	:param dx: x轴方向移动距离
	:param dy: y轴方向移动距离
	:return: 返回移动后的矩形
	'''
	box.corner.x += dx
	box.corner.y += dy
	return box

def main():
	box = Rectangle()
	box.corner = Point()
	box.corner.x,box.corner.y = 3,7
	box.height,box.height = 10,20
	move_corner(box,36,75)

	print(box.corner.x,box.corner.y)

if __name__=='__main__':
	main()