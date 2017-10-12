def bradycardia(hrinst, lowerthresh):

    """
    :param hrinst: (ndarray) instantaneous heart rate- used to determine when bradycardia occurred in ECG trace
    :param lowerthresh: lower threshold for determining bradycardia- user input or default 60 bpm
    :return: brady: (ndarray) 1 for bradycardia, 0 otherwise
    """

    import numpy as np
    brady = np.where(hrinst <= lowerthresh, [1], [0])  # this indicates bradycardia- the heart is beating too slowly
    return brady


def tachycardia(hrinst, upperthresh):

    """
    :param hrinst: (ndarray) instantaneous heart rate- used to determine when tachycardia occurred in ECG trace
    :param upperthresh: upper threshold for determining tachycardia- user input or default 100 bpm
    :return: tachy: (ndarray) 1 for tachycardia, 0 otherwise
    """

    import numpy as np
    tachy = np.where(hrinst >= upperthresh, [1], [0])  # this indicates tachycardia- the heart is beating too quickly
    return tachy
