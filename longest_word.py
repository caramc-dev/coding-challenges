"""
Longest Word Challenge

Challenge:
    Write a function longest_word(sentence) that finds and returns the largest
    word in a string.

Requirements:
    1. Return the longest word in the string
    2. If multiple words have the same length, return the FIRST one encountered
    3. Ignore all punctuation (keep only letters a-z, A-Z, and spaces)
    4. Assume the input string will not be empty
    5. Words are separated by spaces

Return Value:
    - Return the longest word as a string (without punctuation)

Examples:
    longest_word("bun&!! thyme")                    # → "thyme"
    longest_word("I love cats")                    # → "love" (first of equal length)
    longest_word("a beautiful sentence^&!")       # → "beautiful"
    longest_word("letter after letter!!")         # → "letter" (first occurrence)
    longest_word("confusing /:sentence:/[ this is not!!!!!!!~")  # → "confusing"

"""
import string

def longest_word(sentence):
    # use a combination of str.translate() and str.maketrans()
    # wrap the whole expression is .translate, and within that tell it what to translate - any punctuation to ""

    # maketrans takes 3arguments -
    # what character to replace (none), what to replace them with (none), characters to delete

    # Can also be written in 2 steps:
    # translator = str.maketrans("", "", string.punctuation)
    # clean_text = sentence.translate(translator)
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    word_list = sentence.split()

    # Create a variable to compare against - initially an empty string
    longest = ""

    # Loop through the words backwards, replacing is greater than or equal to
    # As it goes backwards it makes sure the firest word in the string list is replaced
    for word in word_list[::-1]:
        if len(word) >= len(longest):
            longest = word

    return longest


print(longest_word("a beautiful beautifur sentence^&!")) # → "beautiful"
print(longest_word("letter after letter!!"))   # → "letter" (first occurrence)
print(longest_word("confusing /:sentence:/[ this is not!!!!!!!~"))  # → "confusing"
