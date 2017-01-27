from bokeh.charts import Bar, output_file, save
from bokeh.charts.attributes import cat, color
from bokeh.charts.operations import blend
import csv
import pandas as pd

# utilize utility to make it easy to get json/dict data converted to a dataframe
df = pd.read_csv('pokemon.csv')


bar = Bar(df,
          values=blend('Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
          label=cat(columns='Name', sort=False),
          stack=cat(columns='Stat', sort=False),
          color=color(columns='Stat', palette=['Red', 'Orange', 'Yellow'],
                      sort=False),
          legend='top_right',
          title="Stats for Pokemon")

output_file("stacked_bar.html", title="stacked_bar.py example")

save(bar)
