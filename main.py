import numpy as np
from bradyTachyCardia import bradyTachyCardia
from write_output import write_output
from load_data import load_data
from HR_inst import HR_inst
from take_average import *

def main(filename):
    """This file is the glue for our heart rate monitor software. It takes as input a file name for ECG data,
    it calculates the instantaneous and average heart rates and when brady- or tachycardia occur, and it writes this 
    data to another file.
    :param filename: (str) name of the ECG file
    :return: nothing
    """
    data = load_data(filename)
    HRinst_output = HR_inst(data)
    HRavg_output = take_average(HRinst_output)
    btc_output = bradyTachyCardia(HRinst_output)
    write_output(HRinst_output, HRavg_output, btc_output)