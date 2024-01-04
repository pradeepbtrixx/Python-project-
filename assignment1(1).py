

stu_no = int(input('enter your roll_no: ' ))
tut_mark = int(input('enter your tutorial mark : '))
test_mark = int(input('enter your test mark : '))

if (int((tut_mark+test_mark)/2)) < 40:
	print('your grade is [F] ')
else:
	exam_mark = int(input('enter your exam mark : '))
	final_result = (tut_mark*25)/100 + (test_mark*25/100) + (exam_mark*50/100)
	if 100 > final_result >= 80:
		print('your grade is [A] ')
	elif 80 > final_result >=70:
		print('your grade is [B]')
	elif 70 > final_result >=60 :
		print('your grade is [C]')
	elif 60 > final_result >=50:
		print('your grade is [D]')
	else:
		print('your grade is [E]')



