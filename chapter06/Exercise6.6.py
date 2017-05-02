#coding:utf-8
def first(word):
	return word[0]
def last(word):
	return  word[-1]
def middle(word):
	return word[1:-1]

def is_palidrome(word):
	'''用递归的方法验证输入的单词是否为回文。
	原理。定义回文为：如果第一个字符与最后一个字符相等，且中间的字符为回文

	 word: 需要被验证的值
	return: 返回布尔值
	'''
	if first(word) != last(word):
		#print 'first letter',first(word),'!=','last letter',last(word)
		return False
	elif len(word) <= 3:
		#print 'no more than 3 letters',word
		return True
	else:
	    #print 'middle word',middle(word)
	    return is_palidrome(middle(word))

print is_palidrome('noon')
