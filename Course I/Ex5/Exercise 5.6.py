from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-application")
location = geolocator.reverse("38.2552027,140.8349828", language="en")
print(location)

aoba_loc = geolocator.geocode("東北大学青葉山キャンパス")
aoba_loc_coord = (aoba_loc.latitude, aoba_loc.longitude)
print(aoba_loc_coord)

from geopy import distance

katahira_loc = geolocator.geocode("Katahira Campus")
katahira_loc_coord = (katahira_loc.latitude, katahira_loc.longitude)
print(distance.distance(aoba_loc_coord,katahira_loc_coord).km)

'''
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.5)


import pandas as pd
df = pd.read_table('location.txt',sep='\s+')
df['location'] = df['longitude'].astype(str) + ','+ df['latitude'].astype(str)
df['ADDRESS'] = df['location'].apply(geocode)
print(df['ADDRESS'])

df['ADDRESS'] = df['ADDRESS'].astype(str)
print(df['ADDRESS'].str.contains('仙台'))
'''