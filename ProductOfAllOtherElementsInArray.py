'''
Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the 
original array except the one at i.
'''

def products(nums):
    '''
    Returns a new array of numbers, wherein the element at i is the product
    of all the elements in the input array except the element at i.

    nums: an array of integers

    ALGORITHM:
    Given an array [1, 2, 3, 4, 5]:
    the desired result for the element at i = 2, for-example, would be
    the product of all the numbers before it (which we call prefix) and the
    the product of all the numbers after it (which we call suffix).
    We create two separate arrays with prefix products and suffix product at
    every index of the input array.
    '''
    prefix_products = []
    for elem in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * elem)
        else:
            prefix_products.append(elem)

    suffix_products = []
    for elem in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * elem)
        else:
            suffix_products.append(elem)

    # Reverse the suffix_products
    suffix_products = list(reversed(suffix_products))

    results = []
    for i in range(len(nums)):
        if i == 0:
            # For the first element:
            results.append(suffix_products[i + 1])

        elif i == len(nums) - 1:
            # For the last element
            results.append(prefix_products[i - 1])

        else:
            # For the rest of the elements
            results.append(prefix_products[i - 1] * suffix_products[i + 1])

    return results
