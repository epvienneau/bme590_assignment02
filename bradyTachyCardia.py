import numpy as np
import pandas as pd
from scipy.stats import threshold

dataset = pd.read_csv("ecg_data.csv")
dataset=dataset.values

def HRinst(dataset):
    """
    Takes the input data from an ndarray consisting of an array of time instances in the first column and
    an array of voltage values in the second column.
    :param dataset: tuple with two elements. First element is a
    :returns: ndarray of 2 columns. First column with time in s, second column with heart rate in BPM. Values in float
    """

    time = dataset[:, 0]
    voltage = dataset[:, 1]
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

def bradyTachyCardia(HRinst):
    """Determines when bradycardia or tachycardia occurred in the ECG trace
    :param HRinst: (ndarray)
    :returns: list of same length as HRinst that indicates when brady- or tachycardia occurred
    """

    bradyTachy = ['']*HRinst.size()
    for i in HRinst:
        if HRinst[i] <= 60:  # this indicates bradycardia, aka the heart is beating too slowly
            bradyTachy[i] = 'B'
        elif HRinst[i] >= 100:  # this indicates tachycardia, aka the heart is beating too quickly
            bradyTachy[i] = 'T'
        else:  # otherwise the heart is beating normally
            bradyTachy[i] = 'N'

    return bradyTachy
