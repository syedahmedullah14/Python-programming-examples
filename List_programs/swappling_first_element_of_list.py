# Q. Python program to interchange first and last elements in a list

'''
Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''
def swap(l):
	size=len(l)
	temp=l[0]
	l[0]=l[size-1]
	l[size-1]=temp
	return l	

list1=[1,2,3,4]
print(swap(list1))

#other different method-->

'''def swapList(newList): 
      
    newList[0], newList[-1] = newList[-1], newList[0] 
  
    return newList 

newList = [12, 35, 9, 56, 24] 
print(swapList(newList)) '''


'''def swapList(list): 
      
    # Storing the first and last element  
    # as a pair in a tuple variable get 
    get = list[-1], list[0] 
      
    # unpacking those elements 
    list[0], list[-1] = get 
      
    return list
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
print(swapList(newList))''' 



'''# Python3 program to illustrate  
# the usage of * operarnd 
list = [1, 2, 3, 4] 
  
a, *b, c = list
  
print(a) 
print(b) 
print(c) 

#Now let’s see the implementation of above approach:

# Python3 program to swap first 
# and last element of a list 
  
# Swap function 
def swapList(list): 
      
    start, *middle, end = list
    list = [end, *middle, start] 
      
    return list
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
  
print(swapList(newList)) '''

'''def swapList(list): 
      
    first = list.pop(0)    
    last = list.pop(-1) 
      
    list.insert(0, last)   
    list.append(first)    
      
    return list
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
  
print(swapList(newList)) '''
