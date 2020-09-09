# Q.Python | Remove all duplicates words from a given sentence
'''
Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.

Examples:

Input : Geeks for Geeks
Output : Geeks for

Input : Python is great and Java is also great
Output : is also Java Python and great'''

from collections import Counter

def duplicate_words(str1):
	
	str1=str1.lower()

	split_str=str1.split(' ')

	dict1=Counter(split_str)
	empty=[]
	for key,value in dict1.items():

		if value>=1:
			empty.append(key)
	empty2=''
	for i in empty:
		empty2=' '.join(empty)

	return empty2

str1='Python is a beast and Python is amazing also'
print(duplicate_words(str1))


# Program without using any external library 

'''
s = "Python is great and Java is also great"
l = s.split() 
k = [] 
for i in l: 
  
    # If condition is used to store unique string  
    # in another list 'k'  
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k)) 
'''