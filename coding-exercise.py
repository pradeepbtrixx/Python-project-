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

try:
    d = input('[enter  your postfix expression here] : ')
    k = []
    for i in d:
        if i in ['+','-','*']:
            k.append(i)
        else:
            k.append(int(i))
    stack = []
    for i in k:
        if i in ['+','-','*']:
            if i =='+':
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif i == '-':
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif i =='*':
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif i == '/':
                stack.append(stack.pop(-2) / stack.pop(-1))
            else:
                stack.append(stack.pop(-2) % stack.pop(-1))

        else:
            stack.append(i)
    print(stack[0])
except :
    print(-1)
#----------------------------------------------------------------------------------------------
#[QUESTION]
'''
LYZ company is working with Analyst team to check the most react tweets of people.
They have been assigned task of finding the most repeated words used by tweeters.
The task looked simple at the beginning but when they started doing the job 
they found that their formula is not working for all the tweets. When the number of words
increases they are unable to find the repeated words. Now they need to 
design a method with will help them pass the sentence and get the most repeated words
in the given sentence. 

Point to Note:
1. An user might type more than one sentence
2. There might be special tags or characters - which should be ignored
3. There must be a module which will help the developers re-use the code

Sample Input :
#Wise wish his #work #get organised. so that I can work in peace #WishMe
Sample Output :
is
'''
#[ANSWER]
from difflib import SequenceMatcher 
import re

class most_tweeted_wordchecker:

	def longestSubstring(str1,str2):  
	    seqmatch = SequenceMatcher(None,str1,str2)  
	    match = seqmatch.find_longest_match(0, len(str1), 0, len(str2)) 
	    if (match.size >= 2): 
	        return str1[match.a: match.a + match.size]  
	    else:
	        False

	def most_tweeted_word(x):
	    d = x.lower()
	    a = re.findall(r'[\w]+',d)
	    data = {}
	    for i in a:
	        for j in a:
	            d = most_tweeted_wordchecker.longestSubstring(i,j)
	            if d in data:
	                data[d] += 1
	            else:
	                data[d] = 1

	    sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=True)
	    print()
	    print()
	    print(f'THE MOST OCCURED WORD IN THIS TWEET IS : {sort_orders[1][0]}')

def main():
	while True:
		va = input('enter your tweet here : ').split(' ')
		if not va:
			break
		elif len(va)<=1:
			return 'please enter sequence of words'
			continue
		else:
			if va:
				most_tweeted_wordchecker.most_tweeted_word(str(va))
				D = input('DO YOU WANT TO CHECK FOR ANOTHER TWEET [Y/N] : ')
				if D == 'Y':
					continue
				else:
					return'THANK YOU SO MUCH FOR USING THIS CODE '


			
if __name__ == '__main__':
	print(main())

#=======================================================================================================================
