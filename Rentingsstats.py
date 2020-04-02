## Building a bar chart for average trip duration by days
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

## Building a bar chart for amount of rentings by days
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

## Building heatmaps average trip duration and amount of rentings for 7 weekdays & 24 hours
heatmap_tripduration=np.zeros((24,7))
heatmap_counts = np.zeros((24,7))
dict2={}
for (i, (day, day_data)) in enumerate(groupdays):
    grouphour=day_data.groupby('hour')
    for (j, (hour_name, hour_data)) in enumerate(grouphour):
        heatmap_tripduration[hour_name][day]=(hour_data['tripduration'].mean())/60
        heatmap_counts[hour_name][day]=(hour_data['tripduration'].count())

## Average trip duration
heatmap_tripduration = pd.DataFrame(heatmap_tripduration,index = ["00:00", "01:00","02:00", "03:00","04:00", "05:00","06:00", "07:00",
                                       "08:00", "09:00","10:00", "11:00","12:00", "13:00","14:00", "15:00",
                                       "16:00", "17:00","18:00", "19:00","20:00", "21:00","22:00", "23:00"] ,
                       columns = [bars])
sns.set(rc={'figure.figsize':(15,10)})
ax = sns.heatmap(heatmap_tripduration, xticklabels=1, yticklabels=1, linewidths=.5 ,cmap="YlGnBu")
ax.set(xlabel='Days', ylabel='Hours', title="Trip duration average for 7 weekdays & 24 hours")
plt.show()

## Amount of rentings
heatmap_counts = pd.DataFrame(heatmap_counts,index = ["00:00", "01:00","02:00", "03:00","04:00", "05:00","06:00", "07:00",
                                       "08:00", "09:00","10:00", "11:00","12:00", "13:00","14:00", "15:00",
                                       "16:00", "17:00","18:00", "19:00","20:00", "21:00","22:00", "23:00"] ,
                       columns = [bars])
sns.set(rc={'figure.figsize':(15,10)})
ax = sns.heatmap(heatmap_counts,xticklabels=1, yticklabels=1, linewidths=.5 ,cmap="YlGnBu")
ax.set(xlabel='Days', ylabel='Hours', title="Amount of Rentings for 7 weekdays & 24 hours")
plt.show()
