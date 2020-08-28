# Q. Handling missing keys in Python dictionaries

#Mehtod 1: using get()

dict1={'a':1, 'b':2}
x=dict1.get('c',3)
print(x)

#Method 2: using setdefault()
'''dict1={'a':1, 'b':2}
x=dict1.setdefault('c',3)
print(x)'''

'''import collections 
  
# declaring defaultdict 
# sets default value 'Key Not found' to absent keys 
defd = collections.defaultdict(lambda : 'Key Not found') 
  
# initializing values  
defd['a'] = 1
  
# initializing values  
defd['b'] = 2
  
# printing value  
print ("The value associated with 'a' is : ",end="") 
print (defd['a']) 
  
# printing value associated with 'c' 
print ("The value associated with 'c' is : ",end="") 
print (defd['c']) '''