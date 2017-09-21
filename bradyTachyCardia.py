def bradyTachyCardia(inputData):
    """Determines when bradycardia or tachycardia occurred in the ECG trace
    :param HRinst: (ndarray)
    :returns: list of same length as HRinst that indicates when brady- or tachycardia occurred
    """

    HRinst = inputData[1]   #  only care about heart rates, not when they happened
    bradyTachy = []  #  make new list to hold characters indicating brady/tachycardia or normal HR
    for i in HRinst:
        if HRinst[i] == 0  # in this case, the heart hasn't beat yet so cannot determine state
            bradyTachy.append('--')
        elif HRinst[i] <= 60:  # this indicates bradycardia, aka the heart is beating too slowly
            bradyTachy.append('B')
        elif HRinst[i] >= 100:  # this indicates tachycardia, aka the heart is beating too quickly
            bradyTachy.append('T')
        else:  # otherwise the heart is beating normally
            bradyTachy.append('N')

    return bradyTachy
