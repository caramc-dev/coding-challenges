"""
Create a function called find_duplicate_integer(ints) that takes a list of integers that contains a duplicate.

The task is to find the duplicated number
"""


def find_duplicate_integer(integers):
    num_list = []
    for i in integers:
        if i not in num_list:
            num_list.append(i)
        else:
            return i
    return None


# do not modify the values below
print(find_duplicate_integer([1, 3, 4, 2, 2]))