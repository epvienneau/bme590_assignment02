from main import main
import os
import time

def test_main():
    timeSinceEpoch = time.time()
    main('Test_ECG.csv', 3)
    timeStamp = os.path.getmtime('assignment02.csv')
    assert timeStamp > timeSinceEpoch  #asserts that new file was actually created/modified in calling of main function