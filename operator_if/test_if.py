
from operator_if.fun_if import get_result_of_number_one_string


def test_get_result_of_number():
    assert get_result_of_number_one_string(-1) == 'Отрицательное'
    assert get_result_of_number_one_string(1) == 'Положительное'
    assert get_result_of_number_one_string(0) == 'Ноль'
    