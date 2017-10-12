def bradycardia(hrinst, lowerthresh):

    """
    :param hrinst: (ndarray) instantaneous heart rate- used to determine when bradycardia occurred in ECG trace
    :param lowerthresh: lower threshold for determining bradycardia- user input or default 60 bpm
    :return: brady: (ndarray) 1 for bradycardia, 0 otherwise
    """

    import numpy as np
    brady = [0] * np.size(hrinst)
    for i in range(len(hrinst)):
        if hrinst[i] <= lowerthresh:  # this indicates bradycardia, aka the heart is beating too slowly
            brady[i] = 1
    return brady


def tachycardia(hrinst, upperthresh):

    """
    :param hrinst: (ndarray) instantaneous heart rate- used to determine when tachycardia occurred in ECG trace
    :param upperthresh: upper threshold for determining tachycardia- user input or default 100 bpm
    :return: tachy: (ndarray) 1 for tachycardia, 0 otherwise
    """

    import numpy as np
    tachy = [0] * np.size(hrinst)
    for i in range(len(hrinst)):
        if hrinst[i] >= upperthresh:  # this indicates tachycardia, aka the heart is beating too quickly
            tachy[i] = 1
    return tachy