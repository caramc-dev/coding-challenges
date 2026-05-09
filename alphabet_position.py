def alphabet_position(text):
    return " ".join(str(ord(char) - 96) for char in text.lower() if char.isalpha())


print(alphabet_position("hello there"))




"""
This took a few iterations working out the logic. I initially forgot to .lower() the text.
This messed up the position of capitals.

Attpt1 -
def alphabet_position(text):
    return " ".join([(ord(char) - 96) if char.isalpha() else char for char in text.split(" ")])

Split but didn't need to do this, also split on a character.

Attpt2 -
I then changed to just iterating of the text but added an if else, which accounted for the space:

def alphabet_position(text):
    return " ".join(str(ord(char) - 96) if char.isalpha() else " " for char in text.lower())

I realised htere should be nothing for the else so moved the if to the end of the phrase

"""


"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""