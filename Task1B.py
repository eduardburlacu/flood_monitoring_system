from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


stations=build_station_list()
x=stations_by_distance(stations,(52.2053, 0.1218))
ans1=[]
ans2=[]
for i in range(10):
    ans1.append((x[i][0].name,x[i][0].town,x[i][1]))
    ans2.append((x[len(x)-i-1][0].name,x[len(x)-1-i][0].town,x[(len(x)-1-i)][1]))
print(ans1)
print(ans2)
