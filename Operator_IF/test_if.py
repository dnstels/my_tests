
from operator_if.fun_if import get_result_of_number


def test_get_result_of_number():
    assert get_result_of_number(-1) == 'Отрицательное'
    assert get_result_of_number(1) == 'Положительное'
    assert get_result_of_number(0) == 'Ноль'
    