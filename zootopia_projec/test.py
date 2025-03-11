from   fetch_information_from_api import load_data
import pytest

def test_loaddata():
    assert load_data() == None

