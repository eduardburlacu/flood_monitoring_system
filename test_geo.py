from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, rivers_by_station_number
from haversine import haversine

def test_stations_by_distance():

    stations = build_station_list()
    ls = stations_by_distance(stations)
    for i in range(len(ls)-1):
        assert ls[i][1] < ls[i+1][1] # checks station's distance smaller than next one's.

def test_stations_within_radius():
    stations = build_station_list()
    ls = stations_within_radius(stations,(52.2053, 0.1218),11)
    for i in ls:
        distance=haversine((52.2053, 0.1218),i.coord)
        assert distance <= 11 # checks each station's distance and compares with radius

def test_rivers_with_station():
    stations = build_station_list()
    ls = rivers_with_station(stations)
    total = []
    for i in ls:
        assert i not in total # checks for duplicates
        total.append[i]
    assert sorted(total) == ls # checks if sorted

def test_rivers_by_station_number():
    stations = build_station_list()
    ls = rivers_by_station_number(stations)
    for i in ls:
        assert i[1] > 0 # checks station no. is greater than 0
    ls2 = ls.copy()
    ls2.sort(key = lambda x: x[1])
    assert ls2 == ls # checks if list is sorted by station number
