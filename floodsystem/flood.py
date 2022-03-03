from .utils import sorted_by_key
def stations_level_over_threshold(stations, tol):
    '''
     Given a list of stations and a tolerance, this function returns a list of tuples, where each tuple holds a station (object) at which the latest relative water level is over tol and the relative water level at the station.
    '''
    output=[]
    for s in stations:
        if s.relative_water_level() is not None:
                if s.relative_water_level()>tol:
                    output.append((s,s.relative_water_level()))
    output1=sorted_by_key(output,1,reverse=True)
    return output1

def stations_highest_rel_level(stations, N):
    '''
    Given a list of stations and an integer, this function returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest.
    '''
    output=[]
    for s in stations:
        if s.relative_water_level() is not None:
            output.append((s,s.relative_water_level()))
    output=sorted_by_key(output,1,reverse=True)
    output1=[]
    if len(output)>N:
        for i in range(N):
            output1.append(output[i][0])
    return output1