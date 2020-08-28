# Q. Python program to print even Numbers in a List 

l1=range(1,10)
for i in l1:
	if i % 2==0:
		print(i)


'''

  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
  
# using list comprehension 
even_nos = [num for num in list1 if num % 2 == 0] 
  
print("Even numbers in the list: ", even_nos) 
'''

'''
# Python program to print Even Numbers in a List 
  
# list of numbers  
list1 = [10, 21, 4, 45, 66, 93, 11]  
  
  
# we can also print even no's using lambda exp.  
even_nos = list(filter(lambda x: (x % 2 == 0), list1)) 
  
print("Even numbers in the list: ", even_nos)  
'''