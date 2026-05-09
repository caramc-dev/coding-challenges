def divisors(n):
    return len([divisor for divisor in range(1, n+1) if n % divisor == 0])


"""
Count the number of divisors of a positive integer n.
Random tests go up to n = 500000, but fixed tests go higher.
Examples (input --> output)

4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30

Note you should only return a number, the count of divisors.
The numbers between parentheses are shown only for you to see which numbers are counted in each case.
"""

"""
I used list comprehension to loop through the list of numbers from 1 to n (inclusive of n).
It returns the length of the new list, where a number is added if it divides into n with no remainder
(n % divisor == 0).

The range starts at 1 to and ends at n+1 to make inclusive of n itself since Python's range() excludes the end value.
"""




"""
My initial solution:
Started divisors with 1 as the number as they will all have 1
I then started the range at 1 to n
This did not not require the +1 as the n in range was already accounted for
Increments increase everytime a number divides into n with no remainder

Refactored to 1 liner to work on list comprehension

def divisors(n):
    divisors = 1
    for i in range(1, n):
        if n % i == 0:
            divisors += 1
    return divisors
"""


