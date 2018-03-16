import pytest
from flatland_space_station import flatland_space_stations,  max_distance_between_stations


def test_max_d():
    assert max_distance_between_stations(-1, 0) == 0
    assert max_distance_between_stations(-1, 1) == 1
    assert max_distance_between_stations(-1, 2) == 2
    assert max_distance_between_stations(0, 2) == 1
    assert max_distance_between_stations(0, 3) == 1
    assert max_distance_between_stations(0, 4) == 2
    assert max_distance_between_stations(0, 5) == 2
    assert max_distance_between_stations(1, 2) == 0
    assert max_distance_between_stations(1, 3) == 1
    assert max_distance_between_stations(1, 4) == 1
    assert max_distance_between_stations(1, 5) == 2
    assert max_distance_between_stations(1, 6) == 2


def test_trivial_towns():
    assert flatland_space_stations(3, [0,1,2]) == 0
    assert flatland_space_stations(5, [0,2]) == 2


def test_furthest_is_first():
    assert flatland_space_stations(10, [8]) == 8


def test_furthest_is_first_distance_is_1():
    assert flatland_space_stations(3, [1, 2]) == 1


def test_furthest_is_last_distance_is_1():
    assert flatland_space_stations(3, [0, 1]) == 1


def test_furthest_is_last():
    assert flatland_space_stations(10, [2]) == 7


def test_furthest_is_in_middle_odd_distance():
    assert flatland_space_stations(7, [0, 6]) == 3


def test_furthest_is_in_middle_even_distance():
    assert flatland_space_stations(5, [0, 4]) == 2


def test_furthest_is_in_middle_distance_is_1():
    assert flatland_space_stations(3, [0, 2]) == 1
    assert flatland_space_stations(4, [0, 3]) == 1


def test_unsorted_cities():
    assert flatland_space_stations(5, [3, 1, 2, 0, 4]) == 0
    assert flatland_space_stations(5, [3, 1, 0, 4]) == 1
    assert flatland_space_stations(5, [1, 0, 4]) == 1
    assert flatland_space_stations(7, [2, 0, 6]) == 2
    assert flatland_space_stations(7, [6, 0, 2]) == 2
    assert flatland_space_stations(7, [6, 2, 0]) == 2


if __name__ == '__main__':
    pytest.main()