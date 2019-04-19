import pytest

from NumberOfSmallerNumsToRight import smaller_counts_to_right

def verify_results(array, expected):
    result = smaller_counts_to_right(array)
    assert result == expected
    
class TestNumberOfSmallerNumsToRight(object):

    def test_general_case(self):
        my_array = [3, 4, 9, 6, 1]
        expected = [1, 1, 2, 1, 0]
        verify_results(my_array, expected)

    def test_monotonically_increasing(self):
        my_array = [1, 3, 5, 7, 9]
        expected = [0, 0, 0, 0, 0]
        verify_results(my_array, expected)

    def test_monotonically_decreasing(self):
        my_array = [5, 4, 3, 2, 1]
        expected = [4, 3, 2, 1, 0]
        verify_results(my_array, expected)

    def test_array_with_repetitions(self):
        my_array = [3, 6, 2, 2, 1, 8, 4, 8]
        expected = [3, 4, 1, 1, 0, 1, 0, 0]
        verify_results(my_array, expected)
