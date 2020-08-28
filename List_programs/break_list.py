# Q. Break a list into chunks of size N in Python

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size=len(l)
empty=[]
empty2=[]
empty3=[]
n=4
i=0
while i<4:
	empty.append(l[:n])
	i+=1
	break
i=5
while i<8:
	empty2.append(l[n:n+4])
	i+=1
	break
i=9
while i<12:
	empty3.append(l[n+4:n+8])
	i+=1

	break
a,b,c=empty,empty2,empty3
print(a,b,c)

# Method 2: using yield keyword

'''my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life'] 
  
# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# How many elements each 
# list should have 
n = 5
  
x = list(divide_chunks(my_list, n)) 
print (x) '''

'''l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
   
# How many elements each  
# list should have  
n = 4
   
# using list comprehension  
x = [l[i:i + n] for i in range(0, len(l), n)]  
print(x)'''