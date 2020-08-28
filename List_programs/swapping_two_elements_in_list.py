# Q. Python program to swap two elements in a list
'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Examples:

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
'''

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
  
# Driver function 
List = [23, 65, 19, 90] 
pos1, pos2  = 1, 3
#or os1, pos2  = 0,2
  
print(swapPositions(List, pos1-1, pos2-1)) 

# other methods-->


# or print(swapPositions(List, pos1, pos2))

'''def swapPositions(list, pos1, pos2): 
      
    # popping both the elements from list 
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    # inserting in each others positions 
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)   
      
    return list
  
# Driver function 
List = [23, 65, 19, 90] 
pos1, pos2  = 1, 3
  
print(swapPositions(List, pos1-1, pos2-1)) '''

'''def swapPositions(list, pos1, pos2): 
  
    # Storing the two elements 
    # as a pair in a tuple variable get 
    get = list[pos1], list[pos2] 
       
    # unpacking those elements 
    list[pos2], list[pos1] = get 
       
    return list
  
# Driver Code 
List = [23, 65, 19, 90] 
  
pos1, pos2  = 1, 3
print(swapPositions(List, pos1-1, pos2-1)) '''


'''list1 = [1, 2, 3] 
  
# Printing list1 before deleting  
print ("List1 before deleting is : " + str(list1)) 
  
# deleting list using *= 0 
list1 *= 0
  
# Printing list1 after *= 0 
print ("List1 after clearing using *= 0: " + str(list1)) '''

'''def swap(l1,pos1,pos2):
	first=l1.pop(pos1)
	last=l1.pop(pos2-1)

	l1.insert(pos2, first)
	l1.insert(pos1, last)
	return l1

list1=[1,2,3,4,5]
pos1, pos2=1,3
print(swap(list1,pos1-1,pos2-1))'''