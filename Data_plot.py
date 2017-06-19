import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def dataPlot(data,statistic):

    data=dataLoad("turb.bin")

    if statistic == 'Mean':
        plt.contourf(data)
        plt.xlabel(y values)
        plt.ylabel(z values)
        plt.title(Plot plot)


dataStat=dataStatistic.datastatistic(data,'Mean')


    dataPlot('turb.bin',