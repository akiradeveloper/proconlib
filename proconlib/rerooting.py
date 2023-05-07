from typing import *
import itertools


class Rerooting:
    # f: (u, v, sum(L))
    # g: (L)
    def __init__(self, n, f, g):
        G = [[] for _ in range(n)]
        self.G = G
        self.f = f
        self.g = g
        self.evals = {}
        self.dp = {}

    def cumsum(self, xs):
        id = self.g()
        out = [id]
        for i, x in enumerate(xs):
            out.append(self.g(out[i], x))
        return out

    def add_edge(self, u, v):
        self.G[u].append(v)

    def dfs_once(self, par, u):
        for v in self.G[u]:
            if v == par:
                continue
            self.dfs_once(u, v)

        print(par, u)
        if par is not None:
            dp = []
            for v in self.G[u]:
                if v == par:
                    continue
                dp.append(self.dp[(v, u)])
            n = len(dp)
            cumL = self.cumsum(dp)
            newv = self.f(u, par, cumL[n])
            self.dp[(u, par)] = newv

    def dfs_reroot(self, par, u):
        dp = []
        for v in self.G[u]:
            dp.append(self.dp[(v, u)])
        n = len(dp)
        cumL = self.cumsum(dp)
        dp.reverse()
        cumR = self.cumsum(dp)
        for i, v in enumerate(self.G[u]):
            L = i
            R = n-L-1
            newv = self.f(u, v, self.g(cumL[L], cumR[R]))
            self.dp[(u, v)] = newv
        for v in self.G[u]:
            if v == par:
                continue
            self.dfs_reroot(u, v)

    def calc(self, u, v):
        return self.dp[(u, v)]
