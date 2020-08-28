# Q. Python | Program to print duplicates from a list of integers

'''
Given a list of integers with duplicate elements in it. 
The task to generate another list, which contains only the duplicate elements. 
In simple words, the new list should contain the elements which appear more than one.
'''
def duplicate(list_1):
    empty=[]
    empty_2=[]
    for i in list_1:
        if i not in empty:
            empty.append(i)
        else:
            if i  not in empty_2:
                empty_2.append(i)
    return empty_2


print(duplicate([-1, 1, -1, 8]))
