'''
Given an array of numbers, find the maximum sum of any contiguous sub-array
of the array.
'''

def max_sub_array_sum(array):
    '''
    The function returns the maximum sum of any contiguous sub-array of the
    array.

    array: an array of integers

    ALGORITHM: Kadane's Algorithm (O(n) time and O(1) space)
    The algorithm traverses the array and at each index maintains the current
    maximum sum that is the sum of the item at the current index and the
    current maximum.
    '''

    max_until_index = 0
    max_so_far = 0
    for item in array:
        max_until_index = max(item, max_until_index + item)
        max_so_far = max(max_until_index, max_so_far)

    return max_so_far

def min_sub_array_sum(array):
    '''
    The function returns the minimum sum of any contiguous sub-array of the 
    array.

    array: an array of integers

    ALGORITHM:
    The array is traversed sequentially with two variables maintaining the
    minimum value until that index which is minimum of the the value at the
    current index and the sum of the value at the current index and the mini-
    mum value until the previous index and minimum seen so far. Whenever a 
    smaller sub-array sum is found ending at a given index, the value is up-
    dated.
    '''

    min_until_index = 0
    min_so_far = 0

    for item in array:
        min_until_index = min (item, item + min_until_index)
        min_so_far = min(min_until_index, min_so_far)

    return min_so_far

def max_circular_sub_array_sum(array):
    '''
    The function returns the maximum sub-array sum with wrap-around allowed.

    ALGORITHM:
    A corresponding minimum sub-array sum is found that locates a sub-array
    that results in the smallest sum. When this sub-array is subtracted from
    the sum of the array, the maximum sub-array sum with wrap-around is found.
    This sum is then compared with the maximum sum without the wrap-around and
    the maximum of the two is returned.
    '''

    max_sum_circular = sum(array) - min_sub_array_sum(array)
    return max(max_sub_array_sum(array), max_sum_circular)
    
