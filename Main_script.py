from Data_load import *
from Data_satistics import *
from Data_plot import *
from Menu import *
#defining requred start data
data = None
result = np.zeros((1,1))

#Defining the different menus
menuItems = np.array([' Load data', ' Display statistics', ' Generate plots', ' Quit'])
statItems = np.array([' Mean', ' Variance', ' Cross correlation', ' Return to main menu'])
plotstatItems = np.array([' Mean', ' Variance', ' Cross correlation', ' Return to main menu'])
while True:
    choice = displayMenu(menuItems)
    if choice == 1:
        try:
            print()
            filename = str(input('Please enter a filename: '))
            print()
            Nx = int(input('Please enter a desired length of the x dimension: '))
            print()
            Ny = int(input('Please enter a desired length of the y dimension: '))
            print()
            Nz = int(input('Please enter a desired length of the z dimension: '))
            print()
            data = dataLoad(filename, Nx,Ny,Nz)
        except FileNotFoundError: #hopper tilbage til main menu
            print('\nError: wrong file name\n')
        except ValueError:
            print('\nError: Please input a valid whole number\n')

    elif choice == 2:
        if data is None:
            print('\nError: no data has been loaded\n')
        else:
            #run Statistic function
            print('\nPlease select a type of statistic\n')
            #data = dataorigin
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
                            Yref = int(input('\nWrite the wanted y referance: '))
                            Zref = int(input('\nWrite the wanted z referance: '))
                            DeltaX = int(input('\nWrite the wanted change in X: '))
                        except ValueError:
                                print('\nError: That is not a number, or an interger')
                        else:
                            #checks if the variables are in the required range
                            if Yref > Ny or Zref > Nz or DeltaX > Nx:
                                print('\nError: your refence must be lower than the loaded data dimensions')
                                continue
                            elif Yref < 0 or Zref < 0 or DeltaX < 0:
                                print('\nError: The reference values must be a positive interger')
                                continue
                            result = dataStatistics(data, statistic, Yref, Zref, DeltaX) #vi skal kunne vælge en specefik mean/varianse for y/z
                            print()
                            print('the{0} is'.format(statistic), result[ycoord, zcoord])  # CHECK STRINGEN
                            print()
                            break
                #calclate the statistic the user wanted with default values for yref, zref and deltax
                else:
                    Yref = 0
                    Zref = 0
                    DeltaX = 0
                    result = dataStatistics(data, statistic, 0, 0, 0)
                    print()
                    print('the uncut{0} is '.format(statistic), result)
                    print()

                    #ask the user to give a coordinate set to display a value for
                    while True:
                        try:
                            ycoord = int(input('\nGive me a damn y-coordinate: '))
                            zcoord = int(input('\nGive me a damn y-coordinate: '))
                        except ValueError:
                            print('\nError: That is not a number, or an interger')
                        else:
                            # checks if the variables are in the required range
                            if ycoord > Ny or zcoord > Nz:
                                print('\nError: Your coordinates must be lower than the loaded data dimensions')
                                continue
                            elif ycoord < 0 or zcoord < 0:
                                print('\nError: The reference values must be a positive interger')
                                continue
                            print()
                            print('the{0} is {1} in the y-coordinate: {2} and z-coordinate: {3}'.format(statistic, result[ycoord,zcoord], ycoord, zcoord))  # CHECK STRINGEN
                            print()
                            break

    #going to the menu for plotting
    elif choice == 3:
        if data is None:
            print('\nError: no data has been loaded\n')
        else:
            print('\nPlease select a type of statistic that you want to plot\n')
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
                            Yref = int(input('\nWrite the wanted y referance: '))
                            Zref = int(input('\nWrite the wanted z referance: '))
                            DeltaX = int(input('\nWrite the wanted change in X: '))
                        except ValueError:
                            print('\nError: That is not a number')
                        else:
                            #making sure the arguments are in valid ranges
                            if 0 < Yref > Ny or 0 < Zref > Nz or 0 < DeltaX > Nx:
                                print('\nError: your refence must be lower than the loaded data dimensions')
                                continue
                            elif Yref < 0 or Zref < 0 or DeltaX < 0:
                                print('\nError: The reference values must be a positive interger')
                                continue
                            result = dataStatistics(data, plotstatistic, Yref, Zref, DeltaX)
                            dataPlot(result, plotstatistic)
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
                    dataPlot(result, plotstatistic, Yref, Zref, DeltaX)

    #Closing the program
    elif choice == 4:
        print()
        print('Quitting the program')
        break

#testtest
