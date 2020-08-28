# Q. Python | Sort Python Dictionaries by Key or Value



'''def dictionary():
	key_value={}
	key_value[2]=32
	key_value[3]=20
	key_value[0]=12
	key_value[1]=10

	print('Task 1:- \n')
	
	print('Keys are')

	for i in sorted(key_value.keys()):
		print (i)
	
	print('Task 2 Keys and Values sorted in alphabetical order by the key:\n')
	print('Keys with values')

	for  i in sorted(key_value):
		print((i, key_value[i]), end =" ")

	print('\nTask 3 Keys and Values sorted in alphabetical order by the value:')

	print(sorted(key_value.items(), key = lambda t: t[1]))
dictionary()'''

def dictionary():

	dict1={'Ahmed': 19, 'Sara': 22, 'Ankita':20, 'Yousuf':20}

	sortbykeys=sorted(dict1.items(), key = lambda t: t[0])
	print(sortbykeys)

	sortbyvalues=sorted(dict1.items(), key = lambda t: t[1])
	print(sortbyvalues)
dictionary()