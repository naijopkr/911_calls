import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import calendar

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

def print_color(text, color = 'green'):
    print(colored(text, color=color))

print_color('911 CALLS INFO', 'red')
print(df.info())
print()

print_color('911 CALLS HEAD', 'red')
print(df.head())
print()

print_color('What are the top 5 zipcodes for 911 calls?')
top_zipcodes = df.groupby('zip').count().sort_values(ascending = False, by = 'e')
print(top_zipcodes['e'].head(5))
print()

print_color('What are the top 5 townships (twp) for 911 calls?')
top_twp = df.groupby('twp').count().sort_values(ascending = False, by = 'e')
print(top_twp['e'].head(5))
print()

print_color('Take a look at the \'title\' column, how many unique title codes are there?')
unique_title = df['title'].unique()
print(f'Unique titles: {len(unique_title)}')
print()

print_color('Get the reason in the column \'title\' and use apply to create a new column with it')
df['Reason'] = df['title'].apply(lambda title: re.match('(fire|ems|traffic)', title, flags=re.IGNORECASE)[0])
print(df.head())
print()

print_color('What is the most common Reason for 911 call?')
top_reason = df.groupby('Reason').count().sort_values(ascending=False, by='e')
print(top_reason['e'])
print()

print_color('Use seaborn to creat a countplot of 911 calls by Reason')
try:
    fig1, ax1 = plt.subplots()
    sns.countplot(df['Reason'], ax=ax1)
    plt.savefig('output/reasons.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Some extra, training to plot different graphs in the same file.')
try:
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x=df['lat'], y=df['lng'], ax=ax2)
    plt.savefig('output/scatter_lat_lng.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Convert the \'timeStamp\' column to timestamp type')
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(df.info())
print()

print_color('Create 3 new columns Hour, Day of Week and Month based on the timeStamp column.')
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
print(df['Hour'].head())
print()

df['day_of_week'] = df['timeStamp'].apply(lambda time: calendar.day_abbr[time.dayofweek])
top_day_week = df.groupby('day_of_week').count().sort_values(ascending=False, by='e')
print(top_day_week['e'])
print()


df['month'] = df['timeStamp'].apply(
    lambda time: time.month
)
df['month_abbr'] = df['timeStamp'].apply(
    lambda time: calendar.month_abbr[time.month]
)
top_month = df.groupby('month').count().sort_values(
    ascending=False, by='e'
)
print(top_month['e'])
print()

print_color('Create a countplot of the \'day_of_week\' column with the hue based on \'Reason\' column')
try:
    fig3, ax3 = plt.subplots()
    sns.countplot(df['day_of_week'], hue=df['Reason'], ax=ax3)
    plt.savefig('output/day_of_week.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Create a countplot of the \'month\' column with the hue based on \'Reason\' column')
try:
    fig4, ax4 = plt.subplots()
    sns.countplot(df['month'], hue=df['Reason'], ax=ax4)
    plt.savefig('output/month.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Create a simple plot of the dataframe indicating the count of calls per month.')
count_month = df.groupby('month').count()
try:
    fig5, ax5 = plt.subplots()
    sns.lineplot(x=count_month.index, y=count_month['e'], ax=ax5)
    plt.savefig('output/count_month.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Create a linear fit to the number of calls per month.')
try:
    fig6, ax6 = plt.subplots()
    sns.lmplot(x='month', y='e', data=count_month.reset_index())
    plt.savefig('output/liner_fit.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()
