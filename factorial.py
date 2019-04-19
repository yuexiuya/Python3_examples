#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: factorial.py
@time: 2019/4/19 15:44
@brief: n! = 1*2*...*(n-1)*n, 0! = 1, negative numbers do not have factorial
'''


while True:
    try:
        factorial = 1
        num = int(input("please input a number : "))
    except ValueError as err:
        print("{} does not have factorial ".format(num))
    else:
        if(num < 0):
            print("{} does not have factorial ".format(num))
        elif(num == 0):
            print("!{0} : {1}".format(num, factorial))
        else:
            for i in range(1, num+1):
                factorial = i*factorial
            else:
                print("!{0} : {1}".format(num, factorial))

