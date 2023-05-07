from proconlib.hld import HLD

def test_hld():
    E = [(0,1),(0,2),(0,3),(1,4),(1,5),(8,4),(4,9),(6,2),(6,10),(6,11),(6,12),(3,7)]
    t = HLD(13)
    for (u,v) in E:
        t.connect(u,v)
    t.build(0)

    print(t.heavy_head)

    LCA = [
        (0,0,0),
        (8,10,0),
        (8,12,0),
        (4,5,1),
        (2,7,0),
        (3,7,3),
        (10,12,6),
        (2,12,2), 
    ]

    for (u,v,lca) in LCA:
        assert t.lca(u,v) == lca
        assert t.lca(v,u) == lca

def test_hld_networkx():
    import networkx
    N = 1000
    refG = networkx.generators.trees.random_tree(N)
    refG = networkx.dfs_tree(refG, 0)
    ref = networkx.algorithms.all_pairs_lowest_common_ancestor(refG)

    G = HLD(N)
    for u, v in refG.edges():
        G.connect(u, v)
    G.build(0)

    # very slow.
    for ((u, v), lca) in ref:
        assert G.lca(u, v) == lca