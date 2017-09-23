from HRinst import HRinst
import numpy as np

dataset = (np.arange(0,29),np.array([0,1,2,1,0,-1,10,10,3,2,0,4,5,0,9,10,11,10,0,1,2,4,3,8.5,8.6,8,1,2,3]))
result = HRinst(dataset)

def test_HRinst():
    assert type(result)== np.ndarray
    assert result.shape[1]==2
    assert np.all((result == (np.array([[  0.,   0.],
        [  1.,   0.],
        [  2.,   0.],
        [  3.,   0.],
        [  4.,   0.],
        [  5.,   0.],
        [  6.,  10.],
        [  7.,  10.],
        [  8.,  10.],
        [  9.,  10.],
        [ 10.,  10.],
        [ 11.,  10.],
        [ 12.,  10.],
        [ 13.,  10.],
        [ 14.,  10.],
        [ 15.,  10.],
        [ 16.,   6.],
        [ 17.,   6.],
        [ 18.,   6.],
        [ 19.,   6.],
        [ 20.,   6.],
        [ 21.,   6.],
        [ 22.,   6.],
        [ 23.,   6.],
        [ 24.,   6.],
        [ 25.,   6.],
        [ 26.,   6.],
        [ 27.,   6.],
        [ 28.,   6.]]))))
test_HRinst()