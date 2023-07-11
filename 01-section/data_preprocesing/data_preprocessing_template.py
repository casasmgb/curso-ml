import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', delimiter=',')

df_fill = df.fillna(method ='bfill')

print (df_fill)

df_mean = df

df_mean['Salary'] = df_mean['Salary'].fillna(df_mean['Salary'].mean())
df_mean['Age'] = df_mean['Age'].fillna(df_mean['Age'].mean())

print (df_mean)

df_mean["Purchased"] = df_mean["Purchased"].astype('category')
print(df_mean.dtypes)

df_mean["PurchasedCategory"] = df_mean["Purchased"].cat.codes
print(df_mean)