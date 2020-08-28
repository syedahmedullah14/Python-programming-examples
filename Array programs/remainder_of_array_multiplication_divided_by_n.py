# Q. Python Program for Find remainder of array multiplication divided by n
'''Given multiple numbers and a number n, the task is to print the remainder after multiply all the number divide by n.

Examples:

Input : arr[] = {100, 10, 5, 25, 35, 14}, 
            n = 11
Output : 9
100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

Approach that avoids overflow : First take a remainder or individual number like arr[i] % n. 
Then multiply the remainder with current result. After multiplication, again take remainder to avoid overflow. 
This works because of distributive properties of modular arithmetic. ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c
'''


def findremainder(arr,lens,n):
	mul=1
	for i in range(lens):
		mul=(mul*(arr[i]%n))%n

	return mul%n

arr=[100, 10, 5, 25, 35, 14]
lens=len(arr)
n=11
print(findremainder(arr,lens,n))
