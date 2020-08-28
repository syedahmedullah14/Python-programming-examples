# Python program to print even length words in a string
'''
Given a string. The task is to print all words with even length in the given string.

Examples:

Input: s = "This is a python language"
Output: This
        is
        python
        language 

'''
def evenWords(s): 
      
    
    s = s.split(' ')  
     
    for word in s:  
          
        
        if len(word)%2==0: 
            print(word)  
  
  
Driver Code  
s = "We are anonymous" 
printWords(s)  