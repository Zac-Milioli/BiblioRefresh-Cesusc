import pandas as pd


df1 = pd.DataFrame({'tombo': [1,2,3,4,5], 'x': [6,7,8,9,10]})
df2 = pd.DataFrame({'tombo': [2,6,9,1,5],'x': [6,7,8,9,10], 'y': [15,645,987,454,12]})
separ = '='*50

print(separ)
print(df1)
print(separ)
print(df2)
print(separ)

df1 = df1[~df1['tombo'].isin(df2['tombo'])]
print(df1)
print(separ)