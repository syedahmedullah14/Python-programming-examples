'''def fun(l,n):
	empty=[]
	l.sort()
	return l[:n:-1]
l=[1,2,3,4,5]
print(fun(l,2))'''

# l=[1,2,3,4,5]
# l.sort()
# n=2
# print(l[-n:])
def fun(l,n):
	for i in l:
	    m=max(l)
	    
	    if i==m:
	    	popped=l.pop()
	        empty.append(popped)
	return empty[:n]

list1=[10,23,45,32]
n=3
empty=[]
print(fun(list1,n))