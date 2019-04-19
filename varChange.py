#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: varChange.py
@time: 2019/4/19 11:14
@brief: exchange user's input var
'''

while True:
    var1 = input("input first var : ")
    var2 = input("input second var : ")
    print("your input is {} and {}".format(var1, var2))
    temp = var1
    var1 = var2
    var2 = temp
    print("after change  is {} and {}".format(var1, var2))