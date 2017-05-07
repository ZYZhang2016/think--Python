#coding:utf-8
handler = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
words = []
#找到所有由8个字母组成的单词
for line in handler:
	word = line.strip()
	if len(word)==8:
	    words.append(word)
#print(len(words))
for word in words:
	for letter in word:
