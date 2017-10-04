import numpy as np
from scipy import stats


def HRinst(dataset):

    """
    Takes the input data of the time and voltage to convert it into an array with time and instantaneous heart rate.
    :param: dataset: tuple of two elements. Each element is an ndarray (1xN).
    :param: dataset: tuple of two elements. Each element is an ndarray (1xN).
    :returns: ndarray of 2 columns. First column with time in s, second column with heart rate in BPM.
        Each element in the ndarray is a float.
    """

    time = dataset[:][0]
    voltage = dataset[:][1]
    thresholded = stats.threshold(voltage, 0.8 * voltage.max())
    peakInd = np.array([0])
    HRinst = np.zeros(len(thresholded))

    for i, val in range(1, len(thresholded) - 1):
        HRinst[i] = HRinst[i - 1]
        if thresholded[i] > thresholded[i - 1] and thresholded[i] >= thresholded[i + 1]:
            peakInd = np.append(peakInd, int(i))
            HRinst[i] = 60/ (time[int(peakInd[-1])] - time[int(peakInd[-2])])
    HRinst[-1]=HRinst[-2]
    HRinst=np.column_stack((time,HRinst))
    return HRinst
