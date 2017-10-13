class ECG_Class(object):

    """This class treats a file containing ECG data as an object

    It has many associated methods that process and display this data
    """

    def __init__(self, filename, avemins=1,outName="None",lowerThresh=60,upperThresh=100):
        '''
        Creates the variables associated with the class

        :type filename: string
        :param filename: the name of the csv file with the ECG data

        :type avemins: double or int
        :param avemins: number of minutes to compute the average heart rate

        :type outName: string
        :param outName: name of output file

        :type lowerThresh: double or int
        :param lowerThresh: lower threshold for bradycardia

        :type upperThresh: double or int
        :param upperThresh: upper threshold for tachycardia
        '''
        from load_data import load_data
        from HRinst import HRinst
        self.name = filename[:-4]
        self.mins = avemins
        if outName=="None":
            self.outputfile = self.name + '_output.txt'
        else:
            self.outputfile = outName
        self.bradyT = lowerThresh
        self.tachyT = upperThresh
        self.data = load_data(self.name)
        self.time = self.data[:][0]
        self.voltage = self.data[:][1]
        self.instHR = HRinst(self.data)

    def avg(self):
        '''
        :type return: tuple
        :return: average heart rate (
        '''
        from take_average import average

        return average(self.instHR,self.time,self.mins)

    def btc(self):
        from bradyTachyCardia import bradyTachyCardia

        return bradyTachyCardia(self.instHR,self.bradyT,self.tachyT)

    def output(self):
        """ Creates a file containing the output of these functions

        Runs all of the functions and outputs into a file of the specified filename

        Args:
            mins (int): Number of minutes to take HR over
            filename (str): optional name of file if you don't want

        Returns:
            An ndarray of average heart rate at each time point
        """

        from write_output import write_output

        ave = self.avg()
        btc = self.btc()
        return write_output(self.time, self.HRinst, ave, btc, self.outputfile)

