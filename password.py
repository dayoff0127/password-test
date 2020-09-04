password = 'a123456'
n = 2
while True :
	a = input('請輸入密碼:')
	if a == password :
		print('登入成功')
		break
	else :
		print('密碼錯誤! 還有', n, '次機會')
		n = n - 1
		if n == -1 :
			break