class ECG_Class(object):
    """This class treats a file containing ECG data as an object

    It has many associated methods that process and display this data

    :type user_input: either string filename or the data itself
    :param user_input: the name of the csv file with the ECG data or the data itself

    :type avemins: double or int
    :param avemins: number of minutes to compute the average heart rate

    :type out_name: string
    :param out_name: name of output file

    :type lower_thresh: double or int
    :param lower_thresh: lower threshold for bradycardia

    :type upper_thresh: double or int
    :param upper_thresh: upper threshold for tachycardia
    """

    def __init__(self, user_input, avemins=1, out_name="_output.txt",
                 lower_thresh=60, upper_thresh=100):
        """
        Creates the variables associated with the class

        """
        from load_data import load_data
        from HRinst import HRinst
        if type(user_input) == str:
            self.name = user_input[:-4]
        else:
            self.name = 'InputData'
        self.mins = avemins
        self.bradyT = lower_thresh
        self.tachyT = upper_thresh
        if type(user_input) == str:
            self.data = load_data(user_input)
        else:
            self.data = user_input
        self.time = self.data[:][0]
        self.voltage = self.data[:][1]
        self.instHR = HRinst(self.data)
        self.avgHR = self.avg()

        if out_name == "_output.txt":
            self.outputfile = self.name + out_name
        elif out_name[-4:] == '.txt':
            self.outputfile = out_name
        else:
            self.outputfile = out_name + '.txt'

    def avg(self):
        """
        :type: tuple
        :return: average heart rate
        """
        from take_average import average

        return average(self.instHR, self.time, self.mins)

    def brady(self, hr_type='inst'):
        from tachybradycardia import bradycardia
        if hr_type == 'inst':
            brady = bradycardia(self.instHR, self.bradyT)
        else:
            brady = bradycardia(self.avgHR, self.bradyT)
        return brady

    def tachy(self, hr_type='inst'):
        from tachybradycardia import tachycardia
        if hr_type == 'inst':
            tachy = tachycardia(self.instHR, self.tachyT)
        else:
            tachy = tachycardia(self.avgHR, self.tachyT)
        return tachy

    def output(self):
        """ Creates a file containing the output of these functions
        """

        from write_output import write_output

        ave = self.avg()
        b = self.brady()
        t = self.tachy()

        return write_output(self.time, self.instHR, ave, b, t, self.outputfile)
