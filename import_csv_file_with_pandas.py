import numpy as np
import pandas as pd

df = pd.read_csv('D:\program\githuub and git\Data_Science_with_nikhil\simple_data1.csv')

df.head(3)

df.tail(3)

df.describe()

description = df.describe().round(1)

print(description)

import matplotlib.pyplot as plt

df.hist(bins=30, figsize=(30, 20))
plt.show()

print(df.dtypes)