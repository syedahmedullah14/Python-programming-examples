
# Q. Python Counter| Find all duplicate characters in string
'''
Given a string, find all the duplicate characters which are similar to each others.

Let’s look at the example.
Examples:

Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s
'''


from collections import Counter 
str1='Anonymous'
x=Counter(str1)
count=-1
for i in x.values():
	count=count+1
	if (i>1):
		print (x.keys(),[count])