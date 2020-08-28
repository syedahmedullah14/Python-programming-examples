# Q. Python | Check order of character in string using OrderedDict( )

'''Given an input string and a pattern, check if characters in the input string follows the same order as determined by characters present in the pattern. Assume there won’t be any duplicate characters in the pattern.

Examples:

Input: 
string = "engineers rock"
pattern = "er";
Output: true
Explanation: 
All 'e' in the input string are before all 'r'.
'''
from collections import OrderedDict 

def checkorder(input,ptr):
	pointer=0
	l=len(ptr)
	dict=OrderedDict.fromkeys(input)

	for key,value in dict.items():
		if key==ptr[pointer]:
			pointer+=1
		if pointer==l:
			return True

	return False





str1="engineers rock"
pattern='er'
print(checkorder(str1,pattern))	