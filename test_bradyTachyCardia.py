from bradyTachyCardia import bradyTachyCardia as BTC

def test_bradyTachyCardia():
    times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    HRs = [0, 50, 90, 110, 70, 60, 100, 112, 40, 30, -1, 200, 64, 76]
    testerArray = (times, HRs)
    BTClist = BTC(testerArray)
    assert type(BTClist) is list
    assert len(BTClist) == len(HRs)
    assert BTClist == ('--', 'B', 'N', 'T', 'N', 'B', 'T', 'T', 'B', 'B', 'B', 'T', 'N', 'N')
