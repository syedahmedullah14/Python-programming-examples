# Q. Python program to find uncommon words from two Strings

'''
Given two sentences as strings A and B. The task is to return a list of all uncommon words. 
A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence.

Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

Examples:

Input : A = "Geeks for Geeks" 
        B = "Learning from Geeks for Geeks"
Output : ['Learning', 'from']

Input : A = "apple banana mango" 
        B = "banana fruits mango"
Output : ['apple', 'fruits']
'''


# using symmetric difference
a="apple banana mango" 
b="banana fruits mango"
x=a.split() 
y=b.split() 
k=set(x).symmetric_difference(set(y)) 
print(list(k))