import numpy as np
import pandas as pd
from scipy.stats import threshold

dataset = pd.read_csv("ecg_data.csv")
dataset=dataset.values

def HRinst(dataset):
    """
    Takes the input data from an ndarray consisting of an array of time instances in the first column and
    an array of voltage values in the second column.
    :param raw_data: (2 column ndarray, type: int)
    :returns: ndarray of 2 columns. First column with time in s, second column with heart rate in BPM
    """

    time = dataset[:][0]
    voltage = dataset[:][1]
    thresholded = threshold(voltage, 0.8 * voltage.max())
    peakInd = np.array([0])
    HRinst = np.zeros(len(thresholded))
    for i in range(1, len(thresholded) - 1):
        HRinst[i] = HRinst[i - 1]
        if thresholded[i] > thresholded[i - 1] and thresholded[i] >= thresholded[i + 1]:
            peakInd = np.append(peakInd, int(i))
            HRinst[i] = 60/ (time[int(peakInd[-1])] - time[int(peakInd[-2])])
    HRinst=np.column_stack((time,HRinst))
    return HRinst
HRinst(dataset)