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
		else:
			stack.append(i)
	print(stack)
except:
	print(-1)