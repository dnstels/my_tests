
import pytest

def get_result_of_number_one_string(num) : 
    return 'Положительное' if num>0 else 'Отрицательное' if num<0 else 'Ноль'

@pytest.mark.parametrize("test_input,expected",[
    (-1,"Отрицательное"),(1,"Положительное"),(0,"Ноль")])
def test_get_result_of_number(test_input, expected):
    assert get_result_of_number_one_string(test_input) == expected
    