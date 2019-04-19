#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: linerEqInTwoUnkown.py
@time: 2019/4/18 18:04
@brief: caculate the result of the liner equation in two unknows , like the ax^2 + bx + c = 0
            (1) b^2 - 4ac = 0 , only one solution
            (2) b^2 - 4ac = 0 ,  two real numbers
            (3) b^2 - 4ac < 0 ,  two imaginary numbers
'''

import cmath

while True:
    print("please input a equation like ax^2 + bx + c = 0")
    a = float(input("input a : "))
    b = float(input("input b : "))
    c = float(input("input c : "))
    d = cmath.sqrt(b**2 - 4 * a * c)
    x1 = (-b - d) / (2*a)
    x2 = (-b+d) / (2*a)
    print("x1 : {:.2f}, x2: {:.2f}".format(x1, x2))
