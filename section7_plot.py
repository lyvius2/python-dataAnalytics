# -*- coding:utf-8 -*-
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import random

# x = [1,2,3]
# y = [5,7,4]
#
# x2 = [1,2,3]
# y2 = [10,14,17]
#
# plt.plot(x,y)
# plt.plot(x2,y2)
#
# matplotlib.rc('font',family='AppleGothic')
# plt.plot(x,y,label=u'첫번째')
# plt.plot(x2,y2,label=u'두번째')
# plt.legend()
# plt.show()

def get_random_numbers(start, end, how_many):
    return [random.randint(start, end) for i in range(how_many)]

def get_array():
    result = []
    for i in range(1,13):
        result.append(i)
    return result

x = get_array()
y = get_random_numbers(0,100,12)

x2 = get_array()
y2 = get_random_numbers(0,100,12)

plt.plot(x,y)
plt.plot(x2,y2)

matplotlib.rc('font',family='AppleGothic')
plt.title('Criminals')
plt.plot(x,y,'ro-',label='Seoul')
plt.plot(x2,y2,'bo-',label='Busan')
plt.xlabel('Month')
plt.ylabel('Number of Criminals')
plt.legend(loc='lower right')
plt.show()