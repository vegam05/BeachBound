import csv
import datetime
from fetcher import returner

response_data = returner(
    19.1194644,  # Latitude
    72.8201599,  # Longitude
    "gfs",  # Model
    ["temp", "wind", "dewpoint", "rh", "pressure"],  # Parameters
    ["surface"],  # Levels
    "xyz"  # API Key
)

# Converting millisecond timestamps into standard format( YYYY-MM-DD HH:MM:SS )
def convert_timestamp(ts):
    return datetime.datetime.utcfromtimestamp(ts / 1000).strftime('%Y-%m-%d %H:%M:%S')

with open('weather_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Features(Top row)
    header = ['Timestamp', 'Temperature (K)', 'Dewpoint (K)', 'Relative Humidity (%)', 'Pressure (Pa)']
    writer.writerow(header)

    
    for i in range(len(response_data['ts'])):
        row = [
            convert_timestamp(response_data['ts'][i]),
            response_data['temp-surface'][i] if 'temp-surface' in response_data else None,
            response_data['dewpoint-surface'][i] if 'dewpoint-surface' in response_data else None,
            response_data['rh-surface'][i] if 'rh-surface' in response_data else None,
            response_data['pressure-surface'][i] if 'pressure-surface' in response_data else None
        ]
        writer.writerow(row)

print("Data saved to weather_data.csv")
