# Q. Merge two dictionaries
def mergedict(dict1,dict2):
	return (dict1.update(dict2))
dict1={'a':1, 'b':2}
dict2={'c':3}
print(mergedict(dict1,dict2))
print(dict1)

# MEthod 2 

'''def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
      
# Driver code 
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3) '''