# Q. Python dictionary with keys having multiple inputs

# creating an empty dictionary 
dict = {} 
  
# Insert first triplet in dictionary 
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z; 
  
# Insert second triplet in dictionary 
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z; 
  
# print the dictionary 
print(dict) 