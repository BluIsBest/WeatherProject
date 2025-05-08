import gatheringInfo

nyStationList = ['44025', '44065', 'SDHN4', 'KPTN6', 'MHRN6', 'ROBN4', 'BATN6']

newYork = gatheringInfo.BB(nyStationList)

SSI = (0.5 * ((newYork.get_SSI_WSPD() / 60) ** 2) +
       0.3 * (930 / newYork.get_SSI_PRES()) +
       0.2 * (newYork.get_SSI_WVHT()) / 12)

if SSI < 0.2:
    print("The expected storm should be a minimal storm")
if 0.21 < SSI < 0.4:
    print("The expected storm should be a moderate storm")
if 0.41 < SSI < 0.6:
    print("The expected storm should be a strong storm")
if 0.61 < SSI < 0.8:
    print("The expected storm should be a severe storm")
if 0.81 < SSI:
    print("The expected storm should be an extreme storm")

