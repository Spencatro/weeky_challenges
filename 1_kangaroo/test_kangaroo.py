import pytest

from kangaroo import kangaroo


def test_start_position_matches():
    assert kangaroo(1, 0, 1, 0)
    assert kangaroo(1, 1, 1, 0)
    assert kangaroo(1, 0, 1, 1)


def test_starting_position_different_speed_matches():
    assert not kangaroo(1, 2, 0, 2)


def test_kangaroo_1_behind_and_slow():
    assert not kangaroo(1, 1, 2, 2)
    assert not kangaroo(10, 10, 20, 20)


def test_kangaroo_2_behind_and_slow():
    assert not kangaroo(2, 2, 1, 1)
    assert not kangaroo(30, 30, 20, 20)


def test_kangaroo_1_behind_and_meets():
    assert kangaroo(0, 3, 4, 2)


def test_kangaroo_2_behind_and_meets():
    assert kangaroo(4, 2, 0, 3)


def test_kangaro_1_behind_and_passes():
    assert not kangaroo(0, 7, 5, 3)


def test_kangaro_2_behind_and_passes():
    assert not kangaroo(5, 3, 0, 7)


if __name__ == '__main__':
    pytest.main()
