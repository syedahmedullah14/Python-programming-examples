# Q. Python Program for Fibonacci numbers

'''The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

    Fn = Fn-1 + Fn-2

with seed values

   F0 = 0 and F1 = 1.'''


def fibonacci(n):
	a=0
	b=1
	if n<0:
		print('invalid input')
	#elif n==0:
		print (a)
	elif n==1:
		print (a)
	else:	
		print(a)
		print(b)
		for i in range(2,n):
			c=a+b
			a=b
			b=c
			print(c)
num=int(input('enter number '))
fibonacci(num)