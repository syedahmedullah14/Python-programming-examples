
# Q. Python Dictionary | Check if binary representations of two numbers are anagram

'''Given two numbers you are required to check whether they are anagrams of each other or not in binary representation.

Examples:

Input : a = 8, b = 4 
Output : Yes
Binary representations of both
numbers have same 0s and 1s.

Input : a = 4, b = 5
Output : No'''
from collections import Counter

def binary_anagram(n1,n2):

	bin1=bin(n1)[2:]
	bin2=bin(n2)[2:]
	#taking absolute value in variable using abs() function, for example -2 will be 2
	zeros=abs(len(bin1)-len(bin2))
	
	if len(bin1)>len(bin2):

		bin2=zeros*'0'+bin2

	else:
		bin1=zeros*'0'+bin1	

	#converting into dictionaries
	x=Counter(bin1)
	y=Counter(bin2)
	
	if x==y:
		return 'Yes'
	else:
		return 'No'
    
n1,n2 = 1,4

print(binary_anagram(n1,n2))