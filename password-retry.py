password = 'a123456'
x = 2
while x >= 0:
	guess_password = input('請輸入密碼: ')
	if guess_password != password and x >= 1:
		print('密碼錯誤還有' ,x ,'次機會')
		x = x - 1
	elif guess_password != password and x == 0:
		break
	else:
		print('登入成功!')
		break