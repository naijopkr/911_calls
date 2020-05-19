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
print(df['zip'].value_counts().head(5))
print()

print_color('What are the top 5 townships (twp) for 911 calls?')
print(df['twp'].value_counts().head(5))
print()

print_color(
    'Take a look at the \'title\' column, how many ' +
    'unique title codes are there?'
)
unique_title = df['title'].nunique()
print(f'Unique titles: {unique_title}')
print()

print_color(
    'Get the reason in the column \'title\' and ' +
    'use apply to create a new column with it'
)
df['Reason'] = df['title'].apply(
    lambda title:
        re.match(
            '(fire|ems|traffic)',
            title,
            flags=re.IGNORECASE
        )[0]
)
print(df.head())
print()

print_color('What is the most common Reason for 911 call?')
print(df['Reason'].value_counts())
print()

print_color('Use seaborn to creat a countplot of 911 calls by Reason')
try:
    fig1, ax1 = plt.subplots()
    sns.countplot(df['Reason'], ax=ax1, palette='viridis')
    plt.savefig('output/reasons.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color(
    'Some extra, training to plot different ' +
    'graphs in the same file.'
)
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

print_color(
    'Create 3 new columns Hour, Day of Week ' +
    'and Month based on the timeStamp column.'
)
df['Hour'] = df['timeStamp'].apply(
    lambda time:
        time.hour
)
print(df['Hour'].head())
print()

df['day_of_week'] = df['timeStamp'].apply(
    lambda time:
        calendar.day_abbr[time.dayofweek]
)
print(df['day_of_week'].value_counts())
print()


df['month'] = df['timeStamp'].apply(
    lambda time:
        time.month
)
df['month_abbr'] = df['timeStamp'].apply(
    lambda time:
        calendar.month_abbr[time.month]
)
print(df['month_abbr'].value_counts())
print()

print_color(
    'Create a countplot of the \'day_of_week\'' +
    'column with the hue based on \'Reason\' column'
)
try:
    fig3, ax3 = plt.subplots()
    sns.countplot(
        x='day_of_week',
        data=df,
        hue='Reason',
        palette='viridis',
        ax=ax3
    )
    box = ax3.get_position()
    ax3.set_position([
        box.x0,
        box.y0,
        box.width * 0.8,
        box.height
    ])
    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc=2,
        borderaxespad=0
    )
    plt.savefig('output/day_of_week.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color(
    'Create a countplot of the \'month\' column ' +
    'with the hue based on \'Reason\' column'
)
try:
    fig4, ax4 = plt.subplots()
    sns.countplot(
        x='month',
        data=df,
        hue='Reason',
        palette='viridis',
        ax=ax4
    )
    box = ax4.get_position()
    ax4.set_position([
        box.x0,
        box.y0,
        box.width * 0.8,
        box.height
    ])
    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc=2,
        borderaxespad=0
    )
    plt.savefig('output/month.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color(
    'Create a simple plot of the dataframe ' +
    'indicating the count of calls per month.'
)
count_month = df.groupby('month').count()
print(count_month.head())
print()
try:
    fig5, ax5 = plt.subplots()
    count_month['e'].plot()
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

print_color('Create new column for date.')
df['date'] = df['timeStamp'].apply(
    lambda time: time.date()
)
by_date = df.groupby('date').count()
try:
    fig7, ax7 = plt.subplots()
    by_date['e'].plot()
    plt.tight_layout()
    plt.savefig('output/by_date.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Traffic by date')
traffic = df[df['Reason'] == 'Traffic'].groupby('date').count()

try:
    fig8, ax8 = plt.subplots()
    sns.lineplot(x=traffic.index, y=traffic['e'], ax=ax8)
    plt.title('Traffic')
    plt.savefig('output/traffic.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Fire by date')
fire = df[df['Reason'] == 'Fire'].groupby('date').count()

try:
    fig9, ax9 = plt.subplots()
    sns.lineplot(x=fire.index, y=fire['e'], ax=ax9)
    plt.title('Fire')
    plt.savefig('output/fire.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('EMS by date')
ems = df[df['Reason'] == 'EMS'].groupby('date').count()

try:
    fig10, ax10 = plt.subplots()
    sns.lineplot(x=ems.index, y=ems['e'], ax=ax10)
    plt.title('EMS')
    plt.savefig('output/ems.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Plot day of week vs hour heatmap')
hours_columns = (
    df.groupby(['day_of_week', 'Hour']).count().unstack()
)
print(hours_columns['e'].head())

try:
    fig11, ax11 = plt.subplots()
    sns.heatmap(data=hours_columns['e'], ax=ax11, cmap='viridis')
    plt.savefig('output/hour_day_heatmap.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Plot day of week vs hour cluster grid')
try:
    fig12, ax12 = plt.subplots()
    sns.clustermap(data=hours_columns['e'], cmap='viridis')
    plt.savefig('output/hour_day_cluster.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Create same plots but with month as columns')
month_columns = (
    df.groupby(['day_of_week', 'month']).count().unstack()
)
print(month_columns['e'].head())
print()

print_color('Month vs day of week heatmap')
try:
    fig13, ax13 = plt.subplots()
    sns.heatmap(data=month_columns['e'], ax=ax13, cmap='viridis')
    plt.savefig('output/month_day_heatmap.png')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()

print_color('Month vs day of week cluster')
try:
    fig14, ax14 = plt.subplots()
    sns.clustermap(data=month_columns['e'])
    plt.savefig('output/month_day_cluster.png', cmap='viridis')
except:
    print('ERROR IN PLOTTING THIS FIGURE.')
else:
    print('Success!')
finally:
    print()
