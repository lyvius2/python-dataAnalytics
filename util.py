# -*- coding: utf-8 -*-

def sum_func(*args):
    sum =0
    for i in args:
        sum += 1

    return sum

def echo_func(say):
    return "You said {0}".format(say)