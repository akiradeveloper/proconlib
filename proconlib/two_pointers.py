from typing import *


def two_pointers(start: int, end: int, f, g):
    l = start
    r = start

    def callback():
        if f(l, r):
            g(l, r)

    while not (l == end and r == end):
        if r < end:
            if f(l, r+1):
                r += 1
            else:
                if l < r:
                    callback()
                    l += 1
                else:
                    callback()
                    r += 1
        else:
            callback()
            l += 1
    callback()