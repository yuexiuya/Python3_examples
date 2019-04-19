#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: tempSwitch.py
@time: 2019/4/19 9:51
@brief: C = ( F - 32 ) /1.8
              F = C*1.8 + 32
'''


while True:
    try:
        temp = eval(input("input temp like {\"F\":temp} or {\"C\":temp} : "))
        print("your input is {}".format(temp))
    except SyntaxError as err:
        print("{}, please input again".format(err))
    except ValueError as err:
        print("{}, please input again".format(err))
    else:
        if "F" in temp:
            c_temp = ( temp["F"] - 32 ) / 1.8
            print("Celsius is {:.2f}".format(c_temp))
        elif "C" in temp:
            f_temp = temp["C"]*1.8 + 32
            print("fahrenheit is {:.2f}".format(f_temp))
        else:
            print("your input is error, please input age")
            continue




