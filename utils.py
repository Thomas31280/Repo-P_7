import googlemaps
from datetime import datetime

import config

gmaps = googlemaps.Client(key=config.MAPS_API_KEY)

# find a place with an address
find_place_result = gmaps.find_place('1600 Amphitheatre Parkway, Mountain View, CA', 'textquery')

print(find_place_result)