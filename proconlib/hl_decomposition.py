from typing import *

class HLD:
    def __init__(self, n):
        self.G = [[] for _ in range(n)]
        self.subcnt = [0 for _ in range(n)]
        self.depth = [0 for _ in range(n)]
        self.par = [None for _ in range(n)]
        self.real_to_virt = [0 for _ in range(n)]
        self.virt_to_real = [0 for _ in range(n)]
        self.heavy_next = [None for _ in range(n)]
        self.heavy_head = [0 for _ in range(n)]

    def connect(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)

    def dfs1(self, root):
        self.depth[root] = 0
        self.par[root] = None
        self.dfs1_sub(root, None)
    
    def dfs1_sub(self, u, par) -> int:
        cnt = 1
        for v in self.G[u]:
            if v == par:
                continue
            self.depth[v] = self.depth[u] + 1
            self.par[v] = u
            cnt += self.dfs1_sub(v, u)
        
        self.subcnt[u] = cnt
        return cnt

    def dfs2(self, root):
        self.dfs2_sub(root, None)

    def dfs2_sub(self, u, par):
        maxv = 0
        heavy_next = None

        for v in self.G[u]:
            if v == par:
                continue
            if self.subcnt[v] > maxv:
                maxv = self.subcnt[v]
                heavy_next = v
            
        if heavy_next is not None:
            self.heavy_next[u] = heavy_next
            self.dfs2_sub(heavy_next, u)

        for v in self.G[u]:
            if v == par or v == heavy_next:
                continue
            self.dfs2_sub(v, u)

    def bfs(self, root):
        from collections import deque
        cur_vid = 0
        q = deque()
        q.append(root)
        while q:
            hn = q.popleft()
            cur = hn
            while cur is not None:
                self.real_to_virt[cur] = cur_vid
                cur_vid += 1
                self.heavy_head[cur] = hn
                for v in self.G[cur]:
                    if v == self.par[cur] or v == self.heavy_next[cur]:
                        continue
                    q.append(v)
                cur = self.heavy_next[cur]

    def build(self, root):
        self.dfs1(root)
        self.dfs2(root)
        self.bfs(root)
        for i, x in enumerate(self.real_to_virt):
            self.virt_to_real[x] = i

    def lca(self, u, v) -> int:
        l = u
        r = v
        while True:
            if self.real_to_virt[l] > self.real_to_virt[r]:
                l, r = r, l
            if self.heavy_head[l] == self.heavy_head[r]:
                return l
            r = self.par[self.heavy_head[r]]

    def decompose(self, u, v) -> list[(int, int)]:
        out = []
        l = u
        r = v
        while True:
            if self.real_to_virt[l] > self.real_to_virt[r]:
                l, r = r, l
            p = (
                max(self.real_to_virt[l], self.real_to_virt[self.heavy_head[r]]),
                self.real_to_virt[r],
            )
            out.append(p)
            if self.heavy_head[l] != self.heavy_head[r]:
                r = self.par[self.heavy_head[r]]
            else:
                break

        return out


