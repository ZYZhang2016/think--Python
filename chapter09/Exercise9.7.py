#coding:utf-8
def is_triple_double(word):
    '''检查word是否有三个连续的双字母

    word:被检查的单词，str
    return：有三个连续双字母则返回True,布尔值
    '''
    count = 0
    i = 0
    while i<len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i += 1
    return False
#print(is_triple_double("wwrrtv"))

def find_triple_double():
    fin = open(r'D:\program\Python27\Lib\site-packages\swampy\words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            count += 1
            print count,word

find_triple_double()
