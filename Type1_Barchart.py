import csv
import pandas as pd
from bokeh.charts import Bar, output_file, save

df = pd.read_csv('Pokemon.csv')

types = [df['Type 1']]

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

types1 = remove_duplicates(df['Type 1'])

Bar1 = Bar(df, label=types1, values='Type 1', title='Frequency of Type 1 Pokemon')

output_file('Type1_Barchart.html')

save(Bar1)
