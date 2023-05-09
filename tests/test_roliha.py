from proconlib.roliha import RoLiHa

import pytest

def listord(s):
    out = []
    for c in s:
        out.append(ord(c)+1)
    return out

@pytest.mark.randomize(s=str)
def test_roliha_get(s):
    S = listord(s)
    roli = RoLiHa(S)
    pass
