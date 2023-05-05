from proconlib.two_pointers import two_pointers
import pytest


def test_two_pointers():
    N = 7
    A = [11, 12, 16, 22, 27, 28, 31]
    K = 10

    def f(x, y):
        return A[y] - A[x] <= K

    tot = 0

    def g(x, y):
        nonlocal tot
        tot += y-x
    two_pointers(0, N-1, f, g)
    assert tot == 11


def test_two_pointers_2():
    N = 5
    A = [0, 100, 200, 300, 400]
    K = 10

    def f(x, y):
        return A[y] - A[x] <= K

    tot = 0

    def g(x, y):
        nonlocal tot
        tot += 1
    two_pointers(0, N-1, f, g)
    assert tot == 5


@pytest.mark.randomize(l=pytest.list_of(int, items=1000), k=int)
def test_two_pointer_quickcheck(l, k):
    import bisect
    l.sort()
    n = len(l)

    def f(x, y):
        return l[y]-l[x] <= k

    tot1 = 0

    def g(x, y):
        nonlocal tot1
        tot1 += (y-x+1)

    two_pointers(0, n-1, f, g)

    tot2 = 0
    for i in range(n):
        ll = l[i:n]
        tot2 += bisect.bisect_right(ll, ll[0]+k)

    assert tot1 == tot2
