from proconlib.two_pointers import two_pointers


def test_two_pointers():
    N = 7
    A = [11, 12, 16, 22, 27, 28, 31]
    K = 10

    def f(x, y):
        if x == y:
            return True
        if A[y] - A[x] <= K:
            return True
        else:
            return False
    tot = 0

    def g(x, y):
        nonlocal tot
        tot += y-x
    two_pointers(0, N-1, f, g)
    assert tot == 11

def test_two_pointers_2():
    N = 5
    A = [0,100,200,300,400]
    K = 10

    def f(x, y):
        if x == y:
            return True
        if A[y] - A[x] <= K:
            return True
        else:
            return False
    tot = 0
    def g(x, y):
        nonlocal tot
        tot += 1
    two_pointers(0, N-1, f, g)
    assert tot == 5
