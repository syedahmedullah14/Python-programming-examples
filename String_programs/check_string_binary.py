
# Q. Python | Check if a given string is binary string or not
'''
Given a string str. The task is to check whether it is a binary string or not.

Examples:

Input: str = "01010101010"
Output: Yes

Input: str = "geeks101"
Output: No
'''


s={'0','1'}
string='10101'
p=set(string)
# using sets because it does not allow duplicate members for example: 101010 will be {'1', '0'}
if s==p or p=={'0'} or p=={'1'}:
	print('String is binary')
else:
	print('String is not binary')

#other method

'''def check(string) : 
  
    # set function convert string 
    # into set of characters . 
    p = set(string) 
  
    # declare set of '0', '1' . 
    s = {'0', '1'} 
  
    # check set p is same as set s 
    # or set p contains only '0' 
    # or set p contains only '1' 
    # or not, if any one condition 
    # is true then string is accepted 
    # otherwise not . 
    if s == p or p == {'0'} or p == {'1'}: 
        print("Yes") 
    else : 
        print("No") 
  
  
          
# driver code 

string = "101010000111"
  
    # function calling 
check(string) '''