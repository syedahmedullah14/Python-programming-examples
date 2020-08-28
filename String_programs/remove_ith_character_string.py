# Q. Ways to remove i’th character from string in Python

#Method 1:

s='Anonymous'
print(s[:2]+s[3:])

# Method 2:
'''
s='Anonymous'
new_s=''
for i in range(len(s)):
	if i != 2:
		new_s=new_s+s[i]
print(new_s)
'''