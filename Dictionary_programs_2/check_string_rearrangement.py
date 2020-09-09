# Q.Python counter and dictionary intersection example (Make a string using deletion and rearrangement)

'''
Given two strings, find if we can make first string from second by deleting some characters from second and rearranging remaining characters.

Examples:

Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible
'''
from collections import Counter

def check(str1,str2):

	dict1=Counter(str1)
	dict2=Counter(str2)
	dict3= dict1 & dict2
	dict4= dict2 & dict1
	if dict3 == dict1 or dict4==dict2:

		return True
	else:

		return False



str1='iamahmed'
str2 ='ahmed'
print(check(str1,str2))