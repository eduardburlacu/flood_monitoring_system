import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
stations=build_station_list()
update_water_levels(stations)
stations=stations_highest_rel_level(stations,25)
i=0
while i<5:
    station=stations[i]
    dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=10))
    if dates==[] or levels==[]:
        stations.pop(i)
        continue
    plot_water_levels(station,dates,levels)
    i+=1