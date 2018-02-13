import pytest

from append_and_delete import append_and_delete


def test_s_can_transform_to_t_in_k_moves():
    assert append_and_delete(3, "asda", "a")


def test_s_can_transform_to_t_in_less_than_k_moves():
    assert append_and_delete(300, "asda", "a")


def test_difference_between_length_of_s_and_t_is_greater_than_k():
    assert not append_and_delete(1, "asdasd", "a")
    assert not append_and_delete(1, "a", "asdasdas")


def test_s_and_t_match():
    assert append_and_delete(0, "a", "a")
    assert append_and_delete(10, "a", "a")
    assert append_and_delete(-10, "a", "a")


def test_s_and_t_similar_length_and_different_contents_not_enough_k():
    assert not append_and_delete(3, "123456", "0234567")
    assert not append_and_delete(3, "1234567", "023456")


def test_s_and_t_same_length_but_different_contents_not_enough_k():
    assert not append_and_delete(3, "cant transform", "wont transform")
    assert not append_and_delete(10, "cant transform", "wont transform")
