from proconlib.rerooting import Rerooting

def f(*xs):
    out = 0
    for x in xs:
        out += x
    return out

def test_rerooting():
    t = Rerooting(5, f)
    E = [(0,1),(0,2),(0,3),(2,4)]
    for (u,v) in E:
        t.add_edge(u,v,1)
        t.add_edge(v,u,1)
    A = [
        (0,1,1),
        (0,2,1),
        (0,3,1),
        (0,4,2),
        (1,2,2),
        (1,3,2),
        (1,4,3),
        (2,3,2),
        (2,4,1),
        (3,4,3),
    ]
    for (u,v,expected) in A:
        assert t.calc(u,v) == expected
        assert t.calc(v,u) == expected