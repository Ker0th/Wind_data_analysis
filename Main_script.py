from Data_load import *
from Data_satistics import *
from Data_plot import *
from Menu import *

menuItems = np.array([' Load data', ' Display statistics', ' Generate plots', ' Quit'])
while True:
    choice = displayMenu(menuItems)
    try:
        if choice == 1:
            filename = str(input('Please enter a filename: '))
            dataorigin = data = dataLoad(filename)
    except FileNotFoundError:
        print('\nwrong file type\n')
    else:
        if choice == 2:
            print('\nError: no data has been loaded\n')
        else:
            #run Statistic function
            statistic

