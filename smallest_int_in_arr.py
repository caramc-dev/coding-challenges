def find_smallest_int(arr):
    return sorted(arr)[0]

def find_smallest_int_2(arr):
    return min(arr)

"""
Attpt 1
Sorted and returned index position 1

Attpt 2
Returned the min value in the array (simpler)
"""


"""
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
"""