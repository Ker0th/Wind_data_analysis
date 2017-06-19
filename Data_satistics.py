import numpy as np
import pandas as pd

def dataStatistics(data, statistic, Yref, Zref, DeltaX):

    if statistic == " Mean":
        result = np.mean(data, axis = 0)

    elif statistic == " Variance":
        result = np.var(data, axis = 0)

    elif statistic == " Cross correlation":
        result = np.zeros((2,2))

    return result
