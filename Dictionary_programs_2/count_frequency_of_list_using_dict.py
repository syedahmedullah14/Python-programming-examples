# Q.Counting the frequencies in a list using dictionary in Python

'''
Given an unsorted list of some elements(may or may not be integers), Find the frequency of each distinct element in the list using a dictionary.

Example:

Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
Output : 1 : 5
         2 : 4
         3 : 3
         4 : 3
         5 : 2
Explanation : Here 1 occurs 5 times, 2 
              occurs 4 times and so on...
'''
from collections import Counter
def count_freq(list1):

	dict1=Counter(list1)
	dict2=dict(dict1)

	for key, value in dict2.items():
		print("%d:%d"%(key,value))

list1=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
count_freq(list1)