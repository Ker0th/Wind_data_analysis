import numpy as np

def dataStatistics(data, statistic, Yref, Zref, DeltaX):
    '''

    :param data: An Nx x Ny x Nz array consisting of wind speed values
    :param statistic: This is a string specifying the statistic that should be calculated (Mean, Variance or Cross correlation)
    :param Yref: The reference y-coordinate, which is used only in the Cross correlation.
    :param Zref: The reference z-coordinate, which is used only in the Cross correlation.
    :param DeltaX: Seperation in the x-coordinate, for which the Cross correlation has to be evaluated
    :return: An Ny x Nz array containing the calculated statistic for each point in the y-z plane.
    '''


    if statistic == " Mean":
        result = np.mean(data, axis = 0)

    elif statistic == " Variance":
        result = np.var(data, axis = 0)

    elif statistic == " Cross correlation":

        # Defining Nx as a constant
        Nx = data.shape[0]

        # Creating two arrays to use in the calculation for the Cross correlation
        DVec = data[:, Nx - DeltaX]
        DrefVec = data[DeltaX:, Yref, Zref]
        result = (np.sum(np.multiply(DVec, DrefVec[:, np.newaxis, np.newaxis]), axis = 0)) / (Nx - DeltaX)

    return result