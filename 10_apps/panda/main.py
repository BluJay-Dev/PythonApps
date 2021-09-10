import os
import pandas

df1 = pandas.read_json('supermarkets.json')
df5 = pandas.read_csv('data.txt', sep=';')
df5.columns = ['ID', 'Address', 'City','Zip','Country','Name','Employees']
df5.set_index("ID")
print(df5)
