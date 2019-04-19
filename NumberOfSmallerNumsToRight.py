'''
Given an array of integers, return an array with elements where each element
corresponds to the number of elements to the right of the number in the original
array that are smaller than the number.
'''

import bisect

def smaller_counts_to_right(array):
    '''
    ALGORITHM: A sorted array of numbers seen so far is maintained. The origi-
    nal list is traversed in the reverse order. The index in the sorted array,
    where the current number may be inserted provides the requisite number.
    '''
    result = []

    # array of the numbers seen so far in a sorted order
    seen = []

    for num in reversed(array):

        # Get the position in the sorted array where the current number may
        # be inserted
        index = bisect.bisect_left(seen, num)

        # The index indicates the number of elements that are smaller than
        # the current number
        result.append(index)

        # Insert the current number at the appropriate position in the sorted
        # array
        bisect.insort(seen, num)

    return list(reversed(result))
