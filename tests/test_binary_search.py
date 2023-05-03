from proconlib.binary_search import binary_search


def test_binary_search():
    A = [1, 3, 4, 5, 5, 6, 7, 8, 10]
    assert binary_search(0, 9, lambda i: A[i] > 5) == 5
    assert binary_search(0, 9, lambda i: A[i] >= 5) == 3
    assert binary_search(0, 9, lambda i: A[i] > 10) == 9
    assert binary_search(0, 9, lambda i: A[i] > 0) == 0
    assert binary_search(0, 9, lambda i: A[i] > 1) == 1
