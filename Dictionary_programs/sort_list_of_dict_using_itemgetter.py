# Q. Ways to sort list of dictionaries by values in Python – Using itemgetter

# Python code demonstrate the working of sorted() 
# and itemgetter 
  
# importing "operator" for implementing itemgetter 
from operator import itemgetter 
  
# Initializing list of dictionaries 
lis = [{ "name" : "Sara", "age" : 22},  
{ "name" : "Ahmed", "age" : 19 }, 
{ "name" : "Yousuf" , "age" : 20 },
{ "name" : "Ankita" , "age" : 20}] 
  
# using sorted and itemgetter to print list sorted by age  
print ("The list printed sorting by age: ")
print (sorted(lis, key=itemgetter('age')) )
  
print ("\r") 
  
# using sorted and itemgetter to print list sorted by both age and name 
# notice that "Manjeet" now comes before "Nandini" 
print ("The list printed sorting by age and name: ")
print (sorted(lis, key=itemgetter('age', 'name')) )
  
print ("\r") 
  
# using sorted and itemgetter to print list sorted by age in descending order 
print ("The list printed sorting by age in descending order: ")
print (sorted(lis, key=itemgetter('age'),reverse = True) )
