#file is too big if I put all of the types on one, so I broke them up into three groups of four and one group of six
#all the necessities
from bokeh.charts import Bar, output_file, save
from bokeh.charts.attributes import cat, color
from bokeh.charts.operations import blend
import csv
import pandas as pd
from bokeh.palettes import Pastel1
from bokeh.layouts import row

#read files
df = pd.read_csv('../pokemon.csv')

df1 = df.sort_values(by='Type 1')

#organize info
Type_1 = df['Type 1']
types = list(set(Type_1))

t1 = sorted(types, key=str.lower)

df2=df1.set_index("Type 1")

#I couldn't figure out how to loop the code and still make different bar charts, so I just copied and pasted it
a = df2.loc[t1[0], :]

bug = Bar(a,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Bug Type Pokemon",
    background_fill_color = 'beige')

b = df2.loc[t1[1], :]

dark = Bar(b,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Dark Type Pokemon",
    background_fill_color = 'beige')
    
c = df2.loc[t1[2], :]

dragon = Bar(c,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Dragon Type Pokemon",
    background_fill_color = 'beige')
    
d = df2.loc[t1[3], :]

electric = Bar(d,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Electric Type Pokemon",
    background_fill_color = 'beige')
    
e = df2.loc[t1[4], :]

fairy = Bar(e,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Fairy Type Pokemon",
    background_fill_color = 'beige')
    
f = df2.loc[t1[5], :]

fighting = Bar(f,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Fighting Type Pokemon",
    background_fill_color = 'beige')
    
g = df2.loc[t1[6], :]

fire = Bar(g,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Fire Type Pokemon",
    background_fill_color = 'beige')

h = df2.loc[t1[7], :]

flying = Bar(h,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Flying Type Pokemon",
    background_fill_color = 'beige')
    
i = df2.loc[t1[8], :]

ghost = Bar(i,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Ghost Type Pokemon",
    background_fill_color = 'beige')

j = df2.loc[t1[9], :]

grass = Bar(j,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Grass Type Pokemon",
    background_fill_color = 'beige')
    
k = df2.loc[t1[10], :]

ground = Bar(k,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Ground Type Pokemon",
    background_fill_color = 'beige')
    
l = df2.loc[t1[11], :]

ice = Bar(l,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Ice Type Pokemon",
    background_fill_color = 'beige')
    
m = df2.loc[t1[12], :]

normal = Bar(m,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Normal Type Pokemon",
    background_fill_color = 'beige')
    
n = df2.loc[t1[13], :]

poison = Bar(n,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Poison Type Pokemon",
    background_fill_color = 'beige')
    
o = df2.loc[t1[14], :]

psychic = Bar(o,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Psychic Type Pokemon",
    background_fill_color = 'beige')
    
p = df2.loc[t1[15], :]

rock = Bar(p,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Rock Type Pokemon",
    background_fill_color = 'beige')

q = df2.loc[t1[16], :]

steel = Bar(q,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Rock Type Pokemon",
    background_fill_color = 'beige')
    
r = df2.loc[t1[17], :]

water = Bar(r,
    values=blend('HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', name='Stats', labels_name='Stat'),
    label=cat(columns='Name', sort=False),
    stack=cat(columns='Stat', sort=False),
    color=color(columns='Stat', palette=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#e5d8bd'],
            sort=False),
    legend='top_right',
    title="Stats for Water Type Pokemon",
    background_fill_color = 'beige')

output_file("Pokemon Types 1-4.html", title="stacked_bar.py example")
    
save(row(bug, dark, dragon, electric))

output_file("Pokemon Types 5-8.html", title="stacked_bar.py example")
    
save(row(fairy, fighting, fire, flying))

output_file("Pokemon Types 9-12.html", title="stacked_bar.py example")
    
save(row(ghost, grass, ground, ice))

output_file("Pokemon Types 13-18.html", title="stacked_bar.py example")
    
save(row(normal, poison, psychic, rock, steel, water))

#I don't know where the stacked_bar.html file got all of its charts from, but that's what I was trying to create at first
