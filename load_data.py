import numpy as np


def load_data(file):

    if not file.endswith('.csv'):
        raise ValueError("file must be in .csv format")

    matrix = np.loadtxt(open(file), delimiter=",", skiprows=1)
    dims = np.shape(matrix)
    print(dims)
    if len(dims)!=2:
        raise ValueError("file must have two columns (time and voltage)")

    time = matrix[:,0]
    voltage = matrix[:,1]
    answer = (time,voltage)
    return answer

print(load_data('data.csv'))