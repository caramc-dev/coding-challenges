# def number(lines):
#     return [f"{i+1}: {v}" for i, v in enumerate(lines)]

def number(lines):
    return [f"{i}: {v}" for i, v in enumerate(lines, start=1)]

print(number(["a", "b", "c"]))

"""
Used enumerate to track the index, and string position to simulate lines.

Attpt 1
+1'd on the assignment

Attmpt 2
used the start arg in enumerate itself to start the count at 1 and not hte index 0 position 
This is cleaner as the offset is handled once by enumerate, rather than on each iteration in the f string
"""


"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
"""