from bokeh.charts import Scatter, output_file, save
import pandas as pd

# output to static HTML file
output_file("scatter.html")

df = pd.read_csv("../pokemon.csv")

scatter = Scatter(df, x='Sp. Atk', y='Sp. Def', color='Type 1', title="Attack vs. Defense", xlabel="Special Attack Power", ylabel="Special Defense Power", background_fill_color = "LightCyan")

output_file('scatter2.html')

# show the results
save(scatter)