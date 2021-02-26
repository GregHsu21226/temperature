temp = input('請輸入溫度: ')
form = input('請輸入攝氏或華氏: ')
temp = float(temp)

if form == '攝氏':
	c = temp
	f = c*9/5 + 32
	print('相當於華氏: ',f,'度')

if form == '華氏':
	f = temp
	c = (f-32)*5/9
	print('相當於攝氏: ',c,'度')
