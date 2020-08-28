# Method 1: 
def second_largest(list1):
    remove=list1.remove(max(list1))
    return max(list1)

print(second_largest( [70, 11, 20, 4, 100] ))

#Method 2:
'''
list1=[1,2,3,4,5]

# m=max(list1)
empty=[]
for i in range(0,len(list1)):
    m=max(list1)
    popped=list1.pop()
    if popped==m:
        empty.append(popped)
print(empty[1])
'''

#Method 3: using sort
'''
list1=[1,2,3,4,5]
list1.sort()
print(list1[-2])
'''
