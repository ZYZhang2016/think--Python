#coding:utf-8
import string

#print(string.punctuation)
def read_words(filename):
    '''把文件中的所有单词放到一个列表中

    filename：放在工作目录中的文件的文件名
    '''
    words = []
    fin = open(filename)
    for line in fin:
        #string.punctuation不包含这4个引号"“”’‘’"
        char_remove = string.punctuation+"“”’‘’"
        #循环string.punctuation中的每一个字符，一一替换
        for char in char_remove:
            line = line.replace(char,'')
        for word in line.strip().lower().split():
            if word not in words:
                words.append(word)
    return words

def bisect(word,dictionary):
    '''二分法查找，若word在dictionary中，则返回False;不在则返回True

    word:单个单词
    dictionary:整个字典list
    '''
    low = 0
    high = len(dictionary)-1
    while low <= high:
        mid = int((low+high)/2.0)
        if word < dictionary[mid]:
            high = mid - 1
        elif word > dictionary[mid]:
            low = mid + 1
        else:
            return False
    return True

def find_uniq(words,dictionary):
    '''查询words中的单词是否在dictionary中和粗先，返回由未出现在字典中的单词组成的列表

       words:电子书中所有单词组成的列表
       dictionary:包含所有单词的字典
    '''
    uniq_words = []
    for word in words:
        if bisect(word,dictionary):
            uniq_words.append(word)
    return uniq_words

def main(file1,file2):
    words = read_words(file1)
    edictionary = read_words(file2)
    not_in = find_uniq(words,edictionary)
    return not_in

if __name__=='__main__':
    a = main('twocities.txt','words.txt')
    print(a)
