# Q. Reverse words in a given String in Python

'''
We are given a string and we need to reverse words of given string ?

Examples:

Input : str = "geeks quiz practice code"
Output : str = "code practice quiz geeks"
'''

str_ = "geeks quiz practice code"
s=str_.split(' ')
rev=s[::-1]
join=' '.join(rev)
print(join)