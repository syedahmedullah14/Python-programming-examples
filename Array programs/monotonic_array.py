
'''Python Program to check if given array is Monotonic


Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. 
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return “True” if the given array A is monotonic else return “False” (without quotes).'''


def monotonic(A):

	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 

arr=[1,2,3,3,4,5]
print(monotonic(arr))