import numpy as np

def load_data(file):
    """ gets the length in items in an array of each interval of the time that is inputed in minutes
    :param file: (.csv file)
    :returns: a tuple of length 2 where the first element is an array of time in seconds and the second an array
     of voltages in mV
    """

    if not file.endswith('.csv'):
        raise ValueError("file must be in .csv format")

    matrix = np.loadtxt(open(file), delimiter=",", skiprows=1)
    dims = np.shape(matrix)

    if len(dims)<2 or dims[1]!=2:
        raise ValueError("file must have two columns (time and voltage)")

    return matrix


if __name__ == "__main__":
    load_data('ECGTest.csv')

