from proconlib.rerooting import Rerooting


def test_rerooting_size():
    def f(u, v, dp):
        return dp + 1

    def g(*xs):
        out = 0
        for x in xs:
            out += x
        return out

    t = Rerooting(5, f, g)
    E = [(0, 1), (0, 2), (0, 3), (2, 4)]
    for (u, v) in E:
        t.add_edge(u, v)
        t.add_edge(v, u)
    t.dfs_once(None, 0)
    t.dfs_reroot(None, 0)
    print(t.dp)

    A = [
        (0, 1, 4),
        (1, 0, 1),
        (0, 2, 3),
        (2, 0, 2),
        (0, 3, 4),
        (3, 0, 1),
        (2, 4, 4),
        (4, 2, 1),
    ]
    for (u, v, expected) in A:
        assert t.calc(u, v) == expected


def test_rerooting_networkx():
    def f(u, v, dp):
        return dp + 1

    def g(*xs):
        out = 0
        for x in xs:
            out = max(out, x)
        return out

    import networkx
    N = 3000
    G = networkx.generators.trees.random_tree(N)
    T = Rerooting(N, f, g)
    for u, v in G.edges:
        T.add_edge(u, v)
        T.add_edge(v, u)
    T.dfs_once(None, 0)
    T.dfs_reroot(None, 0)

    for u, x in networkx.distance_measures.eccentricity(G).items():
        ecc = 0
        for v in T.G[u]:
            if v != u:
                ecc = max(ecc, T.calc(v, u))
        assert ecc == x
