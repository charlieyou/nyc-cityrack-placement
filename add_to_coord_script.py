import pandas as pd
import numpy as np
import googlemaps
import json

# Read the file
data = pd.read_csv("LL84_2015.csv", low_memory=False)
# Output the number of rows
print(data.columns)
# See which headers are available
print(list(data))

print(data.columns)


# Remove last three empty columns
data.drop(['Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14'], axis=1, inplace =True)

# Add spaces for latitude and longitude
data["Latitude"] = np.nan
data["Longitude"] = np.nan

gmaps = googlemaps.Client(key='AIzaSyCJvjykFmmokaAoJ2QllOH6FzeTsnMkhmE')
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print geocode_result

# Calculate Lat and Long using Google API
for index,row in data.iterrows():
	street_number = row['Street_Number']
	s = row['Street_Address']
	street_address = ''.join([i for i in s if not i.isdigit()])

	gmaps = googlemaps.Client(key='AIzaSyCJvjykFmmokaAoJ2QllOH6FzeTsnMkhmE')
	print gmaps.geocode(street_number+' '+street_address+'New York, NY')

	lat = json.loads(geocode_result)['geometry']['location']['lat']
	#lng = json.loads(geocode_result)['geometry']['location']['lng']
	#print lat
	#print geocode_result['geometry'], geocode_result['lng']
	
	# API KEY: AIzaSyCJvjykFmmokaAoJ2QllOH6FzeTsnMkhmE