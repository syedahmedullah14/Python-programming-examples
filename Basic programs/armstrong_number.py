def armstrong(n):
	sum=0
	global num
	n=len(str(num))
	sum=0
	while num>0:
		digit=num%10
		sum+=digit ** n
		num//=10
	print('armstrong') if orig==sum else ('not armstrong')

num=int(input('enter number'))
orig=num
armstrong(num)