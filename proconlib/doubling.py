from typing import *

def doubling_table(f, g, n):
    # out[i] = f^(2^i)
    out = [f]
    for i in range(n):
        cur_f = out[i]
        ff = g(f, cur_f)
        out.append(ff)
    return out

class Doubling:
    def __init__(self, f, g, max_k: int):
        n = len(format(max_k, 'b'))
        self.f_table = doubling_table(f, g, n)
        self.g = g

    def pow(self, k: int):
        # g() = f0
        out = self.g()
        print(out)

        i = 0
        while k > 0:
            if k & 1 == 1:
                out = self.g(self.f_table[i], out)
            k >>= 1
            i += 1
            
        return out