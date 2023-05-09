
ROLIHA_MASK30 = (1 << 30) - 1
ROLIHA_MASK31 = (1 << 31) - 1
ROLIHA_MOD = (1 << 61) - 1
ROLIHA_MASK61 = ROLIHA_MOD
ROLIHA_P = ROLIHA_MOD * 4


def mul(a, b):
    au = a >> 31
    ad = a & ROLIHA_MASK31
    bu = b >> 31
    bd = b & ROLIHA_MASK31
    mid = ad*bu + au*bd
    midu = mid >> 30
    midd = mid & ROLIHA_MASK30
    return au*bu*2 + midu + (midd << 31) + ad*bd


def calcmod(x):
    xu = x >> 61
    xd = x & ROLIHA_MASK61
    out = xu + xd
    if out >= ROLIHA_MOD:
        out -= ROLIHA_MOD
    return out


import random
class RoLiHa:
    def __init__(self, s):
        assert 0 not in s
        
        n = len(s)
        b = random.randint(2, ROLIHA_MOD-2)
        powMemo = [0 for _ in range(n+1)]
        powMemo[0] = 1
        for i in range(1, n+1):
            powMemo[i] = calcmod(mul(powMemo[i-1], b))
        hash = [0 for _ in range(n+1)]
        for i in range(0, n):
            hash[i+1] = calcmod(mul(hash[i], b) + s[i])

        self.powMemo = powMemo
        self.hash = hash

    def get(self, l, r):
        return calcmod(self.hash[r] + ROLIHA_P - mul(self.hash[l], self.powMemo[r-l]))

    def concat(self, h1, h2, h2len):
        return calcmod(mul(h1, self.powMemo[h2len]) + h2)