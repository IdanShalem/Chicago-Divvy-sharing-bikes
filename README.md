# Chicago-Divvy-sharing-bikes
In this project, I analyze data from the database of Chicago Divvy sharing bikes in 2016. The database contains more than 70 thousand rentals. I analyze the data by consumers statistics and rentals statistics in order to examine the target audience and the consumer's behavior. I've made this project by using python.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import seaborn as sns

df = pd.read_csv('Chicago-Divvy-2016.csv',index_col = 'trip_id')
df['starttime'] = pd.to_datetime(df['starttime'])
df['weekday'] = df['starttime'].dt.dayofweek
df['hour'] = df['starttime'].dt.hour

## Making a Pie chart for rentings by gender
fig1, axs = plt.subplots(1, 2, figsize=(17, 6))
Customer_counts = df['gender'].value_counts()
Guests_counts = df['usertype'].value_counts()
labels = ['Males', 'Females', 'Guests']
sizes = [Customer_counts['Male'], Customer_counts['Female'], Guests_counts['Customer']]
explode = (0.02, 0.02, 0.02)  

axs[0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
axs[0].axis('equal') 

## Making a bar chart for trip durations means by gender
grouped_gender = df.groupby('gender')['tripduration'].agg(np.mean)/60
grouped_guests = df.groupby('usertype')['tripduration'].agg(np.mean)/60
duration_gender = [grouped_gender['Male'].round(), grouped_gender['Female'].round(),
                   grouped_guests['Customer'].round()]
x = np.arange(len(labels))  
width = 0.5  
#fig, ax = plt.subplots()
rects1 = axs[1].bar(x-width/20, duration_gender, width)
axs[1].set_ylabel('Duration By Minutes')
axs[1].set_title('Trip Duration Average By Gender')
axs[1].set_xticks(x)
axs[1].set_xticklabels(labels)
def autolabel(rects,ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),xy=(rect.get_x() + rect.get_width() / 2, height),xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1,axs[1])
plt.show()

year_group = df.groupby('birthyear')
age_dict={}
for i , (year,year_data) in enumerate(year_group):
    age_dict[2020-year]=year_data['birthyear'].count()
ages = list(age_dict.keys())
occurencies = list(age_dict.values())
fig, ax = plt.subplots( figsize=(11, 5) ,sharey=True)
ax.plot(ages, occurencies)
ax.set_title('Age Frequencies')
ax.set_xlabel('Age')
ax.set_ylabel('Frequencies')
plt.xticks(np.arange(min(ages), max(ages)+1, 4.0))
plt.show()

## Making a bar chart for trip durations means by days
fig1, axs = plt.subplots(1, 2, figsize=(22, 8))
grouped = df.groupby('weekday')['tripduration'].agg(np.mean)/60
bars = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
x = np.arange(len(bars))  
width = 0.5  
rects1 = axs[0].bar(x-width/20, grouped.round(), width)
axs[0].set_ylabel('Duration By Minutes')
axs[0].set_title('Trip Duration Average By Days')
axs[0].set_xticks(x)
axs[0].set_xticklabels(bars)
autolabel(rects1,axs[0])
days_counts = []
groupdays = df.groupby('weekday')
for i, (day, day_data) in enumerate(groupdays):
        days_counts.append(day_data['weekday'].count())
rects2 = axs[1].bar(x-width/20, days_counts, width)
axs[1].set_title('Amount of Rentings By Days')
axs[1].set_ylabel('Amount of Rentings')
axs[1].set_xticks(x)
axs[1].set_xticklabels(bars)
autolabel(rects2,axs[1])
plt.show()

grouped_station = df.groupby('from_station_name')
list_station = []
counter=0
for (i,(name, name_data)) in enumerate(grouped_station):
    list_station.append({"Station" : name, "No." : name_data['tripduration'].count()})
list_station = sorted(list_station, key = lambda i:i['No.'],reverse=True)
stationdf = pd.DataFrame()
for i in list_station:
    if counter < 10:
        stationdf = stationdf.append({'Station': i['Station'], 'No.': i['No.']}, ignore_index=True)
        counter+=1
    else:
        break
sns.set(rc={'figure.figsize':(10,8)})
ax = stationdf.plot.bar(x='Station', y='No.', rot=45)
ax.set_title('Amount of Rentings By Stations')
ax.set_ylabel('Amount of Rentings')
plt.show()

heatmap_tripduration=np.zeros((24,7))
heatmap_counts = np.zeros((24,7))
dict2={}
for (i, (day, day_data)) in enumerate(groupdays):
    #dict2[day_name]=day_data['tip_amount'].sum()
    grouphour=day_data.groupby('hour')
    for (j, (hour_name, hour_data)) in enumerate(grouphour):
        heatmap_tripduration[hour_name][day]=(hour_data['tripduration'].mean())/60
        heatmap_counts[hour_name][day]=(hour_data['tripduration'].count())
heatmap_tripduration = pd.DataFrame(heatmap_tripduration,index = ["00:00", "01:00","02:00", "03:00","04:00", "05:00","06:00", "07:00",
                                       "08:00", "09:00","10:00", "11:00","12:00", "13:00","14:00", "15:00",
                                       "16:00", "17:00","18:00", "19:00","20:00", "21:00","22:00", "23:00"] ,
                       columns = [bars])
sns.set(rc={'figure.figsize':(15,10)})
ax = sns.heatmap(heatmap_tripduration, xticklabels=1, yticklabels=1, linewidths=.5 ,cmap="YlGnBu")
ax.set(xlabel='Days', ylabel='Hours', title="Trip duration average for 7 weekdays & 24 hours")
plt.show()
heatmap_counts = pd.DataFrame(heatmap_counts,index = ["00:00", "01:00","02:00", "03:00","04:00", "05:00","06:00", "07:00",
                                       "08:00", "09:00","10:00", "11:00","12:00", "13:00","14:00", "15:00",
                                       "16:00", "17:00","18:00", "19:00","20:00", "21:00","22:00", "23:00"] ,
                       columns = [bars])
sns.set(rc={'figure.figsize':(15,10)})
ax = sns.heatmap(heatmap_counts,xticklabels=1, yticklabels=1, linewidths=.5 ,cmap="YlGnBu")
ax.set(xlabel='Days', ylabel='Hours', title="Amount of Rentings for 7 weekdays & 24 hours")
plt.show()
