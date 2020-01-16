#! /usr/bin/env python3
'''
题目：
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
if __name__ == '__main__':
	profit = int(input("Please input profit:"))
	limit = [1000000, 600000, 400000, 200000, 100000]
	rate = [0.01, 0.015, 0.03, 0.05, 0.075]
	money = 0
	for i in range (0, 5):
		if (profit > limit[i]):
			money += (profit - limit[i]) * rate[i]
			profit = limit[i]
	# profit is less than 100000
	money += profit * 0.1
	print ("Money:{0}".format(money))
