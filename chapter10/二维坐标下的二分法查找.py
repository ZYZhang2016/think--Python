#coding:utf-8
def bisect(x,y):
	'''输入一个x，y坐标对，在x轴0~1000，y轴0~1000下，查找到x.y的具体位置

	:param x: x轴坐标
	:param y: y轴坐标
	:return: 返回搜索的次数，打印m每一步出现的x轴中值和y轴中值
	'''
	ceil = 1000
	floor = 0
	left = 0
	right = 1000
	count = 1
	while floor <= ceil and left <= right:
		x_mid = int((left + right) / 2.0)
		y_mid = int((floor + ceil) / 2.0)
		print(count,x_mid,y_mid)
		count += 1
		if y < y_mid and x < x_mid:
			ceil = y_mid - 1
			right = x_mid - 1
		elif y > y_mid and x > x_mid:
			floor = y_mid + 1
			left = x_mid + 1
		elif y < y_mid and x > x_mid:
			ceil = y_mid - 1
			left = x_mid + 1
		elif y > y_mid and x < x_mid:
			floor = y_mid + 1
			right = x_mid - 1
		else:
			return count
	return

print(bisect(1,5))