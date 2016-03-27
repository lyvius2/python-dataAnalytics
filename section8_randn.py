# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import matplotlib.pyplot as plt

from numpy.random import randn
sample = randn(1000)
sample2 = randn(1000)
sample[:10]

sample.mean()
sample.std()

plt.hist(sample, bins=100, alpha=0.7, color='#2196F3')
plt.hist(sample2, bins=50, alpha=1.0, color='#FF5722')
plt.show()