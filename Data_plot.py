import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Data_satistics import *
from Data_load import *
#result = np.zeros((1,1))
def dataPlot(data,plotstatistic, Yref, Zref, DeltaX):
    '''

    :param data:
    :param plotstatistic:
    :param Yref:
    :param Zref:
    :param DeltaX:
    :return:
    '''
    #Contourplot f statistic
    cs=plt.contourf(data)

    plt.colorbar(cs)
    plt.xlabel('zvalues')
    plt.ylabel('yvalues')
    plt.title('{0} Value of wind data in the X-direction or Y-Z plane'.format(plotstatistic))
    plt.show()

#dataPlot(dataLoad("test.bin",20,20,20),' Mean')


#dataStat=dataStatistic.datastatistic(data,'Mean')

