# Q. Ways to sort list of dictionaries by values in Python – Using lambda function

# Python code demonstrate the working of sorted() 
# and lambda function 
  
  
# Initializing list of dictionaries 
lis = [{ "name" : "Sara", "age" : 22},  
{ "name" : "Ahmed", "age" : 19 }, 
{ "name" : "Yousuf" , "age" : 20 },
{ "name" : "Ankita" , "age" : 20}] 
  
# using sorted and itemgetter to print list sorted by age  
print ("The list printed sorting by age: ")
print (sorted(lis, key= lambda i:i['age']) )
  
print ("\r") 
  
# using sorted and itemgetter to print list sorted by both age and name 
# notice that "Manjeet" now comes before "Nandini" 
print ("The list printed sorting by age and name: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])) )
  
print ("\r") 
  
# using sorted and itemgetter to print list sorted by age in descending order 
print ("The list printed sorting by age in descending order: ")
print (sorted(lis, key=lambda i: i['age'],reverse = True) )
