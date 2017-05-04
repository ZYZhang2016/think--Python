#coding:utf-8
def avoids(word,letters):
	for letter in letters:
		if letter in word:
			return False
	return True
print avoids('word','yd')