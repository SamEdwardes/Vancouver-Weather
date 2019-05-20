import pandas as pd
from dateutil import rrule
from datetime import datetime


# Call Environment Canada API
# Returns a dataframe of data
def getHourlyData(stationID, year, month):
    base_url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
    query_url = "format=csv&stationID={}&Year={}&Month={}&timeframe=1".format(stationID, year, month)
    api_endpoint = base_url + query_url
    return pd.read_csv(api_endpoint, skiprows=15)

# Download Vancouver weather data
stationID = 888
start_date = datetime.strptime('Jan2015', '%b%Y')
end_date = datetime.strptime('Dec2019', '%b%Y')

frames = []
for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
    df = getHourlyData(stationID, dt.year, dt.month)
    frames.append(df)

print("Vancouver data loaded.")
weather_data_vancouver = pd.concat(frames)
weather_data_vancouver['Date/Time'] = pd.to_datetime(weather_data_vancouver['Date/Time'])
weather_data_vancouver['Temp (°C)'] = pd.to_numeric(weather_data_vancouver['Temp (°C)'])
weather_data_vancouver['Station ID'] = stationID
weather_data_vancouver['Station Name'] = "VANCOUVER HARBOUR CS"

weather_data_vancouver.to_csv('data/888_hourly.csv')
print("Vancouver data exported to csv.")

# Download Toronto weather data
stationID = 48549
start_date = datetime.strptime('Jan2015', '%b%Y')
end_date = datetime.strptime('Dec2019', '%b%Y')

frames = []
for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
    df = getHourlyData(stationID, dt.year, dt.month)
    frames.append(df)

"Toronto data loaded"
weather_data_toronto = pd.concat(frames)
weather_data_toronto['Date/Time'] = pd.to_datetime(weather_data_toronto['Date/Time'])
weather_data_toronto['Temp (°C)'] = pd.to_numeric(weather_data_toronto['Temp (°C)'])
weather_data_toronto['Station ID'] = stationID
weather_data_toronto['Station Name'] = "TORONTO CITY CENTRE"

weather_data_toronto.to_csv('data/48549_hourly.csv')
print("Toronto data exported to csv.")