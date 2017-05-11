#coding:utf-8
import os
cwd = os.getcwd()
paren_dir = os.path.dirname(cwd)
dir_tree = os.walk(os.path.abspath(paren_dir))
'''
for dirname,subdir,file in dir_tree:
	print(dirname)
	print(subdir)
	print(file)
	print('----------------------')
'''
for dirname,subdir_list,file_list in dir_tree:
	for filename in file_list:
		print(os.path.abspath(filename))
	for subdir in subdir_list:
		print(subdir)