# -*- coding:utf-8 -*-
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import random

def get_random_numbers(start, end, how_many):
    return [random.randint(start, end) for i in range(how_many)]

def get_array():
    result = []
    for i in range(1,13):
        result.append(i)
    return result

x = get_array()
y = get_random_numbers(0,2000,12)
y2 = get_random_numbers(0,2000,12)

matplotlib.rc('font',family='AppleGothic')
plt.figure(figsize=(10,5))
plt.plot(x,y,'ro-',label='2015', color='#2196F3', linewidth=3, alpha=0.5)
plt.plot(x,y2,'bo-',label='2016', color='#F44336', linewidth=3, alpha=0.5)

plt.title('Rainfall')
plt.xlabel('Month')
plt.ylabel('mm')
plt.legend(['2016','2015'])

plt.xlim([1,12])
plt.ylim([0,2000])
plt.xticks(x)

plt.grid()
plt.tick_params(bottom='off', top='off', left='off', right='off',
                labelbottom='on', labelleft='on')

plt.show()