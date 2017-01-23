import csv
import pandas as pd
from bokeh.charts import Bar, output_file, save

df = pd.read_csv('PokemonGO1.csv')

Type_1 = df['Type 1']

types = list(set(Type_1))

t1 = sorted(types, key=str.lower)

freq = [0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0]

x = 0

while x <= 3:
    y = 0
    while y <= 14:
        if str(Type_1[x]) == str(t1[y]):
            freq[y] +=1
        else:
            y+=1
        
    x+=1


print(freq)