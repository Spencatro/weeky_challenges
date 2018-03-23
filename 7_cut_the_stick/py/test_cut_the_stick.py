import datetime
import pytest

from cut_the_stick import cut_the_stick
from cut_the_stick import slow_cut_the_stick


def test_cut_the_stick_ex():
    assert cut_the_stick([5, 4, 4, 2, 2, 8]) == [6, 4, 2, 1]
    assert cut_the_stick([1, 2, 3, 4, 3, 3, 2, 1]) == [8, 6, 4, 1]


def test_cut_sticks_only_once():
    for i in range(1, 100):
        assert cut_the_stick([1] * i) == [i]
    assert cut_the_stick([]) == []


def test_profile_sticks():
    unwieldy_stick_test = []
    for i in range(1, 400):
        for j in range(1, 1000):
            unwieldy_stick_test.append(i)
    fast_start = datetime.datetime.now()
    fast_res = cut_the_stick(unwieldy_stick_test)
    fast_end = datetime.datetime.now()
    fast_time = fast_end - fast_start
    assert fast_time < datetime.timedelta(seconds=.1)

    unwieldy_stick_test = []
    for i in range(1, 400):
        for j in range(1, 1000):
            unwieldy_stick_test.append(i)
    print(len(unwieldy_stick_test))
    slow_start = datetime.datetime.now()
    slow_res = slow_cut_the_stick(unwieldy_stick_test)
    slow_end = datetime.datetime.now()


    slow_time = slow_end - slow_start

    print(fast_time.total_seconds())
    print(slow_time.total_seconds())

    assert fast_res == slow_res
    assert fast_time < slow_time




if __name__ == '__main__':
    pytest.main()

