# coding:utf-8
def is_abecedarian(word):
	'''如果单词中的字母按照字母顺序出现，则返回True

	:param word:单词
	:return: 布尔值
	'''
	word.lower()
	for letter in word:
		order = ord(letter)
