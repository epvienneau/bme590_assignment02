def test_tachybradycardia():
    from tachybradycardia import bradycardia, tachycardia
    import numpy as np
    testerarray = np.array([100, 88, 101, 64, 160, 60.5, 59, 40, 200, 0, -1, 109.5, 90, 80, 62])
    lowerthresholds = np.array([60, 50, 70])
    upperthresholds = np.array([100, 90, 110])
    bradyanswers = np.array([[0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1]])
    tachyanswers = np.array([[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
    for i in range(0, 3):
        bradylist = bradycardia(testerarray, lowerthresholds[i])
        tachylist = tachycardia(testerarray, upperthresholds[i])
        assert len(bradylist) == np.size(testerarray)
        assert len(tachylist) == np.size(testerarray)
        assert bradylist == bradyanswers[i]
        assert tachylist == tachyanswers[i]
