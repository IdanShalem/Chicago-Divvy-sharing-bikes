df = pd.read_csv('Chicago-Divvy-2016.csv',index_col = 'trip_id')
df['starttime'] = pd.to_datetime(df['starttime'])
df['weekday'] = df['starttime'].dt.dayofweek
df['hour'] = df['starttime'].dt.hour
