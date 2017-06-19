import numpy as np

def dataStatistics(data, statistic, Yref, Zref, DeltaX):

    if statistic == " Mean":
        result = np.mean(data, axis = 0)

    elif statistic == " Variance":
        result = np.var(data, axis = 0)

    elif statistic == " Cross correlation":
        Nx = data.shape[0]
        a = data[:, Nx - DeltaX]
        b = data[DeltaX:, Yref, Zref]
        result = (np.sum(np.multiply(a, b[:, np.newaxis, np.newaxis]), axis = 0)) / (Nx - DeltaX)

    return result
