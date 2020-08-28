# Q. Remove multiple elements from a list in Python
'''
Given a list of numbers, write a Python program to remove multiple elements from a list based on the given condition.

Example:

Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]
'''
list1 = [11, 5, 17, 18, 23, 50]  
  

del list1[1:5] 
  
print(*list1) 
