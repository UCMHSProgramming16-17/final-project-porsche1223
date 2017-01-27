from bokeh.charts import Scatter, output_file, save
import pandas as pd

# output to static HTML file
output_file("scatter.html")

df = pd.read_csv("../pokemon.csv")

scatter = Scatter(df, x='Attack', y='Defense', color='Type 1', title="Attack vs. Defense", xlabel="Attack Power", ylabel="Defense Power", background_fill_color = "LightCyan")

output_file('scatter.html')

# show the results
save(scatter)