# Q. Python Program for Sum of squares of first n natural numbers
'''
Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

Examples:

Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

Input : N = 5
Output : 55
'''

def sqrsum(n):
	sum=0
	for i in range(1,n+1):
		sum=sum+(i*i)
	return sum

num=int(input('enter number '))
print(sqrsum(num))

#for cube
'''def sumOfSeries(n): 
    x = (n * (n + 1)  / 2) 
    return (int)(x * x) 
  
  
   
# Driver Function 
n = 5
print(sumOfSeries(n))''' 

#or
'''def cubesum(n):
	sum=0
	for i in range(1,n+1):
		sum=sum+(i*i*i)
	return sum

num=int(input('enter number '))
print(cubesum(num))