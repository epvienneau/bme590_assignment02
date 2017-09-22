import numpy as np
from write_output import write_output
import pytest

def test_write_output():
    HRinst = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 80, 100, 90, 80, 75, 60, 65, 45, 40])
    HRavg = [0, 80, 90, 90, 85, 80, 70, 68, 57, 48]
    btc = ['--', 'B', 'N', 'N', 'T', 'T', 'N', 'B', 'B', 'N']
    write_output(HRinst, HRavg, btc)
    try:
        file = open("assignment02_output.csv", 'r')
    except IOError:
        print("File does not exist!")  # Am I using this correctly here? Does try except belong in a unit test?
    finally:
        file.close()
    # Assume at this point we've verified file exists somehow...
    data = np.loadtxt(open("assignment02_output.csv"), delimiter=",", skiprows=1)
    dims = np.shape(data)
    if dims[1] != 4:
        raise ValueError("File doesn't contain four columns!")
    assert data[0] == HRinst[0]
    assert data[1] == HRinst[1]
    assert data[2] == HRavg
    assert data[3] == btc