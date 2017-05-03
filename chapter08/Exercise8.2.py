#coding:utf-8
prefixes = 'JKLMNOPQ'
suffix = 'ack'
spec='uack'

for letter in prefixes:
    if letter == 'O' or letter == "Q":
        print(letter+spec)
    else:
        print(letter+suffix)
