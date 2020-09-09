#Q. Possible Words using given characters in Python

'''
Given a dictionary and a character array, print all valid words that are possible using characters from the array.
Note: Repetitions of characters is not allowed.
Examples:

Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
        arr = ['e','o','b', 'a','m','g', 'l']
Output : go, me, goal. 
'''
# Function to print words which can be created 
# using given set of characters 
  
 
def charCount(word): 
    dict = {} 
    for i in word: 
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def possible_words(lwords, charSet): 
    for word in lwords: 
        flag = 1
        chars = charCount(word) 
        for key in chars: 
            if key not in charSet: 
            	print(key)
               # flag = 0
            else: 
         #       if charSet.count(key) != chars[key]: 
                #    flag = 0
        #if flag == 1: 
            #print(word) 
  
if __name__ == "__main__": 
    input = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run'] 
    charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l'] 
    possible_words(input, charSet) 