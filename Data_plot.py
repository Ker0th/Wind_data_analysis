import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Data_satistics import *
from Data_load import *

def dataPlot(data,statistic):

    data=dataLoad("test.bin",170,170,170)
    result=dataStatistics(data,statistic,0,0,0)

#Contourplot f statistic
    cs=plt.contourf(result)

    plt.colorbar(cs)
    plt.xlabel('yvalues')
    plt.ylabel('zvalues')
    plt.title('{0} Value of wind data in the X-direction or Y-Z plane'.format(statistic))
    plt.show()

dataPlot(dataLoad("test.bin",20,20,20),' Mean')


#dataStat=dataStatistic.datastatistic(data,'Mean')

