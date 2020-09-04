password = 'a123456'
n = 3
while True :
	a = input('請輸入密碼:')
	if a == password :
		print('登入成功')
		break
	else :
		n = n - 1
		print('密碼錯誤! 還有', n, '次機會')
		if n == 0 :
			break