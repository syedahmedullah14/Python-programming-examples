#recursive
'''def factorial(n):
	return 1 if (n==1 or n==0 ) else n*factorial(n-1)

num=input('type number ')
num=int(num)

print("factorial of ", num, "is", factorial (num))'''

#iterative 

'''def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact 
  

num = 5; 
print("Factorial of",num,"is", factorial(num)) '''

def  factorial(n):
	if n<0:
		return 0
	elif n==1 or n==0:
		return 1
	else:
		fact = 1
		for x in range(1,n+1):
			fact*=x
			x-=1
		return fact
num=input('type number ')
num=int(num)

print("factorial of ", num, "is", factorial (num))

			

