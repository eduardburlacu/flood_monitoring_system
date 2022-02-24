from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
stations=build_station_list()
update_water_levels(stations)
x=stations_highest_rel_level(stations,10)
for element in x:
    print(element.name,element.relative_water_level())