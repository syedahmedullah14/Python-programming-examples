# Q. Python Program for array rotation
'''
input=[1,2,3,4,5]
n=2 --> number of rotations
outpuy=[3,4,5,1,2]'''

def rotate(l,n):
 	empty=[]
 	empty2=[]
 	for i in range(0,n):
 	    empty.append(l[i])
 	for i in range(len(l)-n):
 	    popped=l.pop()
 	    empty2.append(popped)
 	rev=empty2[::-1]
 	final=rev+empty
 	print("Your list after rotation : {}".format(final))
 	
 	rev2=final[::-1]
 	msg="reversal of rotated list"+" "+str(rev2)
 	return msg

empty3=[]
count=1

rotation=int(input("Enter no of rotations : "))
num=int(input("Enter no of elements : "))
for i in range(0,num):

	a=int(input("Enter  element number {} :".format(count)))
	empty3.append(a)
	count+=1
print("Your list before rotation : {}".format(empty3))

print(rotate(empty3,rotation))


#Method 2

'''
array=[1,2,3,4,5]
n=3
array2=array[n:]+array[:n]
reverse=array2[::-1]
print(array2)
print(reverse)
'''



