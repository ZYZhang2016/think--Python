# coding:utf-8
def uses_all(word, letters):
	'''word使用letters中的所有字母(至少一次)，则返回True

	:param word: 被检查的单词
	:param letters: 一串字母
	:return: 布尔值
	'''
	for letter in word:
		if letters.find(letter) == -1:
			return False
	return True


print uses_all('wordz', 'word')