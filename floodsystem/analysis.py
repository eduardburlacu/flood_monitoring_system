import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dat

def polyfit(dates, levels, p):
    # Convert dates to floats
    date = dat.date2num(dates)
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(date-date[0], levels, p)
    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    poly1 = poly(date - date[0])
    output = (poly1, date[0])
    return output

def average_gradient(dates, levels, p):
    # Convert dates to floats
    date = dat.date2num(dates)
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(date-date[0], levels, p)
    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    D = np.polyder(poly)
    der = D(date-date[0])
    total = 0
    for x in der:
        total += x
    average = total/len(date)
    return average