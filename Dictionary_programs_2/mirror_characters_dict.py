# Q. Python Dictionary to find mirror characters in a string
'''
Given a string and a number N, we need to mirror the characters from N-th position up to the length of the string in the alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.

Examples:

Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.

Input : N = 6
        pneumonia
Output : pnefnlmrz'''

def mirror_characters(str1,n):

	original_str='abcdefghijklmnopqrstuvwxyz'
	reversed_str='zyxwvutsrqponmlkjihgfedcba'

	dict1=dict(zip(original_str,reversed_str))
	
	#separate out string
	prefix=str1[0:n-1]
	suffix=str1[n-1:]

	mirror_str=''

	for i in range(len(suffix)):

		#concatinating mirror_str and value of dict1 for example o will be l
		mirror_str=mirror_str+dict1[suffix[i]]
	
	#concatinate prefix and mirror_str
	return prefix+mirror_str

n=6
str1='pneumonia'
print(mirror_characters(str1,n))