from src.calculator import sumar, restar

def test_sumar():
    assert sumar(5, 3) == 8
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0


def test_restar():
    assert restar(5, 3) == 2
    assert restar(-1, -1) == 0
    assert restar(0, 5) == -5