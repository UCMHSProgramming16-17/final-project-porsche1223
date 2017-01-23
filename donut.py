from bokeh.charts import Donut, save, output_file
import csv
import pandas as pd

# utilize utility to make it easy to get json/dict data converted to a dataframe
df = pd.read_csv("Pokemon.csv")

Type_1 = df['Type 1']

types = list(set(Type_1))

t1 = sorted(types, key=str.lower)

donut = Donut(types, t1)

output_file("Donut.html")

save(donut)