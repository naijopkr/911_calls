import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.graph_objects as go
import plotly.io as pio

from termcolor import colored

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

print(colored('911 CALLS INFO', color='red'))
print(df.info())
print()

print(colored('911 CALLS HEAD', color='red'))
print(df.head())
print()

print(colored('What are the top 5 zipcodes for 911 calls?', color='green'))
top_zipcodes = df.groupby('zip').count().sort_values(ascending = False, by = 'e')
print(top_zipcodes['e'].head(5))
print()

print(colored('What are the top 5 townships (twp) for 911 calls?', color='green'))
top_twp = df.groupby('twp').count().sort_values(ascending = False, by = 'e')
print(top_twp['e'].head(5))
print()
