#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: primeNum.py
@time: 2019/4/19 15:34
@brief: determine whether a number is prime number
'''

while True:
    try:
        num = int(input("please input a number : "))
    except ValueError as err:
        print("{} is not prime number ".format(num))
    else:
        if(num > 1):
            for i in range(2, num):
                if(num%i) == 0:
                    print("{} is not prime number ".format(num))
                    break
            else:
                print("{} is prime number ".format(num))
        else:
            print("{} is not prime number ".format(num))