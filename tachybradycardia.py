def bradycardia(hr, lowerthresh):

    """
    This module determines when in the ECG data there is bradycardia

    :param hr: (ndarray) heart rate- used to determine when
     bradycardia occurred in ECG trace
    :param lowerthresh: (int or double) lower threshold for determining
     bradycardia- user input or default 60 bpm
    :return: brady: (ndarray) 1 for bradycardia, 0 otherwise
    """

    import numpy as np
    brady = [0] * np.size(hr)
    for i in range(len(hr)):
        if hr[i] <= int(lowerthresh):  # this indicates bradycardia,
            #  aka the heart is beating too slowly
            brady[i] = 1
    return brady


def tachycardia(hr, upperthresh):

    """
    This module determines when in the ECG data there is tachycardia

    :param hr: (ndarray) heart rate-
     used to determine when tachycardia occurred in ECG trace
    :param upperthresh: (int or double) upper threshold for determining
     tachycardia- user input or default 100 bpm
    :return: tachy: (ndarray) 1 for tachycardia, 0 otherwise
    """

    import numpy as np
    tachy = [0] * np.size(hr)
    for i in range(len(hr)):
        if hr[i] >= int(upperthresh):  # this indicates tachycardia,
            #  aka the heart is beating too quickly
            tachy[i] = 1
    return tachy

