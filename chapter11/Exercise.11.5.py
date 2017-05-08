def invert_dic(dictionary):
    inv = {}
    for key,val in dictionary.items():
        inv.setdefault(val,[]).append(key)
    return inv
dic = {'a':1,'b':2,'c':1}
print(invert_dic(dic))
