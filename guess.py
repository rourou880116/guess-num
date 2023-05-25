import random

r = random.randint(1,100)

while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		break
	elif num < r:
		print('比真實數字小')
	else:
		print('比真實數字大')


