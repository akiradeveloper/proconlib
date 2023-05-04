from typing import *


class ModComb:
    def __init__(self, NMAX: int, M: int):
        fac = [0 for _ in range(NMAX+1)]
        fac[0] = fac[1] = 1
        finv = [0 for _ in range(NMAX+1)]
        finv[0] = finv[1] = 1
        inv = [0 for _ in range(NMAX+1)]
        inv[1] = 1

        for i in range(2, NMAX+1):
            fac[i] = fac[i-1] * i % M
            inv[i] = M - inv[M % i] * (M//i) % M
            finv[i] = finv[i-1] * inv[i] % M

        self.fac = fac
        self.finv = finv
        self.inv = inv