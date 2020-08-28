# Q. K’th Non-repeating Character in Python using List Comprehension and OrderedDict
'''Given a string and a number k, find the k-th non-repeating character in the string. Consider a large input string with lacs of characters and a small character set. How to find the character by only doing only one traversal of input string?

Examples:

Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o

Input : str = geeksforgeeks, k = 4
Output : Less than k non-repeating
         characters in input.
'''

#from collections import OrderedDict
from collections import Counter

def func(str1,k):
	dict1={}
	empty=[]
	empty2=[]
	dict1=Counter(str1)
	for key, value in dict1.items():
		if value>1:
			empty.append(key)
		elif value==1:
			empty2.append(key)
	result=empty2[k-1]
	return result

str1='geeksforgeeks'
k=2
print(func(str1,k))