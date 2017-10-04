from load_data import load_data
import numpy as np


def get_interval(time,mins=1):

    """ Figures out how many points in mins minutes

    Gets the length in items in an array of each interval of the time that is inputed in minutes

    Args:
        time (ndarray): An array of times
        mins (int): Number of minutes to take HR over

    Returns:
        The length in data points of mins minutes
    """

    secs = mins*60
    seglen = 0
    for a in range(time.shape[0]):
        if time[a]>secs:
            seglen = a + 1
            break

    if seglen == 0:
        raise ValueError('not enough data for that long average')

    return seglen


def average(hr,time,mins=1):

    """ Takes a running average of HR data

    Takes a running average of HR data for a user inputted number of minutes

    Args:
        hr (ndarray): An array of heart rates
        mins (int): Number of minutes to take HR over

    Returns:
        An ndarray of average heart rate at each time point
    """

    seglen = get_interval(time,mins)
    averages = []
    for a, val in enumerate(hr):
        if a<seglen:
            averages.append('calculating')
        else:
            curAve = np.mean(hr[a-seglen:a])
            averages.append(curAve)

    return averages

if __name__ == "__main__":
    average('TestAve.csv',1)