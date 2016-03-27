import pandas as pd
from pandas import Series, DataFrame

titanic_df = pd.read_csv('./titanic_data.csv')
print titanic_df.head()