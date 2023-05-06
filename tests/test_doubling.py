from proconlib.doubling import Doubling

import pytest

M = 1_000_000_007

def g(*fL):
    out = 1
    for f in fL:
        out *= f
        out %= M
    return out

def test_doubling():
    assert g() == 1
    assert g(3,3,3) == 27
    d = Doubling(2, g, 10)
    assert d.pow(10) == 1024

@pytest.mark.randomize(x = int, k = int, min_num = 0, max_num = 10)
def test_doubling_quickcheck(x, k):
    ref = pow(x, k, M)
    f = x
    d = Doubling(f, g, k)
    assert d.pow(k) == pow(x,k,M)
