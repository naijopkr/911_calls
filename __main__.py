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
