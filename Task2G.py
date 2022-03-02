import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import average_gradient

stations=build_station_list()
update_water_levels(stations)
stations=stations_highest_rel_level(stations,25)

i=0
while i < len(stations):
    station=stations[i]
    dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=2))
    if dates==[] or levels==[] or station.latest_level == None or station.typical_range == None:
        stations.pop(i)
        continue
    gradient = average_gradient(dates,levels,4)
    relative = station.relative_water_level()
    rise = station.latest_level - station.typical_range[0]
    #print(station.name, gradient, relative, rise)
    if (relative > 4) and (rise > 3) and (gradient > 0.2):
        print("")
        print("Severe flood risk at", station.name)
        print("------------------------------------------------------------")
        print("Average rate of rising:", round(gradient,3), "meters per day     (> 0.2mpd)")
        print("Height above typical upper range:", round(rise,3), "meters   (> 3m)")
        print("Relative Water Level:", round(relative, 2), "                      (> 4)")
    elif (relative > 3) and (rise > 2) and (gradient > 0.1):
        print("")
        print("High flood risk at", station.name)
        print("------------------------------------------------------------")
        print("Average rate of rising:", round(gradient,3), "meters per day     (> 0.1mpd)")
        print("Height above typical upper range:", round(rise,3), "meters   (> 2m)")
        print("Relative Water Level:", round(relative, 2), "                      (> 3)")
    elif (relative > 1.8) and (rise > 1.5) and (gradient > 0.1):
        print("")
        print("Moderate flood risk at", station.name)
        print("------------------------------------------------------------")
        print("Average rate of rising:", round(gradient,3), "meters per day     (> 0.1mpd)")
        print("Height above typical upper range:", round(rise,3), "meters   (> 1.5m)")
        print("Relative Water Level:", round(relative, 2), "                      (> 2)")
    elif (relative > 1.2) and (rise > 0.8) and (gradient > 0):
        print("")
        print("Low flood risk at", station.name)
        print("------------------------------------------------------------")
        print("Average rate of rising:", round(gradient,3), "meters per day     (> 0mpd)")
        print("Height above typical upper range:", round(rise,3), "meters   (> 0.8m)")
        print("Relative Water Level:", round(relative, 2), "                      (> 1.2)")
    i+=1