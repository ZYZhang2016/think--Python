#coding:utf-8

class Time(object):
	'''represent time
	attribute:hour,minute,second
	'''
	def __init__(self,hour=0,minute=0,second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		a = '{}:{}:{}'.format(str(self.hour).zfill(2), str(self.minute).zfill(2), str(self.second).zfill(2))
		return a

	def time_to_int(self):
		minute = self.hour * 60 + self.minute
		second = minute * 60 + self.second
		return second

	def __cmp__(self,other):
		t1 = self.hour,self.minute,self.second
		t2 = other.hour, other.minute, other.second
		return cmp(t1,t2)

	def increment(self, other):
		t = self.time_to_int() + other.time_to_int()
		return self.int_to_time(t)

	def int_to_time(seconds):
		time = Time()
		minutes, time.second = divmod(seconds, 60)
		time.hour, time.minute = divmod(minutes, 60)
		return time



def main():
	time1 = Time(12,4,5)
	time2 = Time(11,59,52)
	print(time1.__cmp__(time2))

if __name__=='__main__':
	main()
