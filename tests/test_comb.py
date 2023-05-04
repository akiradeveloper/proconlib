from proconlib.comb import ModComb

import pytest


@pytest.mark.parametrize("n,k,ans", [
    (10, 2, 55),
    (10, 3, 220),
    (10, 4, 715),
    (400, 296, 546898535),
    (100000, 100000, 939733670)
])
def test_mod_comb_nHk(n, k, ans):
    M = 1_000_000_007
    m = ModComb(2*100000, M)
    a = k+n-1
    b = k
    nHk = m.fac[a] * m.finv[b] * m.finv[a-k]
    assert nHk % M == ans
