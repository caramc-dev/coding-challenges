def question_marks(str):
    # Declare variables to be used
    nums = []
    count = 0

    # Enumerate used to create a list of tuples where it encounters a number,
    # Captures the index position, and the number - converting the value to a number so we can add later
    # Appends to the list as a tuple
    # i.e.
    # [(4, 6), (8, 4), (13, 5), (20, 5), (24, 9)]
    for index, num in enumerate(str):
        if num.isdigit():
            nums.append((index, int(num)))

    # Unpack the tuples created by the for loop as variables that can be compared against each other
    # Loop through the list using zip to compare '2' lists together
    # list '1' is the original nums list, starting at index position zero
    # list '2' is nums[1:] is the list starting at index 1, not index zero.
    # i.e.
    # nums    = [(4,6), (8,4), (13,5), (20,5)]
    # nums[1:]= [(8,4), (13,5), (20,5)]
    # This means we can compare the current iteration of the list against the next.
    #
    # Inside the loop first check if the values in each tuple add up to 10
    # If they do, slice the string on the index positions
    #
    # If the resulting string has 3 question marks add to valid pair counter
    for (index1, value1), (index2, value2) in zip(nums, nums[1:]):
        if value1 + value2 == 10:
            count += 1
            if not str[index1: index2].count("?") == 3:
                return False

    # Check if count is empty (0), as 0 is a falsy value
    # `if not count` is used as more pythonic than `if count < 1`
    if not count:
        return False

    # If none of the false flags are found, then return True
    return True


print(question_marks("arrb6???4xxbl5???eee5ehd9"))




"""
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks.
Check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
If so, then your program should return the string true, otherwise it should return the string false.
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" should return true.
There are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
"""