# coding:utf-8
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


def uses_all(word, letters):
	'''word使用letters中的所有字母(至少一次)，则返回True

	:param word: 被检查的单词
	:param letters: 一串字母
	:return: 布尔值
	'''
	return uses_only(letters,word)


print uses_all('wordz', 'word')
