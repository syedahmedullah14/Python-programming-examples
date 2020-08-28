# Q.Python | Check if a Substring is Present in a Given String

'''
Given two strings, check if s1 is there in s2.

Examples:

Input : s1 = geeks s2=geeks for geeks
Output : yes

Input : s1 = geek s2=geeks for geeks
Output : yes
'''
s1 = 'geeks'
s2='geeks for geeks'

a=s1 in s2
print(a)

# Other methods-->

'''
def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("NO") 
    else: 
        print("YES") 
            
# driver code 
string = "geeks for geeks"
sub_str ="geek"
check(string, sub_str) 
'''

'''
def check(s2, s1):  
    if (s2.count(s1)>0):      
        print("YES")  
    else:  
        print("NO")  
              
s2 = "A geek in need is a geek indeed"
s1 ="geek"
check(s2, s1)  
'''

'''
# When you have imported the re module, you can start using regular expressions. 
import re 
  
# Take input from users 
MyString1 =  "A geek in need is a geek indeed"
MyString2 ="geek"
  
# re.search() returns a Match object if there is a match anywhere in the string 
if re.search( MyString2, MyString1 ): 
    print("YES,string '{0}' is present in string '{1}' " .format(MyString2,MyString1)) 
else: 
    print("NO,string '{0}' is not present in string {1} " .format(MyString2, MyString1) ) 
'''