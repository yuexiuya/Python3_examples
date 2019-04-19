#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: odd_even.py
@time: 2019/4/19 14:23
@brief: determine user's input is odd or even
'''

while True:
    try:
        num = int(input("please input your number : "))
    except ValueError as err:
        print(err)
    else:
        if(num%2):
            print("number is odd")
        else:
            print("number is even")

