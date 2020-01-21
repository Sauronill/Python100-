#! /usr/bin/env python3

import re

def Min(firstVal, secondVal):
	if firstVal <= secondVal:
		return firstVal
	else:
		return secondVal

if __name__ == '__main__':
	coins = input("Please input coin array:")
	MaxValue = int(input("All coin value:"))
	coinArr = re.split("[,]", coins)
	coinNum = coinArr.__len__()
	isfirst = True
	# Static coin num in everyValue
	valueArr = [0 for i in range (0,MaxValue+1)]
	for i in range (0, MaxValue + 1):
		for j in range (0, coinNum):
			print ("{0}  {1}".format(i,j))
			if i >= int(coinArr[j]):
				if (0 == i - int(coinArr[j])):
					valueArr[i] = 1
				elif (valueArr[i - int(coinArr[j])] != 0):
					if (valueArr[i] == 0):
						valueArr[i] = valueArr[i - int(coinArr[j])] + 1
					else:
						if (valueArr[i - int(coinArr[j])] + 1) < valueArr[i]:
							valueArr[i] = valueArr[i - int(coinArr[j])] + 1		
		print (valueArr)
	if (0 == valueArr[MaxValue]):
		print ("-1")
	else:
		print (valueArr[MaxValue])

