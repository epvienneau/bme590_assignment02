from load_data import load_data
from take_Average import average
from HRinst import HRinst
from bradyTachyCardia import bradyTachyCardia
from write_output import write_output

class ECG_Class(object):

    """This class treats a file containing ECG data as an object

    It has many associated methods that process and display this data"""

    def __init__(self):
        self.data = load_data(self)
        self.time = self.data[:][0]
        self.voltage = self.data[:][1]
        self.instHR = HRinst(self.data)

    def avg(self):
        return average(self.instHR,self.time,mins=1)

    def bradyTachy(self):
        return bradyTachyCardia(self.instHR)

    def output(self,mins=1,filename="assignment02_output.csv"):
        """ Creates a file containing the output of these functions

        Runs all of the functions and outputs into a file of the specified filename

        Args:
            mins (int): Number of minutes to take HR over
            filename (str): optional name of file if you don't want

        Returns:
            An ndarray of average heart rate at each time point
        """

        ave = average(self.instHR,self.time,mins)
        btc = bradyTachyCardia(self)
        return write_output(self.time, self.HRinst, ave, btc, filename)