## Building a Pie chart for rentings statistics by gender
fig1, axs = plt.subplots(1, 2, figsize=(17, 6))
Customer_counts = df['gender'].value_counts()
Guests_counts = df['usertype'].value_counts()
labels = ['Males', 'Females', 'Guests']
sizes = [Customer_counts['Male'], Customer_counts['Female'], Guests_counts['Customer']]
explode = (0.02, 0.02, 0.02)  
axs[0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
axs[0].axis('equal') 

## Building a bar chart for average trip duration by gender
grouped_gender = df.groupby('gender')['tripduration'].agg(np.mean)/60
grouped_guests = df.groupby('usertype')['tripduration'].agg(np.mean)/60
duration_gender = [grouped_gender['Male'].round(), grouped_gender['Female'].round(),
                   grouped_guests['Customer'].round()]
x = np.arange(len(labels))  
width = 0.5  
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

## Building a line chart for ages frequencies
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
