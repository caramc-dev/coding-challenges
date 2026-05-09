def expanded_form(num):
    nums = []
    counter = len(str(num))
    for n in str(num):
        counter -= 1
        if n != "0":
            nums.append(int(n) * (10 ** (counter)))

    return ' + '.join(str(x) for x in nums)


print(expanded_form(1206))


"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.

For example: 4,265 = 4 × 1,000 + 2 × 100 + 6 × 10 + 5 × 1
"""