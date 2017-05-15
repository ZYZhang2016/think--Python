#coding:utf-8
import copy

class Point(object):
	'''一个二维的点
	'''


class Rectangle(object):
	'''定义一个矩形的点和长宽
	attribute：height，width,corner
	'''

def print_point(p):
	print('(%g, %g)' % (p.x, p.y))

def deep_move_corner(box, dx, dy):
	'''返回一个移动corner后的新矩形

	:param box: Recyangle()对象
	:param dx: x轴方向移动距离
	:param dy: y轴方向移动距离
	:return: 返回移动后的新矩形
	'''
	box2 = copy.deepcopy(box)
	box2.corner.x += dx
	box2.corner.y += dy
	return box2


def main():
	box = Rectangle()
	box.corner = Point()
	box.corner.x, box.corner.y = 3, 7
	box.height, box.height = 10, 20
	moved_rect = deep_move_corner(box, 36, 75)

	print_point(moved_rect.corner)

if __name__ == '__main__':
	main()