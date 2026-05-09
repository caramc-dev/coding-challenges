def create_phone_number_1(nums):
    phone_num = ["("]
    for index, num in enumerate(nums):
        if index == 2:
            num = f"{num}) "
            phone_num.append(str(num))
        elif index == 5:
            num = f"{num}-"
            phone_num.append(str(num))
        else:
            phone_num.append(str(num))

    return ''.join(phone_num)


def create_phone_number_refactored(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)



"""
Thought process for _1:
Loop through the list using enumerate to capture formatting by adding to a new list, starting with the opening parenthesis.
I used specific index points to append with formatting rules, and the else to capture when just a number was needed.

Process for refactor - on seeing the other solutions, I discovered a different string formatting method - .format()
.format(*n) unpacks a list of numbers in 1 go, and the curly braces serve as placeholders.
This maps on a like for like basis, index position[0] being in the first {} and so on.
In this particular problem, it simplified the looping logic and reduced the code to one line.
"""


"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""

