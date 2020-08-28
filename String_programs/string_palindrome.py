# Q. Python program to check if a string is palindrome or not
'''
Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

Examples:

Input : malayalam
Output : Yes

Input : geeks
Output : No
'''


a='malayalam'
rev=a[::-1]
if a==rev:
	print("palindrome")
else:
	print("not palindrome")