import pytest

from MaxSubArraySum import max_sub_array_sum, max_circular_sub_array_sum

def verify_results(array, expected):
    max_sum = max_sub_array_sum(array)
    assert max_sum == expected

def verify_results_circular(array, expected):
    max_sum = max_circular_sub_array_sum(array)
    assert max_sum == expected

class TestMaxSubArraySum(object):

    def test_normal_array(self):
        my_array = [34, -50, 42, 14, -5, 86]
        verify_results(my_array, 137)

    def test_all_negative(self):
        my_array = [-5, -1, -8, -9]
        verify_results(my_array, 0)

class TestMaxSubArraySumWithWrapAround(object):

    def test_normal_array(self):
        my_array = [8, -1, 3, 4]
        verify_results_circular(my_array, 15)
        
