import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation
def plot_water_levels(station,dates,levels):
    low=[station.typical_range[0]]*len(dates)
    up=[station.typical_range[1]]*len(dates)
    plt.plot(dates,levels)
    plt.plot(dates,low,label='Typical Low')
    plt.plot(dates, up, label='Typical High')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()