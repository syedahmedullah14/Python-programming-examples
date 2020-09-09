#Q.Python dictionary, set and counter to check if frequencies can become same

'''
Given a string which contains lower alphabetic characters, we need to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.

Examples:

Input  : str = “xyyz”
Output : Yes
We can remove character ’y’ from above 
string to make the frequency of each 
character same.
'''

from collections import Counter

def check_freq(str1):

	dict1=Counter(str1)

	set1=list(set(dict1.values()))

	if len(set1)>2:
		print('No')
	elif len(set1)==2 and set1[1]-set1[0]>1:
		print('No')
	else:
		print('Yes')

	return set1


str1 = 'xyyz'
check_freq(str1)