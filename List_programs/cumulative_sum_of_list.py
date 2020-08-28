# Q.Python program to find Cumulative sum of a list
'''
The problem statement asks to produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements.

Examples : 
 

Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]

Input : list = [4, 10, 15, 18, 20]
Output : [4, 14, 29, 47, 67]
'''
list1 =[10, 20, 30, 40, 50]
list2=[]
total=0
for i in list1:
	total+=i
	total.append(list2)
print(list2)