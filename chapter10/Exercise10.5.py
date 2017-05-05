#coding:utf-8
import random

def has_duplicate():
    '''若23个学生中，有两个人生日相同，则返回True,使用random模块的rabdint随机生日

    return:布尔值
    '''
    stud = []
    for i in range(0,23):
        stud.append(random.randint(1,365))
    #print(stud)
   # print(len(stud))
    i = 0
    while i<len(stud)-1:
        #print(i)
        if stud[i] in stud[i+1:]:
            return True
        i += 1
    return False

def count_matches(n=100):
    '''重复n次，计算有多少次重复

    :param n:重复has_duplicate的次数
    :return: 返回有重复生日的次数
    '''
    count = 0
    for i in range(n):
        if has_duplicate():
            count += 1
    return count
print(count_matches(10000))
