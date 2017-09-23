from load_data import load_data
import pytest

tester = load_data('data.csv')


def test_format():

    assert tester is tuple
    assert tester.len() == 2


def test_columns_full():

    assert tester[0] != []
    assert tester[1] != []


def test_assertions_type():

    with pytest.raises(ValueError, match=r'.* .csv .*'):
        assert load_data('hello')


def test_assertions_size():
    with pytest.raises(ValueError, match=r'.* two .*'):
        assert load_data('onecol.csv')

