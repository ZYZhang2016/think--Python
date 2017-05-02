def check_fermat(a,b,c,n):
	'''
	验证费马定律（不存在这样的整数a,b,c使得对于n大于2，a**n+b**n==c**n

	a:左边整数1
	b:左边整数2
	c:右边整数
	n:幂
	return:返回验证结果的布尔值
	'''
	left = a**n + b**n
	right = c**n
	if left==right:
		print("Holy smokes,Fermat was wrong!")
	else:
		print("No,that doesn't work.")

check_fermat(3,4,5,3)
