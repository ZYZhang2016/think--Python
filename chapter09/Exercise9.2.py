#coding:utf-8
def has_no_e(word):
	for letter in word:
		if letter.lower() == 'e':
			return False
	return True
fin = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
count = 1
for line in fin:
	word = line.strip()
	if has_no_e(word):
		print count,word
		count += 1