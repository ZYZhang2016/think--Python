#coding:utf-8
import time
#导入单词表
handler = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
start1 = time.clock()
words1 = []
for line in handler:
	word = line.strip()
	words1.append(word)
end1 = time.clock()
#print(len(words1))

def bisect(words,word):
	'''用二分法查找words中出现的word

	:param words: 被搜索的列表
	:param word: 需要查找的元素
	:return:
	'''
	low = 0
	high = len(words)-1
	count = 0
	while low <= high:
		mid = int((low + high) / 2.0)
		count += 1
		if word < words[mid]:
			high = mid - 1
		elif word > words[mid]:
			low = mid + 1
		else:
			return count,mid
	return count,None

print(bisect(words1,'apple'))
