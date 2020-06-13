# Exercise 5.6 (Extra)

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="chun")

# Finding the location name of the coordinate
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.reverse, min_delay_seconds=0.5)

import pandas as pd

location_data = pd.read_csv("locations.csv").astype(str)

lat_long = location_data['longitude'] + ',' + location_data['latitude']
print(lat_long)

address = lat_long.apply(geocode).astype(str)
print(address)

miyagi_prf = '宮城県'
yamagata_prf = '山形県'

# Number of locations in Miyagi Prefecture (宮城県)

contains_miyagi = address.str.contains(miyagi_prf)
#print(contains_miyagi)
print(f"From the data, number of city in Miyagi is {contains_miyagi.sum()}.")



# Number of locations in Yamagata Prefecture (山形県)

contains_yamagata = address.str.contains(yamagata_prf)
#print(contains_yamagata)
print(f"From the data, number of city in Yamagata is {contains_yamagata.sum()}.")
