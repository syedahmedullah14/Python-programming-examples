#Q. Print anagrams together in Python using List and Dictionary
'''
Given an array of words, print all anagrams together ?

Examples:

Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
Output : 'cat tac act dog god'
'''

def anagrams(list1):
	dict={}
	for word in list1:
		sorted_word=''.join(sorted(word))
		if sorted_word not in dict.keys():
			dict[sorted_word]=[word]
		else:
			dict[sorted_word].append(word)

	result=''
	for values in dict.values():
		result=result+' '.join(values)+' '

	return result
list1=['cat', 'dog', 'tac', 'god', 'act']
print(anagrams(list1))