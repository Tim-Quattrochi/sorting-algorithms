import pytest
from app import bubble_sort, selection_sort, insertion_sort


@pytest.mark.parametrize("test_arr, sorted_arr", [
    ([1, 5, 3, 2, 4, 6, 8, 7, 9, 0], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),  # random
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),  # sorted
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),  # reverse
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [
        1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),  # duplicate
    ([], []),  # empty
    ([1], [1]),  # single
])
def test_bubble_sort(test_arr, sorted_arr):

    returned_arr, comparisons, swaps = bubble_sort(test_arr)
    assert returned_arr == sorted_arr
    assert comparisons >= swaps, "expected comparisons to be greater than swaps"


def test_selection_sort():
    test_arr = [1, 5, 3, 2, 4, 6, 8, 7, 9, 0]
    assert selection_sort(test_arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_insertion_sort():
    test_arr = [1, 5, 3, 2, 4, 6, 8, 7, 9, 0]
    assert insertion_sort(test_arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
