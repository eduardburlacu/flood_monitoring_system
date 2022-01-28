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

