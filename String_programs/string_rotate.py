
# Q. String slicing in Python to rotate a string
'''
Given a string of size n, write functions to perform following operations on string.

    Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
    Right (Or clockwise) rotate the given string by d elements (where d <= n).

Examples:

Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe" 
         Right Rotation : "ksGeeksforGee"
'''  

n='anonymous'
d=2
# left rotation
a=n[0:d]
b=n[d:]
c=b+a
print(c)
# right rotation
x=n[0:len(n)-2]
y=n[len(n)-2:]
z=y+x
print(z)