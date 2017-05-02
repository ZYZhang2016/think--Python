def is_triangle(a,b,c):
	'''
	检查输入的三个整数是否能构成一个三角形

	param a: 边长1
	param b: 边长2
	param c: 边长3
	return: 返回是否能构成三角形的结布尔值
	'''
	test1 = a+b-c
	test2 = a+c-b
	test3 = b+c-a
	if test1>0 and test2>0 and test3>0:
		print("Yes")
	else:
		print("No")

is_triangle(3,4,1)