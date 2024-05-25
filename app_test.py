import pytest
from app import bubble_sort


def test_bubble_sort():
    test_arr = [1, 5, 3, 2, 4, 6, 8, 7, 9, 0]
    assert bubble_sort(test_arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
