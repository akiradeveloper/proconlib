from typing import *


def binary_search(l: int, r: int, f: Callable[[int], bool]) -> int:
    lo = l
    hi = r
    while lo < hi:
        mid = (lo+hi) // 2
        if f(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
