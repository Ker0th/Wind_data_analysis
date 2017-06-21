from Data_load import *
from Data_satistics import *
from Data_plot import *
from Menu import *
#defining requred start data
data = None
result = None
#Defining the different menus
menuItems = np.array([' Load data', ' Display statistics', ' Generate plots', ' Quit'])
statItems = np.array([' Mean', ' Variance', ' Cross correlation', ' Display the statistical matrix', ' Return to main menu'])
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
        except FileNotFoundError:
            print('\nError: wrong file name, please enter a valid filename\n')
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
                    print('\nYou will be needed to input some reference points, that is between 0 and the chosen dimension\n')
                    while True:
                        try:
                            Yref = int(input('\nPlease choose a reference for the y coordinate: '))
                            Zref = int(input('\nPlease choose a reference for the z coordinate: '))
                            DeltaX = int(input('\nPlease choose the separation in X: '))
                        except ValueError:
                                print('\nError: That is not a number, or an integer')
                        else:
                            #checks if the variables are in the required range
                            if not(Yref < Ny) or not(Zref < Nz) or not(DeltaX < Nx):
                                print('\nError: your values must be lower than the loaded data dimensions')
                                continue
                            elif Yref < 0 or Zref < 0 or DeltaX < 0:
                                print('\nError: The reference values must be a positive integer')
                                continue
                            result = dataStatistics(data, statistic, Yref, Zref, DeltaX)
                            # ask the user to give a coordinate set to display a value for
                            while True:
                                try:
                                    ycoord = int(input('\nPlease choose an y-coordinate: '))
                                    zcoord = int(input('\nPlease choose a z-coordinate: '))
                                except ValueError:
                                    print('\nError: That is not a number, or an integer')
                                else:
                                    # checks if the variables are in the required range
                                    if not (ycoord < Ny) or not (zcoord < Nz):
                                        print('\nError: Your coordinates must be lower than the loaded data dimensions')
                                        continue
                                    elif ycoord < 0 or zcoord < 0:
                                        print('\nError: The reference values must be a positive integer')
                                        continue
                                    print()
                                    print('the{0} is {1} for the point where the y-coordinate is: {2} and z-coordinate: {3}'.format(statistic,result[ycoord, zcoord],ycoord,zcoord))  # CHECK STRINGEN
                                    print()
                                    break
                            break

                #shows the full matrix for the statistic that have previously been calculated
                elif statistic == ' Display the statistical matrix':
                    if result is None:
                        print('\nError: no statistical data has been loaded\n')
                    else:
                        print()
                        print('the previous statistic as a matrix is {0}'.format(result))
                        print()
                #calclate the statistic the user wanted with default values for yref, zref and deltax
                else:
                    Yref = 0
                    Zref = 0
                    DeltaX = 0
                    result = dataStatistics(data, statistic, 0, 0, 0)

                    #ask the user to give a coordinate set to display a value for
                    while True:
                        try:
                            ycoord = int(input('\nPlease choose a y-coordinate: '))
                            zcoord = int(input('\nPlease choose a z-coordinate: '))
                        except ValueError:
                            print('\nError: That is not a number, or an integer')
                        else:
                            # checks if the variables are in the required range
                            if not(ycoord < Ny) or not(zcoord < Nz):
                                print('\nError: Your coordinates must be lower than the loaded data dimensions')
                                continue
                            elif ycoord < 0 or zcoord < 0:
                                print('\nError: The reference values must be a positive integer')
                                continue
                            print()
                            print('the{0} is {1} for the point where the y-coordinate is: {2} and z-coordinate: {3}'.format(statistic, result[ycoord,zcoord], ycoord, zcoord))  # CHECK STRINGEN
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
                    print('\nYou will be needed to input some reference points, that is between 0 and the chosen dimension\n')
                    while True:
                        try:
                            Yref = int(input('\nPlease choose a reference for the y coordinate: '))
                            Zref = int(input('\nPlease choose a reference for the z coordinate: '))
                            DeltaX = int(input('\nPlease choose the separation in X: '))
                        except ValueError:
                            print('\nError: That is not a number')
                        else:
                            #making sure the arguments are in valid ranges
                            if 0 < Yref > Ny or 0 < Zref > Nz or 0 < DeltaX > Nx:
                                print('\nError: your reference must be lower than the loaded data dimensions')
                                continue
                            elif Yref < 0 or Zref < 0 or DeltaX < 0:
                                print('\nError: The reference values must be a positive integer')
                                continue
                            result = dataStatistics(data, plotstatistic, Yref, Zref, DeltaX)
                            print()
                            print('Close the plot to continue')
                            print()
                            dataPlot(result, plotstatistic)
                            break
                # calclate the statistic the user wanted with default values for yref, zref and deltax
                else:
                    Yref = 0
                    Zref = 0
                    DeltaX = 0
                    #result = dataStatistics(data, plotstatistic, Yref, Zref, DeltaX)
                    result = dataStatistics(data, plotstatistic, Yref, Zref, DeltaX)
                    print()
                    print('Close the plot to continue')
                    print()
                    dataPlot(result, plotstatistic)

    #Closing the program
    elif choice == 4:
        print()
        print('Quitting the program')
        break