
# Q. Python program to print odd Numbers in a List 

l1=[2,-3,4,-5,6]
even=0
odd=0
for i in l1:
	if i%2==0:
		even+=1
	else:
		odd+=1
print('even:', even, 'odd:', odd)

'''
   
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93, 11] 
   
only_odd = [num for num in list1 if num % 2 == 1] 
odd_count = len(only_odd) 
   
print("Even numbers in the list: ", len(list1) - odd_count) 
print("Odd numbers in the list: ", odd_count) 
'''

'''
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93, 11] 
  
odd_count = len(list(filter(lambda x: (x%2 != 0) , list1))) 
  
# we can also do len(list1) - odd_count 
even_count = len(list(filter(lambda x: (x%2 == 0) , list1))) 
  
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count) 
'''