from load_data import load_data
import numpy as np


def get_interval(mat,mins):
    time = mat[:][0]
    hr = mat[:][1]
    secs = mins*60
    seglen = 0
    for a in range(len(time)):
        if time[a]>secs:
            seglen = a + 1
            break

    if seglen == 0:
        raise ValueError('not enough data for that long average')

    return seglen


def average(mat,mins):

    time = mat[:][0]
    hr = mat[:][1]
    secs = mins*60
    seglen = get_interval(mat,mins)
    print(seglen)
    averages = []
    for a in range(len(hr)):
        if a<seglen:
            averages.append('calculating')
        else:
            curAve = np.mean(hr[a-seglen:a])
            averages.append(curAve)

    return averages
