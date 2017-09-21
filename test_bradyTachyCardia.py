from bradyTachyCardia import bradyTachyCardia as BTC

def test_bradyTachyCardia():
    testerArray = (100, 88, 101, 64, 160, 60, 59, 40, 71, 0, -1, 200, 90, 80, 62)
    BTClist = BTC(testerArray)
    assert BTClist.size == testerArray.size()
    assert BTClist.dim == testerArray.dim()
    assert BTClist == ('T', 'N', 'T', 'N', 'T', 'B', 'B', 'B', 'N', 'B', 'B', 'T', 'N', 'N', 'N')