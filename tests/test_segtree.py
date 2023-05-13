from proconlib.segtree import SegTree, LazySegTree

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
                    assert S.fold(l, r) == max(L[l:r])


@pytest.mark.randomize(T=pytest.list_of((int, int, int), items=30), min_num=0, max_num=50)
def test_lazysegtree(T):
    def F(*xs):
        out = 0
        for x in xs:
            out = max(out, x)
        return out

    def G(x, a):
        return max(x, a)

    n = 50
    L = [0 for _ in range(n)]
    S = LazySegTree(n, F, F, G)
    for l, r, x in T:
        # set
        l, r = min(l, r), max(l, r)
        for i in range(l, r):
            L[i] = x
            S.set_val(i, x)

        # compare
        for j in range(n):
            for k in range(n):
                if j < k:
                    assert S.fold(j, k) == max(L[j:k])
