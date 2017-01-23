#Imports and things
from bokeh.charts import BoxPlot, output_file, save
from bokeh.sampledata.autompg import autompg as df
import pandas as pd

#Turn csv file into DataFrame
df = pd.read_csv('pokemon.csv')

#Create BoxPlot
box = BoxPlot(df, values='HP', label='Type 1', title="HP Box Plot", plot_width=400, legend = False, color='Type 1')

#File
output_file('HP_BoxPlot.html')

#Save
save(box)
