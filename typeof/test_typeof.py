

def test_type_1():
    a=1
    assert type(a) == type(1)
    assert type(a) == int
    assert isinstance(a,int)

def test_list_is_mutable():
    m = list([1, 2, 3])
    n = m
    assert n is m
    assert id(n)==id(m)
    n.pop()
    assert n is m
    assert id(n)==id(m)
    assert len(n)==len(m)
    assert n == list([1,2])
    assert m == list([1,2])

def test_int_is_immutable():
    a=1
    b=a
    assert a is b
    b+=1
    assert a is not b

def test_list_copy():
    m = list([1, 2, 3])
    n = m.copy()
    assert n is not m
    assert id(n)!=id(m)
    n.pop()
    assert len(n)!=len(m)



