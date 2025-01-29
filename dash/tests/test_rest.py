import sys
import pytest
sys.path.append('.')

from get_rest import create_request_department_for_LabourCost, get_fake_graph_data, get_from


def test_get_from():
    err,res=get_from(url='http://fake_url',endPoint=None)
    assert res == None
    assert err != None

def test_print_fakedata():
    txt=get_fake_graph_data()
    # print(txt.to_json())
    res=f"""{{['weekNumberOfThePlanEndDate':]}}"""
    print(txt)

@pytest.mark.parametrize("test_input,expected",[
    (None,''),
    ("Строка","%D0%A1%D1%82%D1%80%D0%BE%D0%BA%D0%B0"),
    (["str1","str2"],"str1%2Cstr2"),
    (["str1"],"str1"),([],"")
    ])
def test_create_request_department_for_LabourCost(test_input,expected):
    assert create_request_department_for_LabourCost(test_input) == expected
