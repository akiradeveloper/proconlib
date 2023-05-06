from typing import *
import itertools

class Rerooting:
    def __init__(self, n, f):
        g = [[] for _ in range(n)]
        self.g = g
        self.f = f
        self.evals = {}
        self.dp = {}

    def cumsum(self, xs):
        id = self.f()
        out = [id]
        for i, x in enumerate(xs):
            out.append(self.f(out[i], x))
        return out

    def add_edge(self, u, v, eval):
        self.g[u].append(v)
        self.evals[(u, v)] = eval

    def dfs_once(self, par, u):
        for v in self.g[u]:
            if v == par:
                continue
            self.dfs_once(u, v)
        
        print(par, u)
        if not par == None:
            dp = []
            for v in self.g[u]:
                if v == par:
                    continue
                dp.append(self.dp[(v, u)])
            n = len(dp)
            cumL = self.cumsum(dp)
            newv = self.f(self.evals[(u, par)], cumL[n])
            self.dp[(u, par)] = newv

    def dfs_reroot(self, par, u):
        dp = []
        for v in self.g[u]:
            dp.append(self.dp[(v, u)])
        n = len(dp)
        cumL = self.cumsum(dp)
        dp.reverse()
        cumR = self.cumsum(dp)
        for i, v in enumerate(self.g[u]):
            L = i
            R = n-L-1
            newv = self.f(self.evals[(u, v)], cumL[L], cumR[R])
            self.dp[(u, v)] = newv
        for v in self.g[u]:
            if v == par:
                continue
            self.dfs_reroot(u, v)

    def calc(self, u, v):
        return self.dp[(u, v)]