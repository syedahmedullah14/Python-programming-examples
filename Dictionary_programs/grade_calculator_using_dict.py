# Q. Program to create grade calculator in Python
'''Given different scored marks of students. We need to find grades. The test score is an average of the respective marks scored in assignments, tests and lab-works. The final test score is assigned using below formula.

10 % of marks scored from submission of Assignments
70 % of marks scored from Test
20 % of marks scored in Lab-Works

 
Grade will be calculated according to :

1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"

Also, calculate the total class average and letter grade of class.'''

def get_average(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 

def calculate(students):
	
	assignment=get_average(students["assignment"])
	lab=get_average(students["lab"])
	test=get_average(students["test"])

	return (0.1*assignment + 0.7 * test + 0.2*lab)
def grade(score):

	if score>=90: return 'A'
	elif score>=80: return 'B'
	elif score>=70: return 'C'
	elif score>=60: return 'D'
	else: return 'E'

Ankita = { "name":"Ankita", 
         "assignment" : [97, 92, 93, 79], 
         "test" : [91, 90], 
         "lab" : [88.20, 97.20] 
       } 

Yousuf = { "name":"Yousuf", 
         "assignment" : [90, 80, 78, 81], 
         "test" : [75, 85], 
         "lab" : [88.20, 87.20] 
       } 

Sara = { "name":"Sara", 
         "assignment" : [95, 88, 60, 76], 
         "test" : [75, 80], 
         "lab" : [90.20, 89.20] 
       } 



students=[Ankita,Sara,Yousuf]

for i in students : 
    print(i["name"]) 
   
    print("Average marks of %s is : %s " %(i["name"],calculate(i))) 
                           
    print("Letter Grade of %s is : %s" %(i["name"],grade(calculate(i)))) 
      
    print()

class_ave=0
for x in students:
	class_ave+=calculate(x)
	
	average=class_ave/3

print('Class average is ',average)
print('Letter grade of class is', grade(average))