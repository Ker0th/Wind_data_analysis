import numpy as np
def inputNumber(prompt, length):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('That is not even a number')
        else:
            if num not in range(1,length+1):
                print('that is not a valid option, try again')
                continue
            break
    return num
def displayMenu(options):
    #
    for i in range(len(options)):
        print('{:d}.{:s}'.format(i+1,options[i]))
        choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber('Please choose a menu item: ', len(options))
    return choice