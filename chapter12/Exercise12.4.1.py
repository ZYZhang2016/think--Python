#coding:utf-8
import time
handler = open('words.txt')
words = []
for line in handler:
	word = line.strip()
	words.append(word)

def bisect(words,word):
	'''二分法查找word是否在words中

	:param words: 一个单词列表
	:param word: 被查找单词
	:return: 返回布尔值
	'''
	low = 0
	high = len(words)-1
	while low <= high:
		mid = int((low + high) / 2.0)
		if word < words[mid]:
			high = mid - 1
		elif word > words[mid]:
			low = mid + 1
		else:
			return True
	return False

def find_plalidrome(words):
	'''查找出words中的所有回文单词

	:param words:单词序列
	:return:返回一个序列，包含所有words中的回文单词
	'''
	i = 0
	plalidrome = {}
	for word in words:
		if bisect(words[i+1:], word[::-1]):
			 plalidrome[i] = word
		i += 1
	return plalidrome
start = time.clock()
print(find_plalidrome(words))
end = time.clock()
print(end-start)
