from proconlib.binary_search import binary_search
import pytest


def test_binary_search():
    A = [1, 3, 4, 5, 5, 6, 7, 8, 10]
    assert binary_search(0, 9, lambda i: A[i] > 5) == 5
    assert binary_search(0, 9, lambda i: A[i] >= 5) == 3
    assert binary_search(0, 9, lambda i: A[i] > 10) == 9
    assert binary_search(0, 9, lambda i: A[i] > 0) == 0
    assert binary_search(0, 9, lambda i: A[i] > 1) == 1


@pytest.mark.randomize(l=pytest.list_of(int, items=10000), x=int)
def test_binary_search_quichcheck(l, x):
    l.sort()
    n = len(l)
    l1 = binary_search(0, n, lambda i: l[i] >= x)
    r1 = binary_search(0, n, lambda i: l[i] > x)
    import bisect
    l2 = bisect.bisect_left(l, x)
    r2 = bisect.bisect_right(l, x)
    assert l1 == l2
    assert r1 == r2
