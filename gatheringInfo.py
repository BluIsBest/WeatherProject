from ndbc_api import NdbcApi
import datetime

api = NdbcApi()


def gatherWindSpeed(BuoyList):
    utc_now = datetime.datetime.now(tz=datetime.UTC)
    formatted_endTime = utc_now.strftime("%Y-%m-%d")
    unformatted_startTime = utc_now - datetime.timedelta(days=1)
    formatted_startTime = unformatted_startTime.strftime("%Y-%m-%d")
    List = []
    avgWindSpeed = 0.0
    for buoy in BuoyList:
        buoyWind = api.get_data(
            station_id=buoy,
            mode='stdmet',
            start_time=formatted_startTime,
            end_time=formatted_endTime,
            as_df=True
        )

        try:
            subsetWindOnly = buoyWind.iloc[0:3, 1]
            avgWindSpeed += buoyWind.iloc[0:3, 1].sum()
            List.append(subsetWindOnly)

        except KeyError as e:
            print(f"Warning. {e}")
            continue
        except AttributeError as a:
            print(f"Warning. {a}")
            continue

    print(f"Average Wind speed for stations {BuoyList}: {avgWindSpeed / 15}")
    return avgWindSpeed / 15


def gatherPres(BuoyList):
    utc_now = datetime.datetime.now(tz=datetime.UTC)
    formatted_endTime = utc_now.strftime("%Y-%m-%d")
    unformatted_startTime = utc_now - datetime.timedelta(days=1)
    formatted_startTime = unformatted_startTime.strftime("%Y-%m-%d")
    avgPres = 0.0
    List = []
    for buoy in BuoyList:
        buoyPres = api.get_data(
            station_id=buoy,
            mode='stdmet',
            start_time=formatted_startTime,
            end_time=formatted_endTime,
            as_df=True
        )

        try:
            subsetPresOnly = buoyPres.iloc[0:3, 7]
            avgPres += buoyPres.iloc[0:3, 7].sum()
            List.append(subsetPresOnly)

        except KeyError as e:
            print(f"Warning. {e}")
            continue
        except AttributeError as a:
            print(f"Warning. {a}")
            continue

    print(f"Average Pressure for stations {BuoyList}: {avgPres / 15}")
    return avgPres / 15


def gatherWaveHeight(BuoyList):
    utc_now = datetime.datetime.now(tz=datetime.UTC)
    formatted_endTime = utc_now.strftime("%Y-%m-%d")
    unformatted_startTime = utc_now - datetime.timedelta(days=1)
    formatted_startTime = unformatted_startTime.strftime("%Y-%m-%d")
    avgWave = 0.0
    List = []
    print(BuoyList)
    for buoy in BuoyList:
        buoyWave = api.get_data(
            station_id=buoy,
            mode='stdmet',
            start_time=formatted_startTime,
            end_time=formatted_endTime,
            as_df=True
        )

        try:
            subsetWaveOnly = buoyWave.iloc[0:3, 3]
            avgWave += buoyWave.iloc[0:3, 3].sum()
            List.append(subsetWaveOnly)

        except KeyError as e:
            print(f"Warning. {e}")
            continue
        except AttributeError as a:
            print(f"Warning. {a}")
            continue

        return avgWave / 2


nyStationList = ['44025', '44065', 'SDNH4', 'KPTN6', 'MHRN6', 'ROBN4', 'BATN6']


print(gatherWaveHeight(nyStationList))
