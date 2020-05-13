import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

from termcolor import colored

# dataset: https://www.kaggle.com/mchirico/montcoalert/data
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

def print_color(text, color):
    print(colored(text, color=color))

print_color('911 CALLS INFO', 'red')
print(df.info())
print()

print_color('911 CALLS HEAD', 'red')
print(df.head())
print()

print_color('What are the top 5 zipcodes for 911 calls?', 'green')
top_zipcodes = df.groupby('zip').count().sort_values(ascending = False, by = 'e')
print(top_zipcodes['e'].head(5))
print()

print_color('What are the top 5 townships (twp) for 911 calls?', 'green')
top_twp = df.groupby('twp').count().sort_values(ascending = False, by = 'e')
print(top_twp['e'].head(5))
print()

print_color('Take a look at the \'title\' column, how many unique title codes are there?', 'green')
unique_title = df['title'].unique()
print(f'Unique titles: {len(unique_title)}')

print_color('Get the reason in the column \'title\' and use apply to create a new column with it', 'green')
df['Reason'] = df['title'].apply(lambda title: re.match('(fire|ems|traffic)', title, flags=re.IGNORECASE)[0])
print(df.head())

print_color('Use seaborn to creat a countplot of 911 calls by Reason', 'green')
f = plt.Figure()
f.add_subplot = sns.countplot(df['Reason'])
plt.savefig('output/reasons.png')
