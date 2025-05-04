from ndbc_api import NdbcApi
import datetime
import pandas as pd
import math

# Initialize the NDBC API so we can gather information from buoys
api = NdbcApi()

# The NDBC uses the UTC time as its standard, so we use this to be able to grab the most recent data.
# Initially this is set to gather readings from within 1 hour
utc_now = datetime.datetime.now(tz=datetime.UTC)
given_endTime = utc_now.strftime("%Y-%m-%d %H:%M")
start = utc_now - datetime.timedelta(hours=1)
given_startTime = start.strftime("%Y-%m-%d %H:%M")


# Formatting for debugging & testing
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
# ______________________________________________________________________________________

'''
            print(lastFive.iloc[0:3, 3])
            ^ Prints the first 3 values for WSPD. As long as it below lastFive.reset_index() its sorted by recent

            print(lastFive)
            ^ Prints dataframe, sorted like above, but includes everything

            NaN/nan is what will show in empty value spaces. Use math.isnan(value) to check for if nan. ITS A FLOAT!!
            
            WSPD == 3
            WVHT == 5
            PRES == 10
'''


# This class will hold one location per object, and within that its respective closest Buoys.
class BB:
    # First the class initialization is overwritten and will throw an error if no list is given
    def __init__(self, id_list):
        self.__id_list = id_list

    def get_station_ID_list(self):
        return self.__id_list

# This function will get the average Wind Speed from the locations buoy list, and will be returned to the user
    def get_SSI_WSPD(self):
        # Set initial counting variable to determine which Buoys are giving the information we are searching for
        WSPD_counter = 0
        sum_of_WSPD = 0.0
        # Iterate through the list of buoys provided
        for buoy in self.__id_list:
            # For tracking purposes
            print(buoy)
            # API Call for {buoy} in station list
            BuoyWspd = api.get_data(
                station_id=buoy,
                mode='stdmet',
                start_time=given_startTime,
                end_time=given_endTime,
                as_df=True
            )
            # For tracking progress
            print(f"Finished API call for buoy: {buoy}")

            # Flip resulting Dataframe (using pandas) to see 5 most recent results
            lastFive = pd.DataFrame(BuoyWspd)
            lastFive = lastFive.tail()

            # Remove Multi Indexing so we can sort by timestamp
            lastFive = lastFive.reset_index()
            lastFive = lastFive.sort_values(by='timestamp', ascending=False)

            # Check if the stations most recent readings have been submitted, else grab the next furthest back, or if
            #       not within 3 spaces, skip this buoys reading. If read properly, increment the WSPD_counter += 1
            lastFive = lastFive.iloc[0:3, 3]
            WSPD_values = lastFive.tolist()
            # Iterate through the WSPD_values list
            for value in WSPD_values:
                # If the value is not a nan value (its usually regarded as a float and will break calculations)
                if not math.isnan(value):
                    sum_of_WSPD += value
                    WSPD_counter += 1
                    break
                else:
                    # Pass if it is a nan
                    pass

        return sum_of_WSPD / WSPD_counter

    def get_SSI_WVHT(self):
        # Set initial counting variable to determine which Buoys are giving the information we are searching for
        WVHT_counter = 0
        sum_of_WVHT = 0.0
        # Iterate through the list of buoys provided
        for buoy in self.__id_list:
            # For tracking purposes
            print(buoy)
            # API Call for {buoy} in station list
            BuoyWvht = api.get_data(
                station_id=buoy,
                mode='stdmet',
                start_time=given_startTime,
                end_time=given_endTime,
                as_df=True
            )
            # For tracking progress
            print(f"Finished API call for buoy: {buoy}")

            # Flip resulting Dataframe (using pandas) to see 5 most recent results
            lastFive = pd.DataFrame(BuoyWvht)
            lastFive = lastFive.tail()

            # Remove Multi Indexing so we can sort by timestamp
            lastFive = lastFive.reset_index()
            lastFive = lastFive.sort_values(by='timestamp', ascending=False)

            # Check if the stations most recent readings have been submitted, else grab the next furthest back, or if
            #       not within 3 spaces, skip this buoys reading. If read properly, increment the WVHT_counter += 1
            lastFive = lastFive.iloc[0:3, 5]
            WVHT_values = lastFive.tolist()
            # Iterate through the WVHT_values list
            for value in WVHT_values:
                # If the value is not a nan value (its usually regarded as a float and will break calculations)
                if not math.isnan(value):
                    sum_of_WVHT += value
                    WVHT_counter += 1
                    break
                else:
                    # Pass if it is a nan
                    pass

        return sum_of_WVHT / WVHT_counter

    def get_SSI_PRES(self):
        # Set initial counting variable to determine which Buoys are giving the information we are searching for
        PRES_counter = 0
        sum_of_PRES = 0.0
        # Iterate through the list of buoys provided
        for buoy in self.__id_list:
            # For tracking purposes
            print(buoy)
            # API Call for {buoy} in station list
            BuoyPres = api.get_data(
                station_id=buoy,
                mode='stdmet',
                start_time=given_startTime,
                end_time=given_endTime,
                as_df=True
            )
            # For tracking progress
            print(f"Finished API call for buoy: {buoy}")

            # Flip resulting Dataframe (using pandas) to see 5 most recent results
            lastFive = pd.DataFrame(BuoyPres)
            lastFive = lastFive.tail()

            # Remove Multi Indexing so we can sort by timestamp
            lastFive = lastFive.reset_index()
            lastFive = lastFive.sort_values(by='timestamp', ascending=False)

            # Check if the stations most recent readings have been submitted, else grab the next furthest back, or if
            #       not within 3 spaces, skip this buoys reading. If read properly, increment the PRES_counter += 1
            lastFive = lastFive.iloc[0:3, 9]

            PRES_values = lastFive.tolist()
            # Iterate through the PRES_values list
            for value in PRES_values:
                # If the value is not a nan value (its usually regarded as a float and will break calculations)
                if not math.isnan(value):
                    sum_of_PRES += value
                    PRES_counter += 1
                    break
                else:
                    # Pass if it is a nan
                    pass

        # Now we gather the final WSPD Average and return it
        return sum_of_PRES / PRES_counter

    def get_SSI_PRES(self):
        # Set initial counting variable to determine which Buoys are giving the information we are searching for
        PRES_counter = 0
        sum_of_PRES = 0.0
        # Iterate through the list of buoys provided
        for buoy in self.__id_list:
            # For tracking purposes
            print(buoy)
            # API Call for {buoy} in station list
            BuoyPres = api.get_data(
                station_id=buoy,
                mode='stdmet',
                start_time=given_startTime,
                end_time=given_endTime,
                as_df=True
            )
            # For tracking progress
            print(f"Finished API call for buoy: {buoy}")

            # Flip resulting Dataframe (using pandas) to see 5 most recent results
            lastFive = BuoyPres.tail()

            # Remove Multi Indexing so we can sort by timestamp
            lastFive = lastFive.reset_index()
            lastFive = lastFive.sort_values(by='timestamp', ascending=False)

            # Check if the stations most recent readings have been submitted, else grab the next furthest back, or if
            #       not within 3 spaces, skip this buoys reading. If read properly, increment the PRES_counter += 1
            lastFive = lastFive.iloc[0:3, 9]

            PRES_values = lastFive.tolist()
            # Iterate through the PRES_values list
            for value in PRES_values:
                # If the value is not a nan value (its usually regarded as a float and will break calculations)
                if not math.isnan(value):
                    sum_of_PRES += value
                    PRES_counter += 1
                    break
                else:
                    # Pass if it is a nan
                    pass

        # Now we gather the final WSPD Average and return it
        return sum_of_PRES / PRES_counter


