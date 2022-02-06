# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from haversine import haversine
from .utils import sorted_by_key  # noqa

def haversine2(p,q):
    y = pow(math.sin(0.5*(p[0]-q[0])), 2) + pow(math.sin(0.5*(p[0]-q[0])), 2)
    x = math.sqrt(y)
    d = 12756.2 * math.arcsin(x)


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
    '''
    Given a list of stations, this function returns a sorted list with all the rivers.
    '''
    rivers = []
    for s in stations:
        if s.river not in rivers:
            rivers.append(s.river)
    return rivers


def stations_by_river(stations):
    '''
    Given a list of stations, this function returns a dictionary that maps river names (key) to a list of station objects on a given river.
    '''
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


def rivers_by_station_number(stations, N):
    '''
    Given a list of stations, this function returns a list of (river name, number of stations) tuples, sorted by the number of stations.
    '''
    #Create a dictionary river: [all stations on that river in a list]
    dict=stations_by_river(stations)
    # lot is a list of tuples of (river,number of stations) sorted by #of stations
    lot=[]
    for key,value in dict.items():
        lot.append((key,len(value)))
    #The list (river,count of stations) is now sorted by the number(descending order).
    lot=sorted_by_key(lot,1,reverse=True)
    #Now we output first N counts(or more in case of equality for last place)
    answer=[]
    for i in range(N):
        answer.append(lot[i])
        if i==N-1:
            j=i+1
            while lot[j][1]==lot[i][1]:
                answer.append(lot[j])
                j+=1
    return answer