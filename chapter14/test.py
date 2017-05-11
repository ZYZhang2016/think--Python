import os
#print(os.getcwd())

handler = open('words.txt')
words = []
for line in handler:
	word = line.strip()
	words.append(word)

print(words)
