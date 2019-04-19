#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: useIf.py
@time: 2019/4/19 11:19
@brief: judge user's input number is  positive, negative or zero
'''

num = float(input("please input a number : "))

if num > 0 :
    print("number {} is positive ".format(num))
elif num < 0 :
    print("number {} is negative ".format(num))
else :
    print("number {} is zero ".format(num))
