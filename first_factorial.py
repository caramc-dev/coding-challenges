import math


def first_factorial(num):
    return math.factorial(num)


def first_factorial_long(num):
    total = 1
    for n in range(1, num + 1):
        total *= n
    return total


def first_fact_recursion(num):
    if num <= 1:
        return 1
    else:
        return num * first_fact_recursion(num-1)


print(first_factorial_long(8))
print(first_factorial(8))
print(first_fact_recursion(8))


"""
Question: First Factorial

Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. 
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
For the test cases, the range will be between 1 and 18 and the input will always be an integer.
"""

"""
Attpmt1:
Import math and apply the factorial method. 
This is inbuilt in the library, so whilst it could test my arithmatic, this option is widely used.

Attmpt 2:
Solved for the event that math import wasn't allowed. 
starting with a base of 1, as this is the lowest possible outcome, I using range to step through the increments.
Start at index pos 1 (number 2) as 1 is accounted for and n+1 that increases so is inclusive of n, adding to the total


Solution 3 
Found from others and noted this uses recursion
The product of the first iteration is used as the argument by recalling the same function in decreasing increments
Returns 1 if only 1 is input as this will always be 1,  and acts as a way to break the recursive loop 
"""