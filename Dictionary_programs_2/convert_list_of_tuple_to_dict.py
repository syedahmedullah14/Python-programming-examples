#Q.Python | Convert a list of Tuples into Dictionar
'''
Sometimes you might need to convert a tuple to dict object to make it more readable.

Input : [('A', 1), ('B', 2), ('C', 3)]
Output : {'B': [2], 'A': [1], 'C': [3]}
'''

def tuple_to_dict(list1):

	dict1=dict(list1)

	return dict1

list1=[('A', 1), ('B', 2), ('C', 3)]
print(tuple_to_dict(list1))