from .load_data import load_data
from .take_average import get_interval
from .take_average import average
import numpy as np
import pytest
import unittest

tup = load_data('TestAve.csv')
time = tup[0]
hr = tup[1]
mat = np.transpose(np.array([time, hr]))


def test_seglen():

    assert get_interval(time, 60) == 60
    assert get_interval(time, 180) == 180


def test_output():

    assert type(average(hr, time, 3)) is list


class MyTestCase(unittest.TestCase):

    def test_seg(self):
        self.assertRaises(ValueError, get_interval, mat, 1200)
