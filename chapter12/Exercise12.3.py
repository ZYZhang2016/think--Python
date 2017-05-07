#coding:utf-8
import string
def most_frequent(str):
	dic = {}
	inv = {}
	sorted_inv = {}
	newstr = str.lower()
	#遍历字符串，若为字母，在字典中记录频率
	for letter in newstr:
		if letter in string.ascii_letters: #string.ascii_letters保存所有大小写的字母（string.ascii_digits保存数字0-9）
		    dic[letter] = dic.get(letter,0) + 1
	#交换key与value的值，并保存到字典inv中
	for letter,frequence in dic.items():
		inv.setdefault(frequence,[]).append(letter)
	#根据frequency排列
	lst = []
	for i in sorted(inv,reverse=True):
		lst.append((i,inv[i]))
	return lst
print most_frequent('fewfhqpfbcvSvWERBDBASDFKSGHUIWERPGYSDVGLSGVnbvaiuedrgbSDMgvbalgMDncvfbeipugfwfvs')