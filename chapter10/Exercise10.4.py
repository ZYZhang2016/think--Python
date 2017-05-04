#coding:utf-8
def is_anagram(word1,word2):
	'''word1字母重排列后能够构成word2(两者拥有完全相同的字母)

	:param word1: 字符串1
	:param word2: 字符串2
	:return: 布尔值
	'''
	if len(word1) !=len(word2):
		return False
	list1 = list(word1)
	list2 = list(word2)
	list1.sort()
	list2.sort()
	if list1 != list2:
		return False
	else:
		return True
print is_anagram('word','orwdd')