from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
rivers.sort()
print(len(rivers), "rivers. First 10 - ", rivers[:10])

StaRiv = stations_by_river(stations)
output1 = []
for s in StaRiv["River Aire"]:
    output1.append(s)
output1.sort()
print(output1)
output2 = []
for s in StaRiv["River Cam"]:
    output2.append(s)
output2.sort()
print(output2)
output3 = []
for s in StaRiv["River Thames"]:
    output3.append(s)
output3.sort()
print(output3)