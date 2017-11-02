from .load_data import load_data
import numpy as np


def get_interval(time, secs=1):

    """  Figures out how many points in secs seconds
    :param time: (ndarray) An array of times
    :param secs: (int) Number of seconds to take HR over
    :returns: The length in data points of secs
    """

    seglen = 0
    for a in range(time.shape[0]):
        if time[a] > secs:
            seglen = a + 1
            break

    if seglen == 0:
        raise ValueError('not enough data for that long average')

    return seglen


def average(hr, time, secs=1):

    """ Takes a running average of HR data
    :param hr: (ndarray) An array of heart rates
    :param time: (ndarray) An array of time values
    :param secs: (int) Number of seconds to take HR over
    :returns: An ndarray of average heart rate at each time point
    """

    seglen = get_interval(time, secs)
    averages = []
    for a, val in enumerate(hr):
        if a < seglen:
            averages.append(0)
        else:
            cur_ave = np.mean(hr[a-seglen:a])
            averages.append(cur_ave)

    return averages


if __name__ == "__main__":
    average()
