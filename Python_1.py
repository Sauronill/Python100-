#! /usr/bin/env python3
'''
题目：
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

if __name__ == '__main__':
    count = 0
    #组成互不相同三位数
    for i in range(1,5):
        for j in range (1,5):
            for k in range (1, 5):
            #去掉重复数字
                if i != j and i != k and j != k :
                    print ("Idx:{0} : {1}".format((count + 1), i*100+j*10+k))
                    count += 1
    print ("All Count:{0}".format(count))
