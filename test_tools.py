
import string
import sys
sys.path.append('.')
from core.models import Sink
import core.tools as tools


def test_get_first_or_none_noiterable():
    sut_a=123
    sut_b=None
    assert tools.get_first_or_none(sut_a) == None
    assert tools.get_first_or_none(sut_b) == None

def test_get_first_or_none_list():
    sut=list(range(10))
    assert tools.get_first_or_none(sut) == 0

def test_get_first_or_none_dict():
    sut_a=dict(zip(range(10),list(map(chr, range(ord('a'),ord('a')+10)))))
    sut_b=dict(zip(list(map(chr, range(ord('a'),ord('a')+10))),range(10)))
    assert tools.get_first_or_none(sut_a) == 0
    assert tools.get_first_or_none(sut_b) == 'a'

def test_get_first_or_none_range():
    sut=range(5,10)
    assert tools.get_first_or_none(sut) == 5

def test_get_first_or_none_string():
    sut=string.ascii_lowercase
    assert tools.get_first_or_none(sut) == 'a'

if __name__=='__main__':
    tup=('a','b','z')
    di={'a':1,'b':2,'c':3}
    sss={
            "Pressure":0.1,
            'Temperature':0.2,
            'GasFlowRate':0.3
    }
    print(tools.norm_dict(Sink,sss))
    pass
