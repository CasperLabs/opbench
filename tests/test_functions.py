from opbench.helper import round_up


def test_round_up():
    assert round_up(3.2, 1) == 4
    assert round_up(684, 2) == 690
    assert round_up(1239000, 3) == 1240000
    assert round_up(1231000, 3) == 1240000
    assert round_up(-1239000, 3) == -1230000
    assert round_up(-1231000, 3) == -1230000
    assert round_up(0.64, 1) == 1
    assert round_up(-0.64, 1) == -1
    assert round_up(0, 1) == 0
