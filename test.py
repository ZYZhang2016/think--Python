#coding：utf-8

handler = open('words.txt')
words = []
for word in handler:
    word = word.strip()
    words.append(word)

if "impenitently" in words:
    print("I am wrong")
