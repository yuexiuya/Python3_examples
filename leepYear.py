#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: leepYear.py
@time: 2019/4/19 15:28
@brief: determine whether the year is leep year
'''

while True:
    try:
        year = int(input("please input a year : "))
    except ValueError as err:
        print(err)
    else:
        if(year%100): # special year
            if(year%400):
                print("{0} is leap year".format(year))
            else:
                print("{0} is normal year".format(year))
        else: # normal year
            if(year%4):
                print("{0} is leap year".format(year))
            else:
                print("{0} is normal year".format(year))
