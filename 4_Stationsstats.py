## Building a bar chart for 10 most busy stations
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
