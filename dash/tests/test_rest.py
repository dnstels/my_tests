import pytest
from get_rest import get_LabourCost, get_fake, get_from


def test_get_from():
    err,res=get_from(url='http://fake_url',endPoint=None)
    assert res == None
    assert err != None

def test_get_LabourCost():
    err,res=get_LabourCost(None)
    assert res == None
    assert err != None

def test_print_fakedata():
    txt=get_fake()
    # print(txt.to_json())
    res=f"""{{['weekNumberOfThePlanEndDate':]}}"""
    print(txt)