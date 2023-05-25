import random

r = random.randint(1,100)
count = 0
while True:
	num = input('請輸入數字: ')
	num = int(num)
	count += 1
	if num == r:
		print('你猜對了!')
		print('這是你猜的第',count,'次')
		break
	elif num < r:
		print('比真實數字小')
	else:
		print('比真實數字大')
	print('這是你猜的第',count,'次')



