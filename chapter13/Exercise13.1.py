#coding:utf-8
import string
import collections

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
            words.append(word)
    return words

def count_word(words):
    '''对单词计数保存到字典，按照频率大小，排序返回一个元组组成的列表

       words:一个字符串组成的列表
    '''
    dic = {}
    for word in words:
        dic[word] = dic.get(word,0) + 1

    dic_od = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    return dic_od


if __name__=='__main__':
    words = read_words('twocities.txt')
    words_dic = count_word(words)
    print(words_dic)
