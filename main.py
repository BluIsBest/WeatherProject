import gatheringInfo

nyStationList = ['44025', '44065', 'SDNH4', 'KPTN6', 'MHRN6', 'ROBN4', 'BATN6']

print(gatheringInfo.gatherWindSpeed(nyStationList))
print(gatheringInfo.gatherWindSpeed(nyStationList) ** 2)

SSI = (0.5 * ((gatheringInfo.gatherWindSpeed(nyStationList) / 60)**2) +
       0.3 * (930 / gatheringInfo.gatherPres(nyStationList)) +
       0.2 * (gatheringInfo.gatherWaveHeight(nyStationList)) / 12)

if SSI < 0.2:
    print("\nNote that some values are hard coded. Further research must be done to validate our prediction values")
    print("The expected storm should be a minimal storm")
if 0.21 < SSI < 0.4:
    print("\nNote that some values are hard coded. Further research must be done to validate our prediction values")
    print("The expected storm should be a moderate storm")
if 0.41 < SSI < 0.6:
    print("\nNote that some values are hard coded. Further research must be done to validate our prediction values")
    print("The expected storm should be a strong storm")
if 0.61 < SSI < 0.8:
    print("\nNote that some values are hard coded. Further research must be done to validate our prediction values")
    print("The expected storm should be a severe storm")
if 0.81 < SSI:
    print("\nNote that some values are hard coded. Further research must be done to validate our prediction values")
    print("The expected storm should be an extreme storm")

