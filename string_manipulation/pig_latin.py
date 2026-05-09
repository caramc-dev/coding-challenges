import string


def pig_it(text):
    text_list = []
    for word in text.split(" "):
        if not word in string.punctuation:
            text_list.append(f"{word[1:]}{word[0]}ay")
        else:
            text_list.append(word)

    return " ".join(text_list)


"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

"""
The solution splits the string into a list of words, check if each word is a 
punctuation mark, and if not, rotate the first letter to the end and 
append "ay". T
I chose punctuation over isalpha() as that would fail edge cases where there are digits.
isalpha() would not account if there were any numbers, only checking it the word is all letters
"""

