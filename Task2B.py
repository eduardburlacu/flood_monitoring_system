from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
stations=build_station_list()
update_water_levels(stations)
x=stations_level_over_threshold(stations,0.8)
for element in x:
    print(element[0].name,element[1])

