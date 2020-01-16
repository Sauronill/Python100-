#! /usr/bin/env python3
'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
#useList
if __name__ == '__main__':
	year = int(input("Please input year:"))
	month = int(input("Please input month:"))
	day = int(input("Please input day:"))
	daysList = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
	dayIdx = 0
	if ((year%4 ==0 and year%100 != 0) or year%400 == 0):
		dayIdx = daysList[month - 1] + day + 1
	else:
		dayIdx = daysList[month - 1] + day
	print ("The day index in this year is {0}".format(dayIdx))


