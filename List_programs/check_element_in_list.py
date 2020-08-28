# Mehtod 1
''''
list1=[1,2,3,4,5]
n=6
for i in list1:

	if list1[i]==n:
		print(n, ' is in the list')
		break
	else:
		print(n,'is not in the list')
		break'''
# Method 2: using in
list1=[1,2,3,4,5]
if 2 in list1:
	print ('True')
else:
	print ('False')