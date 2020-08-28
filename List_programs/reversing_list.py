'''list1=[1,2,3,4,5]
#print(list1[::-1])
list1.reverse()
print(list1)'''

'''list1=[1,2,3,4,5]
empty=list1[:]
list1.clear()
for i in range(len(empty)):
	popped=empty.pop()
	list1.append(popped)

print(list1)'''
list1=[1,2,3,4,5]
empty=[]
#empty=list1[:]
for i in list1[::-1]:
	empty.append(i)

	
print(empty)