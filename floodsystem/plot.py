import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

def plot_water_levels(station,dates,levels):
    low=[station.typical_range[0]]*len(dates)
    up=[station.typical_range[1]]*len(dates)
    plt.plot(dates,levels,label='Water Levels')
    plt.plot(dates,low,label='Typical Low')
    plt.plot(dates, up, label='Typical High')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.legend()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    low=[station.typical_range[0]]*len(dates)
    up=[station.typical_range[1]]*len(dates)
    plt.plot(dates,levels,'.',label='Water Levels')
    POLY = polyfit(dates,levels,p)
    plt.plot(dates, POLY[0],label='Least Squares Fit')
    plt.plot(dates,low,label='Typical Low')
    plt.plot(dates, up, label='Typical High')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.legend()
    plt.show()