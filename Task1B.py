from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
stations=build_station_list()
x=stations_by_distance(stations,(52.2053, 0.1218))
ans=[]
for i in range(10):
    ans.append((x[i][0].name,x[i][0].town,x[i][1]))
print(ans)