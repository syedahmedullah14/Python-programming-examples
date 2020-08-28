# Q. Python | Remove empty tuples from a list
'''
In this article, we will see how can we remove an empty tuple from a given list of tuples. 
We will find various ways, in which we can perform this task of removing tuples using various methods and ways in Python.
Examples:

Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
Output : [('ram', '15', '8'), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('', '')]
          '''
def remove_empty_tuple(list_1):
    for i in list_1:
        if i:
            continue
        else:
            list_1.remove(i)
    return list_1

print(remove_empty_tuple(  [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]))