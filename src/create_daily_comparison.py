'''
The purpose of this script is to transform the raw data imported from the web so that each row represents one day,
and has a column for each stations measurements.
'''
import pandas as pd


# get data
df = pd.read_csv('data/daily_weather.csv')

# create an empty list to hold dataframes
df_list = []

# create a new df for each station
for station in df['Station Name'].unique():
    df_list.append(df[df['Station Name'] == station])

# create a new dataframe that contains all the dates
unique_dates = df['Date/Time'].unique()
df_comparison = pd.DataFrame({'Date/Time': unique_dates})

# TODO: create the left join
# join the station data to
for df in df_list:
    df_comparison = pd.concat([df_comparison, df[['Date/Time','Total Precip (mm)']]],
                              join='left',
                              keys='Date/Time')


print(df_comparison.head())





