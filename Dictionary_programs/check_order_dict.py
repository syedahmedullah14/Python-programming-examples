'''Given an input string and a pattern, check if characters in the input string follows the same order as determined by characters present in the pattern. 
Assume there won’t be any duplicate characters in the pattern.

Examples:

Input: 
string = "engineers rock"
pattern = "er";
Output: true
Explanation: 
All 'e' in the input string are before all 'r'.'''

def checkorder(input,ptr):
	l=len(ptr)
	for i in range(l-1):
		x=ptr[i]
		y=ptr[i+1]
		last=input.rindex(x)
		first=input.index(y)
		if last == -1 or first==-1 or last>first:
			return False
	return True
str1='engineers rock'
pattern='roc'
print(checkorder(str1,pattern))