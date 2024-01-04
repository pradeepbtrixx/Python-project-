def evaluate_exp():
	val = input('enter : ')
	try :
		if eval(val):
			print(eval(val))
	except :
		print(-1)

if __name__ == "__main__":
	evaluate_exp()