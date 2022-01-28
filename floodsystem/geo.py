# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from .utils import sorted_by_key  # noqa
def stations_by_distance(stations, p):
    '''
    Given a list of stations and coordinates p(tuple of lat,long), returns a list of tuples of station,distance sorted by distance.
    '''
    lt= []
    for station in stations:
        distance=haversine(p,station.coord)
        tup=(station,distance)
        lt.append(tup)
    lt=sorted_by_key(lt,1)
    return lt
def stations_within_radius(stations, centre, r):
    x=stations_by_distance(stations,centre)
    i=0
    while x[i][1]<=r: i+=1
    a=[x[j][0] for j in range(i)]
    return a
def rivers_with_station(stations):
    rivers = []
    for s in stations:
        if s.river not in rivers:
            rivers.append(s.river)
    return rivers
def stations_by_river(stations):
    rivers = rivers_with_station(stations)
    rivers.sort()
    #riverstations =
    riverdict = {}
    for r in rivers:
        riverdict[r] = []
        for s in stations:
            if r == s.river:
                riverdict[r].append(s.name)
    return riverdict
                

    #riverdict = dict.fromkeys(rivers, x)
