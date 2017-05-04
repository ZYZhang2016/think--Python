#coding:utf-8

def rotate_letter(letter,n):
	'''字母letter被旋转n个位置

	:param letter:需要旋转的字母
	:param n: 移动n位
	:return: 返回旋转后的字母
	'''
	if letter.isupper():
		start = ord('A')
	elif letter.islower():
		start = ord('a')
	else:
		return letter
	pos_cur = ord(letter)-start
	pos_rot = (pos_cur+n)%26 +start  #这一步好厉害呀，移动一个单位，超出便捷后返回到队列开头，可以用这个方法
	return chr(pos_rot)

def rotate_word(word,n):
	'''ROT13加密法，单词中每个字母按照字母表移动n位

	:param word:需要被旋转的单词
	:param n: 旋转n个位置
	:return: 返回旋转后的单词
	'''
	word_rot = ''
	for letter in word:
		word_rot += rotate_letter(letter,n)
	return word_rot

print(rotate_word('melon',-10))