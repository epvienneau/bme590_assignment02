This project acts as a heart rate monitor by analyzing ECG data and determining the instantaneous heart rate, the average heart rate over a user-specified interval, and when brady- or tachycardia occurred. To run it, call main(ecg_data.csv, mins), where ecg_data.csv is the ecg data and mins is the number of minutes over which the average heart rate should be calculated. ecg_data.csv must have a header of exactly one line, it must be comma separated, the first column must be time in seconds and the second column must be voltage in mV.
 Travis Badge: ![Alt Text](https://travis-ci.org/epvienneau/bme590_assignment02.svg?branch=master)
