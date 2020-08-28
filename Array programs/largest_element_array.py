# Q. Python Program to find largest element in an array
'''Given an array, find the largest element in it.

Input : arr[] = {10, 20, 4}
Output : 20

Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
'''

arr=[2,3,5]
x=max(arr)
print(x)

#2nd method

'''def largest(arr,n): 
  
    # Initialize maximum element 
    max = arr[0] 
  
    # Traverse array elements from second 
    # and compare every element with  
    # current max 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  
# Driver Code 
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = largest(arr,n) 
print ("Largest in given array is",Ans) '''