#coding:utf-8
def is_palindrome(word):
	'''输入的字符串是回文则返回True

	:param word: 字符串
	:return:布尔值
	'''
	if word.find(word[::-1]) != -1:
		return True
	else:
		return False

#print is_palindrome('weewq')
def find_num():
	for i in range(100000,1000000):
		if is_palindrome(str(i)[-4:]) and \
		   is_palindrome(str(i+1)[-5:]) and \
		   is_palindrome(str(i+2)[1:5]) and \
		   is_palindrome(str(i+3)[0:]):
			print i
find_num()