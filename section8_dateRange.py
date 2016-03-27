# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import matplotlib.pyplot as plt

from numpy.random import randn

ts = pd.Series(randn(52), \
               index=pd.date_range('1/1/2016', periods=52, freq='W'))


df = DataFrame(randn(52,5), \
               index=ts.index, \
               columns=list('ABCDE'))
df.cumsum().plot()


