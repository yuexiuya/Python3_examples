#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: randomNum.py
@time: 2019/4/19 9:47
@brief: generate random number
'''

import random
import time

while True:
    print("random  number : {0}".format(random.randint(0, 100)))
    time.sleep(2)