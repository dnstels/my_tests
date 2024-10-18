
from contextlib import nullcontext as does_not_raise

import sys

import pytest
sys.path.append('.')
from core import definitions
import core.tools as tools
from core.dto import Flowline
import fake_pipesim_data as input_data


model=None

def test_init_empty():
    indata=tools.norm_dict(Flowline,{})
    # with pytest.raises(Exception):
    with does_not_raise():
        sut=Flowline(**indata)
        assert sut is not None
        assert isinstance(sut.Diameter,float)

@pytest.mark.parametrize(
    "flowline_name",
    [
        'kg202-205.Flowline_1',
        'kg202.Flowline_1',
        'kg205.Flowline_1',
    ],
)
def test_init_from_pipesim_model(flowline_name):
    flowline_in, __ =input_data.get_data_flowlines(model)
    indata=tools.map_data(flowline_in[flowline_name],
                          definitions.FLOWLINE_NAME_REPLACEMENT_MAP)
    indata=tools.norm_dict(Flowline,indata)

    with does_not_raise():
        sut=Flowline(**indata)
        assert sut is not None
        sut.Name=flowline_name
        assert isinstance(sut.HorizontalDistance,float)
        # assert isinstance(sut.Diameter,None)
        print(sut.to_json())

# @pytest.mark.parametrize(
#     "example_input,expectation",
#     [
#         (3, does_not_raise()),
#         (2, does_not_raise()),
#         (1, does_not_raise()),
#         (0, pytest.raises(ZeroDivisionError)),
#     ],
# )
# def test_division(example_input, expectation):
#     """Test how much I know division."""
#     with expectation:
#         assert (6 / example_input) is not None


if __name__=='__main__':
    test_init_from_pipesim_model('kg202-205.Flowline_1')
    # test_division(0,does_not_raise())
