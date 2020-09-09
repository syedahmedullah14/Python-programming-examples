# Q. Python Counter to find the size of largest subset of anagram words

'''Given an array of n string containing lowercase letters.
Find the size of largest subset of string which are anagram of each others.
An anagram of a string is another string that contains same characters, only the order of characters can be different.
For example, “abcd” and “dabc” are anagram of each other.

Examples:

Input: 
ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3
'''
from collections import Counter

def anagrams(str1):
	dict={}
	str1=str1.split(' ')
	
	for i in range(0,len(str1)): 
		str1[i]=''.join(sorted(str1[i])) 

	dict2=Counter(str1)

	for value in dict2.values():
		return (max(dict2.values()))
		break


	# or return (max(dict2.values()))

str1='ant magenta magnate tan gnamate'
print(anagrams(str1))