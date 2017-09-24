def write_output(time_HRinst, HRavg, btc):
    """Writes to text file time, instantaneous heart rate, average heart rate over user-specified interval, and when
    brady- or tachycardia occurred in the ECG trace
    :param time_HRinst: ndarray where first element is times and second element is instantaneous heart rates
    :param HRavg: list of average heart rates
    :param btc: list of characters to indicate patient status (-- means not enough data, T means tachycardia,
        B means bradycardia, and N means normal
    :returns: nothing"""

    file = open("assignment02_output.csv", "w+")
    header = "Time (s), Instantaneous Heart Rate, Average Heart Rate, Brady/Tachycardia Occurrence\n"
    file.write(header)
    for i, hr in enumerate(HRavg):
        row = str(time_HRinst[0][i]) + "," + str(time_HRinst[1][i]) + "," + str(HRavg[i]) + "," + btc[i] + "\n"
        file.write(row)
    file.close()