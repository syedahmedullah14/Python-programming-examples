# Q. Python program for removing i-th character from a string
'''
Given the string, we have to remove the ith indexed character from the string.

In any string, indexing always start from 0. Suppose we have a string geeks then its indexing will be as –

g e e k s
0 1 2 3 4
'''

# Method 1:
n='Anonymous'
i=2
a=n[0:i]
b=n[i+1:]
c=a+b
print(c)

# Method 2

'''
n='Anonymous'
i=2
for x in n:
	if x!=n[i]:
		print(x)
		'''

