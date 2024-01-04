class grade_check():
	student_entry = 0
	def __init__(self,roll_no,tut_mark,test_mark):
		self.roll_no = roll_no
		self.tut_mark = tut_mark
		self.test_mark = test_mark
		self.exam_mark = 0
		grade_check.student_entry += 1

	def grade(self):
		if ((self.tut_mark+self.test_mark)/2) < 40:
			return 'your grade is [F] '
		else:
			self.exam_mark = int(input('enter your exam mark:'))
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

stu_no = int(input('enter your roll_no: ' ))
tut_mark = int(input('enter your tutorial mark : '))
test_mark = int(input('enter your test mark : '))					  

student = grade_check(stu_no,tut_mark,test_mark)
print(student.grade())