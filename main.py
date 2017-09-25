import numpy as np
from bradyTachyCardia import bradyTachyCardia
from write_output import write_output
from load_data import load_data
from HRinst import HRinst
from take_Average import average
from take_Average import get_interval

def main(filename,mins):
    """This file is the glue for our heart rate monitor software. It takes as input a file name for ECG data,
    it calculates the instantaneous and average heart rates and when brady- or tachycardia occur, and it writes this
    data to another file.
    :param filename: (str) name of the ECG file
    :param mins: (int) number of minutes used to calculate average hr
    :return: nothing
    """
    data = load_data(filename)
    HRinst_output = HRinst(data)
    HRavg_output = average(HRinst_output,mins)
    btc_output = bradyTachyCardia(HRinst_output)
    write_output(HRinst_output, HRavg_output, btc_output)

if __name__ == "__main__":
    main('Test_ECG.csv',2)