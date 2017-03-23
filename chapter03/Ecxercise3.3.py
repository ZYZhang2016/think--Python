#编写一个函数，出入参数s,打印该字符串，使得打印的字符串的最后一个字符在第70列
def right_justify(s):
	length = len(s)
	print(" "*(69-length),s)

right_justify("hahaha")