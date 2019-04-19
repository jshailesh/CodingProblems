'''
Given an array of integers that are out of order, determine the bounds of the
smallest window that must be sorted in ofer for the entier array to be sorted.
'''

def smallest_window(array):
    '''
    The function returns the lower and upper indices of the array elements that
    form a window that needs to be sorted to have the arrays sorted.

    array: an array of integers that are out of order.

    ALGORITHM: For the lower bound, we start tracing the array from the left
    and compare every element with the current maximum. If an element is small-
    er than the current maximum, that becomes the lower bound.
    Similarly, for the upper bound, we start tracing the array from the right
    and compare every element with the current mininum. If an alement is greater
    that the current minimum, that becomes the upper bound.
    '''

    left, right = None, None
    len_array = len(array)

    max_seen = -float("inf")
    min_seen = float("inf")

    for i in range(len(array)):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i

    for i in range(len(array) - 1, -1, -1):
        min_seen = min(min_seen, array[i])
        if array[i] > min_seen:
            left = i

    return left, right


        
