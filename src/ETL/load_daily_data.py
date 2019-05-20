import pandas as pd


def get_daily_data(stationIDs=[51442], years=[2018, 2019]):

    # fixed API variables
    timeframe = 2  # 1 (hourly); 2 (daily)
    month = 1
    day = 1

    # create an empty list to hold the dataframes, each year will have its own dataframe
    df_list = []

    for stationID in stationIDs:

        for year in years:

            # create API call
            base_url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&"
            api_details = f"stationID={stationID}&Year={year}&Month={month}&Day={day}&timeframe={timeframe}"
            url = base_url + api_details

            # read in first column only, we will use these to determine how many rows to skip
            df_one_col = pd.read_csv(url, usecols=[0], skip_blank_lines=False)

            # the first row of the dataframe starts with 'Date/Time', get the index location
            rows_to_skip = df_one_col['Station Name'][df_one_col['Station Name'] == 'Date/Time'].index.values[0] + 1

            # read data from website
            df = pd.read_csv(url, skiprows=rows_to_skip)

            # read dataframe details
            df_details = pd.read_csv(url, nrows=7)

            # add details
            df['Station Name'] = df_details.columns.values[1]
            df['Province'] = df_details.iloc[:, 1][0]
            df['Current Station Operator'] = df_details.iloc[:, 1][1]
            df['Latitude'] = df_details.iloc[:, 1][2]
            df['Longitude'] = df_details.iloc[:, 1][3]
            df['Elevation'] = df_details.iloc[:, 1][4]
            df['Climate Identifier'] = df_details.iloc[:, 1][5]
            df['WMO Identifier'] = df_details.iloc[:, 1][6]

            # append df to list
            df_list.append(df)

    # union all df together
    return (pd.concat(df_list))


# get data
df_weather = get_daily_data(stationIDs=[51442, 51459], years=[2015, 2016, 2017, 2018, 2019])
df_weather.to_csv('data/daily_weather.csv')

