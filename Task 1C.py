from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
a=build_station_list()
x=stations_within_radius(a,(52.2053, 0.1218),10)
print(x)