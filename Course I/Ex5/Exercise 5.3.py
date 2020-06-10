# Exercise 5.3

import pandas as pd
import numpy as np

room_data = pd.read_csv('room_stats.csv')

# A

df = room_data.loc[(pd.to_datetime(room_data['date']).dt.day==2)]

print(df)



# B
light_off = room_data[room_data['Light']==0]

light_hour = (pd.to_datetime(light_off['date']).dt.hour)

light_hour.to_csv('light_off_data.csv')

# C

import pandas as pd

room_data = pd.read_csv('room_stats.csv')

room_data['date'] = pd.to_datetime(room_data['date'])
room_data = room_data.set_index('date')



print("\nThe Maximum of Humidity and CO2 per 300 seconds")
group3 = room_data.resample('600S').max()

CO2 = group3[['CO2']]


CO2 = CO2.loc['2015-02-03 06:00':'2015-02-03 18:00']

print(CO2)

CO2.to_csv('max_co2.csv')


# D

room_data = pd.read_csv('room_stats.csv')

day_data = pd.to_datetime(room_data['date']).dt.day
hour_data = pd.to_datetime(room_data['date']).dt.hour
minute_data = pd.to_datetime(room_data['date']).dt.minute

stats = room_data[['Temp.','Humid.','CO2']]

room_stats2 = pd.concat([day_data, hour_data, minute_data, stats], axis=1)

room_stats2 = room_stats2.set_axis(['day', 'hour', 'minute', 'Temp.', 'Humid.','CO2'], axis=1, inplace=False)


print(room_stats2)

room_stats2.to_csv('room_stats2.csv')
