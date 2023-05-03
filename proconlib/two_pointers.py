from typing import *


def two_pointers(start: int, end: int, f, g):
    l = start
    r = start
    while not (l == end and r == end):
        cur = f(l, r)
        if r < end:
            nxt = f(l, r+1)
            if nxt:
                r += 1
            else:
                if l < r:
                    if cur:
                        g(l, r)
                    l += 1
                else:
                    if cur:
                        g(l,r)
                    r += 1
        else:
            if cur:
                g(l, r)
            l += 1
    if f(l,r):
        g(l,r)