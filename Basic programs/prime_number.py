def prime(n):
	global num
	for x in range(2,num):
		if num%x == 0:
			print('not prime')
			break
	else:
		print('prime')
		

num=int(input('enter number '))
prime(num)