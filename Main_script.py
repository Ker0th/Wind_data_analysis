from Data_load import *
from Data_satistics import *
from Data_plot import *
from Menu import *
dataorigin = np.zeros(((1,1,1)))
data = np.zeros(((1,1,1)))
result = np.zeros((1,1))
menuItems = np.array([' Load data', ' Display statistics', ' Generate plots', ' Quit'])
while True:
    choice = displayMenu(menuItems)
    try:
        if choice == 1:
            print()
            filename = str(input('Please enter a filename: '))
            print()
            Nx = int(input('Please enter a desired length of the x dimension: '))
            print()
            Ny = int(input('Please enter a desired length of the y dimension: '))
            print()
            Nz = int(input('Please enter a desired length of the z dimension: '))
            print()
            dataorigin = data = dataLoad(filename, Nx,Ny,Nz)
    except FileNotFoundError:
        print('\nError: wrong file name\n')
    except ValueError:
        print('\nError: Please input a valid whole number\n')
    else:
        if choice == 2:
            if data.any() == 0:
                print('\nError: no data has been loaded\n')
            else:
                #run Statistic function
                statItems = np.array([' Mean', ' Variance', ' Cross correlation', ' Return to main menu'])
                print('\nPlease select a type of statistic\n')
                data = dataorigin
                while True:
                    stat = displayMenu(statItems)
                    statistic = statItems[stat - 1]
                    #checks if the user want to quit the menu
                    if statistic == ' Return to main menu':
                        print()
                        break
                    #checks if the user wants to use cross correlation statistic and ask the user to input the required values
                    elif statistic == ' Cross correlation':
                        while True:
                            try:
                                Yref = float(input('\nWrite the wanted y referance: '))
                                Zref = float(input('\nWrite the wanted z referance: '))
                                DeltaX = float(input('\nWrite the wanted change in X: '))
                            except ValueError:
                                    print('Error: That is not a number')
                            else:
                                result = dataStatistics(data, statistic, Yref, Zref, DeltaX)
                                print()
                                print('the{0} is'.format(statistic), result)
                                print()
                                break
                    #calclate the statistic the user wanted with default values for yref, zref and deltax
                    else:
                        Yref = 0
                        Zref = 0
                        DeltaX = 0
                        result = dataStatistics(data, statistic,Yref, Zref, DeltaX)
                        print()
                        print('the{0} is '.format(statistic), result)
                        print()
        elif choice == 3:
            if data.any() == 0:
                print('\nError: no data has been loaded\n')
            else:
                plotstatItems = np.array([' Mean', ' Variance', ' Cross correlation', ' Return to main menu'])
                print('\nPlease select a type of statistic\n')
                #data = dataorigin
                while True:
                    stat = displayMenu(plotstatItems)
                    plotstatistic = plotstatItems[stat - 1]
                    if plotstatistic == ' Return to main menu':
                        print()
                        break
                    #checks if the user wants to use cross correlation statistic and ask the user to input the required values
                    elif plotstatistic == ' Cross correlation':
                        while True:
                            try:
                                Yref = float(input('\nWrite the wanted y referance: '))
                                Zref = float(input('\nWrite the wanted z referance: '))
                                DeltaX = float(input('\nWrite the wanted change in X: '))
                            except ValueError:
                                print('Error: That is not a number')
                            else:
                                result = dataStatistics(data, plotstatistic, Yref, Zref, DeltaX)
                                dataPlot(result, plotstatistic, Yref, Zref, DeltaX)
                                print()
                                print('Close plots to continue')
                                print()
                                break
                    # calclate the statistic the user wanted with default values for yref, zref and deltax
                    else:
                        Yref = 0
                        Zref = 0
                        DeltaX = 0
                        #result = dataStatistics(data, plotstatistic, Yref, Zref, DeltaX)
                        result = dataStatistics(data, plotstatistic, Yref, Zref, DeltaX)
                        print()
                        print('Close plots to continue')
                        print()
                        print(result)
                        dataPlot(result, plotstatistic, Yref, Zref, DeltaX)
                        break
        elif choice == 4:
            print()
            print('Quitting the program')
            break

#testtest
