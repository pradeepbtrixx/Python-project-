'''
[question]
1.	Ask for a student number.
2.	Ask for the student’s tutorial mark.
3.	Ask for the student’s test mark.
4.	Calculate whether the student’s average so far is high enough 
    for the student to be permitted to write the examination. 
    If the average (mean) of the tutorial and test marks is lower than 40%,
    the student should automatically get an F grade, and the program should print
    the grade and exit without performing the following steps.

5.	Ask for the student’s examination mark.
6.	Calculate the student’s final mark. The tutorial and test marks should count 
	for 25% of the final mark each, and the final examination should
	count for the remaining 50%.

7.	Calculate and print the student’s grade, according to the following table:
Weighted final score	Final grade
80 <= mark <= 100	A
70 <= mark < 80	B
60 <= mark < 70	C
50 <= mark < 60	D
mark < 50	E 
'''
#[ANSWER]
class grade_check:
	student_entry = 0
	def __init__(self,roll_no,tut_mark,test_mark):
		self.roll_no = roll_no
		self.tut_mark = tut_mark
		self.test_mark = test_mark
		self.exam_mark = 0
		grade_check.student_entry += 1

	def grade(self):
		if ((self.tut_mark+self.test_mark)/2) < 40:
			return 'your grade is [F]'
		else:
			self.exam_mark = float(input('enter your exam mark:'))
			final_result = (self.tut_mark*25)/100 + (self.test_mark*25/100) + (self.exam_mark*50/100)
			if 100 > final_result >= 80:
				return 'your grade is [A] '
			elif 80 > final_result >=70:
				return 'your grade is [B]'
			elif 70 > final_result >=60 :
				return'your grade is [C]'
			elif 60 > final_result >=50:
				return'your grade is [D]'
			else:
				return'your grade is [E]'

def main():					
	while True:
		stu_no = int(input('enter your roll_no: ' ))	
		tut_mark = float(input('enter your tutorial mark : '))
		test_mark = float(input('enter your test mark : '))					  
	
		student = grade_check(stu_no,tut_mark,test_mark)
		print(student.grade())

		st = input('do u want to know how many search that u made now [Y/N]:')
		if st == 'Y':
			print(f'you checked the grades for {grade_check.student_entry}student')
		else:
			pass
		c = input("DO YOU WANT TO CHECK FOR ANOTHER STUDENT [Y/N]: ")
		if c == 'N':
			print('thank you so much for use this code ')
			break

if __name__ == '__main__':
	main()

#-------------------------------------------------------------------------------------
'''
[question]
You are given a string representing the postfix expression.Evaluate the expression.
 And print the answer and print -1 if expression is wrong

Input Description:
You are given with a string containing operator and digits 0-9.

Output Description:
Print the answer print -1 if expression given is wrong

Sample Input :
23+*
Sample Output :
-1
'''
#[ANSWER]
#POSTFIX EXPRESSION
import re
import numpy as np
d = input('enter some operater and operand : ')

v2 = []
for i in d:   # Type casting int value from string and added to v2 list
	if i in ['+','-','*','%','/']:
		v2.append(i)
	else:
		v2.append(int(i))

try :
	stack = []
	for i in v2:
		if i in ['+','-','*','/']:
			if i == '+':
				stack.append(stack.pop(-2) + stack.pop(-1))
			elif i == '-':
				stack.append(stack.pop(-2) - stack.pop(-1))
			elif i == '*':
				stack.append(stack.pop(-2) * stack.pop(-1))
			elif i == '/':
				stack.append(stack.pop(-2) / stack.pop(-1))
			elif i == '%':
				stack.append(stack.pop(-2) % stack.pop(-1))
			else:
				pass
		else:
			stack.append(i)
	print(stack)
except:
	print(-1)

#----------------------------------------------------------------------------------------------









