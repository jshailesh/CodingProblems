import pytest
from SmallestWindowToSort import smallest_window

def verify_result(array, expected):
    [left, right] = smallest_window(array)
    assert [left, right] == expected

class TestSmallestWindow(object):
    def test_sorted_list(self):
        my_array = [1, 2, 3, 4, 5]
        verify_result(my_array, [None, None])

    def test_mixed_array(self):
        my_array = [3, 7, 5, 6, 9]
        verify_result(my_array, [1, 3])

    def test_reversed_array(self):
        my_array = [5, 4, 3, 2, 1]
        verify_result(my_array, [0, 4])





        
