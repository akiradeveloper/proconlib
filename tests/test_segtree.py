from proconlib.segtree import *

import pytest

@pytest.mark.randomize(T=pytest.list_of(int, items=50))
def test_segtree(T):
    def F(*xs):
        out = 0
        for x in xs:
            out = max(out, x)
        return out

    n = len(T)
    L = [0 for _ in range(n)]
    S = SegTree(n, F)
    for i in range(n):
        x = abs(T[i])
        # set
        L[i] = x
        S.set_val(i, x)

        # compare
        for l in range(n):
            for r in range(n):
                if l < r:
                    assert S.fold(l,r) == max(L[l:r])