# In order to pull information about each individual buoy, we define another class that will use the API to gather the
#       individual information about hte buoy sucha as WSPD, WVHT, PRES, but also the location (longitude, latitude)
#       and the nearest town to said buoy ==> EX: station_id 44025 is 30 NM south of Islip, NY
class Buoy:
    def __init__(self, id):
        # First we set the ID to the member variable, and call for the information from the NDBC_API
        self.__id = id
        buoy = api.get_data(station_id=id,
                            mode='stdmet',
                            start_time=given_startTime,
                            end_time=given_endTime,
                            as_df=True)
        # Similar to the BB class, we call the most recent entries and sort them
        lastFive = buoy.tail().reset_index()
        lastFive = lastFive.sort_values(by='timestamp', ascending=False)
        # We set individual lists of the 3 most recent entries (~30 minutes of reporting) in order to still give a value
        #       in case a buoy does not report (some reports are hourly, on a 30-minute mark, etc.)
        WSPD_val = lastFive.iloc[0:3, 3].tolist()
        WVHT_val = lastFive.iloc[0:3, 5].tolist()
        PRES_val = lastFive.iloc[0:3, 9].tolist()

        # We then check through each of these lists for a non-NaN answer and save it to the self.__VARIABLE
        for value in WSPD_val:
            if not math.isnan(value):
                self.__WSPD = value
                break
            else:
                pass

        for value in WVHT_val:
            if not math.isnan(value):
                self.__WVHT = value
                break
            else:
                pass

        for value in PRES_val:
            if not math.isnan(value):
                self.__PRES = value
                break
            else:
                pass

        # We then call the station information to gather info such as Latitude and Longitude, and the Name
        lastFive = api.station(station_id=id, as_df=True)
        self.__NAME = "".join(str(lastFive.loc['Name'].tolist()))
        self.__LOC = "".join(str(lastFive.loc['Location'].tolist()))

    # Define the getter functions to get the needed information from individual buoys
    def getWSPD(self):
        return self.__WSPD

    def getWVHT(self):
        return self.__WVHT

    def getPRES(self):
        return self.__PRES

    def getNAME(self):
        return self.__NAME

            
# We now define the radial search function to search for stations in a new location, defined by the user
def Add_New_Location(lat, long):
    # First we define a int variable to track how many stations we need (7 is a good number)
    num = 0
    # Then an empty list to store the station_ids for our eventual BB object definition
    location_station_list = []
    
    # Use the ANDBC_API raidal search feature to grab the nearest stations and allow us to quickly find the station name
    station_list = api.radial_search(lat=lat, lon=long, radius=350, units='km').iloc[0:10]
    station_list = station_list.reset_index()
    
    for _, row in station_list.iterrows():
        if row['Includes Meteorology'] is True and num < 8:
            # If the station gives meteorology data then we add it to the list of stations to use, otherwise goto next
            location_station_list.append(row['Station'])
            num += 1
        else:
            pass

# Finally we check if the station id list is empty, if it isn't we return the new object to be saved
#          Otherwise we raise an error and pass
    if location_station_list != None:
        newLoc = BB(location_station_list)
        return newLoc
    else:
        pass


    def getLOC(self):
        return self.__LOC

