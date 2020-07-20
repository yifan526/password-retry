password = 'a123456'
x = 2

while x >= 0 :
	pass1 = input('please enter passcode')
	if x == 0:
		break
	elif pass1 != password:
		print (x,' attempts left')
		x = x - 1
	else:
		print ('password correct')
		break