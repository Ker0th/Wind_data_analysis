import numpy as np
def dataLoad(filename, Nx, Ny, Nz):
    '''

    :param filename: A string containing the filename of a data file
    :param Nx: Size of the first dimension of the 3-dimensional output array
    :param Ny: Size of the second dimension of the 3-dimensional output array
    :param Nz: Size of the third dimension of the 3-dimensional output array
    :return: A 3-dimensional array with size Nx x Ny x Nz
    '''
    try:
        data = np.fromfile(filename, dtype='f4', count = Nx*Ny*Nz)
        #reshapes the vector to a Nx x Ny x Nz 3-dimensional array with Nz cahnging the fastes
        data = data.reshape([Nx,Ny,Nz])
    except (ValueError,OverflowError):
        print("Value out of range.")
    return data
