# Q. Python program to print all Prime numbers in an Interval
'''Given two positive integer start and end.
The task is to write a Python program toprint all Prime numbers in an Interval.'''

start=10
end=100


print(start, end)
for num in range(start,end+1):
	if (num>1):
		for i in range(2,num):
			if ((num%i)==0):
				break
		else:
			print(num)
		
