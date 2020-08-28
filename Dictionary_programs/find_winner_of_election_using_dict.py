# Q. Dictionary and counter in Python to find winner of election

'''
Last Updated: 24-04-2020

Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.

Examples:

Input :  votes[] = {"john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"};
Output : John
We have four Candidates with name as 'John', 
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.
'''

from collections import Counter 
def votes(list1):
	list1=Counter(list1)
	dict={}

	for value in list1.values():

		dict[value]=[]

	for key, value in list1.items():
		
		dict[value].append(key)

	max_votes=sorted(dict.keys(), reverse=True)[0]
	 

	if len(dict[max_votes])>1:

		print (sorted(dict[max_votes])[0])
	else:
		
		print (dict[max_votes][0])

      

list1=['ahmed','ankita','yousuf','ankita','sara','ankita','sara','yousuf','sara']
print(votes(list1))