import pytest
from ProductOfAllOtherElementsInArray import products

class TestProductOfElements(object):
    def test_normal_list(self):
        my_array = [1, 2, 3, 4, 5]
        results  = products(my_array)
        assert results == [120, 60, 40, 30, 24]

    def test_empty_list(self):
        my_array = []
        results = products(my_array)
        assert len(results) == 0
            
    def test_list_with_zero(self):
        my_array = [1, 2, 0, 3, 4]
        results  = products(my_array)
        assert results == [0, 0, 24, 0, 0]
