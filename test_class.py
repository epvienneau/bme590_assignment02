import ECG_Class
from take_average import average
from HRinst import HRinst
from bradyTachyCardia import bradycardia
from bradyTachyCardia import tachycardia
from write_output import write_output


def test_unpack():
    obj1 = ECG_Class('testclass.csv')
    assert obj1.name == 'testclass'
    assert len(obj1.time) == len(obj1.data)
    assert len(obj1.voltage) == len(obj1.data)
    assert type(obj1.data) == 'ndarray'


def test_defaults():
    obj1 = ECG_Class('testclass.csv')
    assert obj1.mins == 1
    assert obj1.outname == "assignment02"
    assert obj1.bradyT == 60
    assert obj1.tachyT == 100


def test_average():
    obj2 = ECG_Class('testclass.csv',avemins=2)
    assert obj2.mins == 2
    assert obj2.avg() == average(obj2.time,obj2.voltage)

def test_btc():
    obj2 = ECG_Class('testclass.csv')
    obj3 = ECG_Class('testclass.csv',lowerThresh=50,upperThresh=110)
    assert obj2.bradyT == 60
    assert obj2.tachyT == 100
    assert obj3.bradyT == 50
    assert obj3.tachyT == 110
    assert obj3.brady() == bradycardia()

def test_inst():
    obj1 = ECG_Class('testclass.csv')
    assert obj1.instHR == HRinst(obj1.data)