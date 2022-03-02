from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import  stations_level_over_threshold, stations_highest_rel_level
import random
def test_stations_level_over_threshold():
    stations=build_station_list()
    update_water_levels(stations)
    for i in range(10):
        tol=random.randint(0, 5)
        sth=stations_level_over_threshold(stations,tol)
        for element in sth:
            assert element[1]>=tol
        for i in range(len(sth)):
            if i!=0:
                assert sth[i-1][1]>=sth[i][1]
def test_stations_highest_rel_level():
    stations=build_station_list()
    update_water_levels(stations)
    risklist=stations_highest_rel_level(stations,100)
    for i in range(len(risklist)):
        if i != 0:
            assert risklist[i-1].relative_water_level() >= risklist[i].relative_water_level()
    assert(len(risklist))==100
