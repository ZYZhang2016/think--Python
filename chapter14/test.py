import dbm
import os
import pickle
import argparse


parser=argparse.ArgumentParser()
parser.add_argument("echo",help="echo the string")
args=parser.parse_args()
print(args.echo)
'''
cmd = 'ls -l'
fp = os.popen(cmd)
res = fp.read()
#state = fp.close()
# help(shelve)
'''
'''
def db():
	i = 0
	db = dbm.open('plalidrome_words.db', 'c')
	bd[i]
db()



handler = open('words.txt')
words = []
for line in handler:
	word = line.strip()
	words.append(word)

print(words)
'''
