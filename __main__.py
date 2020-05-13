import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.graph_objects as go
import plotly.io as pio

df = pd.read_csv('911.csv', dtype=dict(
    lat = float,
    lng = float,
    desc = str,
    zip = str,
    title = str,
    timeStamp = str,
    twp = str,
    addr = str,
    e = str
))

print('911 CALLS INFO')
print(df.info())

print('911 CALLS HEAD')
print(df.head())

print('What are the top 5 zipcodes for 911 calls?')
top_zipcodes = df.groupby('zip').count().sort_values(ascending = False, by = 'e')
print(top_zipcodes['e'].head(5))
