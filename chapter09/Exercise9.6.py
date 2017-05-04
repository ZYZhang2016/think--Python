# coding:utf-8
def is_abecedarian1(word):
	'''如果单词中的字母按照字母顺序出现，则返回True
	   #使用for循环

	:param word:单词
	:return: 布尔值
	'''
	word.lower()
	letter_curt = word[0]
	for letter in word:
		if letter < letter_curt:
			return False
		letter_curt = letter
	return True


def is_abecedarian2(word):
	'''如果单词中的字母按照字母顺序出现，则返回True
       #使用递归

	:param word:单词
	:return: 布尔值
	'''
	word.lower()
	if len(word)<=1:
		return True
	if word[0]>word[1]:
		return False
	return is_abecedarian2(word[1:])



def is_abecedarian3(word):
	'''如果单词中的字母按照字母顺序出现，则返回True
       #使用while循环

	:param word:单词
	:return: 布尔值
	'''
	word.lower()
	i = 0
	while i < len(word)-1:
		if word[i]>word[i+1]:
			return False
		i += 1
	return True

print(is_abecedarian3('abcde'))
