from typing import *

class Cumsum2:
    def __init__(self, h: int, w: int, default=0):
        self.dp = [[default for _ in range(w+1)] for j in range(h+1)]

    def set(self, i: int, j: int, x):
        self.dp[i+1][j+1] = x

    def build(self):
        double_sweep(self.dp)

    def query(self, p: Tuple[int,int], q: Tuple[int,int]):
        sum1 = self.dp[p[0]][p[1]]
        sum4 = self.dp[q[0]][q[1]]
        sum2 = self.dp[p[0]][q[1]]
        sum3 = self.dp[q[0]][p[1]]
        return sum4 + sum1 - sum2 - sum3


def double_sweep(m):
    h = len(m)
    w = len(m[0])
    for i in range(h):
        for j in range(w-1):
            m[i][j+1] += m[i][j]
    for j in range(w):
        for i in range(h-1):
            m[i+1][j] += m[i][j]
