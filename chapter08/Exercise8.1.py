#coding:utf-8
def revs_print(word):
    '''倒序打印字符串,每行一个字符

    word:字符串
    '''
    for letter in word[::-1]:
        print(letter)

revs_print('abcdefg')
