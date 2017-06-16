import numpy as np
from pandas import DataFrame

dt = np.zeros(3)
def dataLoad(filename):
    names = 'Nx', 'Ny', 'Nz'

    # note that the offsets are larger than the size of the type because of
    # struct padding
    offsets = 8, 4, 0
    formats = 'f4', 'f4', 'f4'
    dt = np.dtype({'names': names, 'offsets': offsets, 'formats': formats},align=True)
    data = DataFrame(np.fromfile(filename, dt))
    data = np.matrix(data)
    print(dt)
    return data
print(dataLoad('test.bin'))