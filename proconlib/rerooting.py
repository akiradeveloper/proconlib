from typing import *
import itertools

class Rerooting:
    def __init__(self, n, id, f):
        g = [[] for _ in range(n)]
        self.g = g
        self.id = id
        self.f = f
        self.evals = {}
        self.dp = {}

    def cumsum(self, xs, id = 0):
        out = [id]
        for i, x in enumerate(xs):
            out.append(self.f(out[i], x))
        return out

    def add_edge(self, u, v, eval):
        self.evals[(u, v)] = eval

    def dfs_once(self, par, u):
        for v in self.g[u]:
            if v == par:
                continue
            self.dfs1(u, v)
        
        if par:
            dp = []
            for v in self.g[u]:
                if v == par:
                    continue
                dp.append(self.dp[(v, u)])
            cumL = self.cumsum(dp)
            newv = self.f(self.evals[(u, par)], cumL[len(cumL)])
            self.dp[(u, par)] = newv

    def reroot(self, par, u):
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
            newv = self.f(cumL[L], cumR[R])
            newv = self.f(newv, self.evals[(u, v)])
            self.dp[(u, v)] = newv
        for v in self.g[u]:
            if v == par:
                continue
            self.reroot(u, v)

    def calc(self, u, v):
        self.dp[(u, v)]