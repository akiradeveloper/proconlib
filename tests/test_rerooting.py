from proconlib.rerooting import Rerooting

def test_rerooting_size():
    def f(*xs):
        out = 0
        for x in xs:
            out += x
        return out
    def g(e, dp):
      return e + dp

    t = Rerooting(5, f, g)
    E = [(0,1),(0,2),(0,3),(2,4)]
    for (u,v) in E:
        t.add_edge(u,v,1)
        t.add_edge(v,u,1)
    t.dfs_once(None, 0)
    t.dfs_reroot(None, 0)
    print(t.dp)

    A = [
        (0,1,4),
        (1,0,1),
        (0,2,3),
        (2,0,2),
        (0,3,4),
        (3,0,1),
        (2,4,4),
        (4,2,1),
    ]
    for (u,v,expected) in A:
        assert t.calc(u,v) == expected