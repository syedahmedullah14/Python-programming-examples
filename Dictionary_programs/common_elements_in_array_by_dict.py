# Q. Python | Find common elements in three sorted arrays by dictionary intersection

'''
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples:

Input:  ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [80, 20]

Input:  ar1 = [1, 5, 5]
        ar2 = [3, 4, 5, 5, 10]
        ar3 = [5, 5, 10, 20]
Output: [5, 5]
'''
from collections import Counter

def common(ar1,ar2,ar3):
	#converting arrays into dictionaries
	ar1 = Counter(ar1)
	ar2 = Counter(ar2)
	ar3 = Counter(ar3)
	result=dict(ar1.items() & ar2.items() & ar3.items())
	com_arr=[]
	#the below statement will print dictionary but we only need keys to print
	print(result)

	for key, value in result.items():
		for i in range(value):
			#printing keys
			com_arr.append(key)
	return com_arr
	
ar1 = [1, 5, 10, 20, 40, 80] 
ar2 = [6, 7, 20, 80, 100] 
ar3 = [3, 4, 15, 20, 30, 70, 80, 120] 
print(common(ar1,ar2,ar3))