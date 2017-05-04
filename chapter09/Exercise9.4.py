#coding:utf-8
def uses_only(word,letters):
	'''word中的字母全部包含在letters中，则返回True

	:param word: 被检查的单词
	:param letters: 一串字母
	:return: 布尔值
	'''
	for letter in word:
		if letter not in letters:
			return False
	return True
print (uses_only('wo','word'))
