from proconlib.comb import ModComb

import pytest


@pytest.mark.randomize(n=int, k=int, min_num=1, max_num=100000)
def test_mod_comb_nCk(n, k):
    M = 1_000_000_007
    n, k = max(n, k), min(n, k)
    assert n >= k

    m = ModComb(n, M)
    nCk = m.fac[n] * m.finv[k] * m.finv[n-k]

    import math
    assert nCk % M == math.comb(n, k) % M
