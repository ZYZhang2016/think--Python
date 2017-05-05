#coding:utf-8
import time

def func1():
	handler = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
	start1 = time.clock()
	words1 = []
	for line in handler:
		word = line.strip()
		words1.append(word)
	end1 = time.clock()
	print('func1: %3f' % (end1 - start1))
	return words1

def func2():
	handler = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
	words2 = []
	for line in handler:
		word = [line.strip()]
		words2 = words2 + word
	print('func1: %3f' % (end2 - start2))
	return words2

a = func1()
print(a)


