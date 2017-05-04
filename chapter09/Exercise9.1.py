#coding:utf-8
fin = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
for line in fin:
	word = line.strip()
	if len(word)>20:
		print word