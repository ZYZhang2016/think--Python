#coding:utf-8
import time
handler = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
words = []
for line in handler:
	word = line.strip()
	words.append(word)

def bisect(words,word):
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

def find_plalidrome(words,word):
	i = 0
	plalidrome = {}
	for word in words:
		if bisect(words[i+1:], word[::-1]):
			 plalidrome[i] = word
		i += 1
	return plalidrome
start = time.clock()
print(find_plalidrome(words,word))
end = time.clock()
print(end-start)
