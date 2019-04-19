#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: triangleArea.py
@time: 2019/4/19 9:27
@brief: calculate area of triangle
    hp = half of perimeter
    area = sqrt ( hp*(hp - a)*(hp - b)*(hp - c) )
'''
import math


def triangle_area(a, b, c) :
    if a < (b + c) and a > abs(b - c) and a > 0 and b > 0 and c > 0 :
        hp = (a + b + c) / 2
        area = math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))
        print("triangle area : {0}".format(area))
    else :
        print("{0},{1},{2} can not build a triangle.", a, b, c)


while True :
    print("please input three side's length of triangle : ")
    a = float(input("input a : "))
    b = float(input("input b : "))
    c = float(input("input c : "))
    triangle_area(a, b, c)
