import numpy as np
from scipy import stats


def HRinst(dataset,secperunit=60):

    """
    Takes the input data of the time and voltage to convert it into an array with time and instantaneous heart rate.

    :param dataset: (tuple) Two elements, each a 1xN ndarray for time and voltage values respectively
    :param secperunit: (int or double) Conversion from unit of time ndarray to seconds
    :returns: (ndarray) 2 columns. First column with time in s, second column with heart rate in BPM.
        Each element in the ndarray is a float.
    """

    time = dataset[:][0]
    voltage = dataset[:][1]
    thresholded = stats.threshold(voltage, 0.5 * voltage.max())
    HRinst = np.zeros(len(thresholded))

    is_increasing = np.roll(thresholded, 1) <= thresholded
    will_decrease = np.roll(thresholded, -1) < thresholded
    is_maximum = is_increasing * will_decrease
    peakInd = np.asarray(np.where(is_maximum))

    for i,val in enumerate(thresholded):
        peaks=peakInd[peakInd<i]
        if i>peakInd[0][1]:
            HRinst[i] = secperunit/ (time[int(peaks[-1])] - time[int(peaks[-2])])
        else:
            HRinst[i]=0

    HRinst[-1]=HRinst[-2]
    HRinst=np.column_stack((time,HRinst))
    return HRinst