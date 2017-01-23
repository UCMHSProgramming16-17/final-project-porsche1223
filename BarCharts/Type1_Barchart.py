import csv
import pandas as pd
from bokeh.charts import Bar, output_file, save

df = pd.read_csv('pokemon.csv')

Type_1 = df['Type 1']

types = list(set(Type_1))

t1 = sorted(types, key=str.lower)

numIndices = len(t1)

num = len(Type_1)

x = 0
freq = []

while x < numIndices:
    freq.append(0)
    x += 1

x = 0

while x < num:
    y = 0
    while y < numIndices:
        if str(Type_1[x]) == str(t1[y]):
            freq[y] +=1
        
        y+=1
        
    x+=1

data = {'Type': t1, 'Freq': freq}
df = pd.DataFrame(data)

from bokeh.charts import Bar, output_file, save
from bokeh.layouts import row

# x-axis labels pulled from the interpreter column, stacking labels from sample column
bar = Bar(df, values='Freq', label='Type', title="Frequency of Type 1 Pokemon", legend='top_left', plot_width=400, color = 'blue')

output_file("Type1_Barchart.html")

save(bar)