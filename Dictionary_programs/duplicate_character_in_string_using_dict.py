# Q. Python Counter| Find all duplicate characters in string
'''
Given a string, find all the duplicate characters which are similar to each others.

Let’s look at the example.
Examples:

Input : hello
Output : l
'''

from collections import Counter

def duplicate(str1):

	temp=0
	dict=Counter(str1)
	for key, value in dict.items():
		if value>1:
			return (key)


str1='hello'

print(duplicate(str1))