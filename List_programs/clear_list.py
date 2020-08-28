# Q Different ways to clear a list in Python
#Method 1: using pop() 

list1=[1,2,3,4,5]
for i in range(len(list1)):
	list1.pop()
print(list1)

# Method 2: using clear() method

list1=[1,2,3,4,5]
list1.clear()
print(list1)