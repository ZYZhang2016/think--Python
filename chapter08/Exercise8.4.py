#coding:utf-8
def myfind(word,letter,pos):
    '''实现find函数的功能

    word:待搜索的字符串
    letter:需要检索的字母
    pos:起始搜索位置
    '''
    index = pos
    while index < len(word):
        if word[index]==letter:
            return index
        index += 1
    return -1
print(myfind('banana','n',3))
