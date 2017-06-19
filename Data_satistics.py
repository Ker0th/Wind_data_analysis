import numpy as np
import pandas as pd

def dataStatistics(data, statistic, Yref, Zref, DeltaX):

    if statistic == " Mean":
        result = np.mean(data,axis=0)

    if statistic == " Variance":
        result = np.zeros((2,2))

    if statistic == " Cross correlation":
        #asgkjnasg
        #askgjnadg
        result = np.zeros((2,2))

    return result
