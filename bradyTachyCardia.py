import numpy as np


def bradyTachyCardia(HRinst):
    """Determines when bradycardia or tachycardia occurred in the ECG trace
    :param HRinst: (ndarray)
    :returns: list of same length as HRinst that indicates when brady- or tachycardia occurred
    """

    bradyTachy = ['']*(np.size(HRinst))

    for i in range(len(HRinst)):
        if HRinst[i] <= 60:  # this indicates bradycardia, aka the heart is beating too slowly
            bradyTachy[i] = 'B'
        elif HRinst[i] >= 100:  # this indicates tachycardia, aka the heart is beating too quickly
            bradyTachy[i] = 'T'
        else:  # otherwise the heart is beating normally
            bradyTachy[i] = 'N'

    return bradyTachy
