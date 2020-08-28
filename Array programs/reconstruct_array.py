
'''Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M
Last Updated: 17-02-2020

Given an array of N elements and an integer M. Now, the array is modified by replacing some of the array elements with -1. 

The task is to print the original array.

The elements in the orginal array are related as, for every index i, a[i] = (a[i-1]+1)% M.

It is guaranteed that there is one non zero value in the array.

Examples:

Input: arr[] = {5, -1, -1, 1, 2, 3}, M = 7
Output: 5 6 0 1 2 3
M = 7, so value at index 2 should be (5+1) % 7 = 6
value at index 3 should be (6+1) % 7 = 0

Input: arr[] = {5, -1, 7, -1, 9, 0}, M = 10
Output: 5 6 7 8 9 0'''

def reconstruct(l,n):
	empty=[]
	for i in range(0,len(l)):
	    if l[i]==-1:
	        a=(l[i-1]+1)%n
	        empty.append(a)
	    else:
	        empty.append(l[i])
	return empty


l=[5, -1, 7, -1, 9, 0]
M=10
print(reconstruct(l,M))

