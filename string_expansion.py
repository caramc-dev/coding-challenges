# Attpt 1:
# Loop through the chars in the string
# If a digit is encountered, it is entered into the multiplier.
# This is replaced if the next character is not a letter
# When the next char is a letter, and there is a multiplier present it multiplies and adds to the list
# If no numbers are encountered, the string is returned rejoined.
def string_expansion(str):
    expanded = []
    multiplier = None
    for char in str:
        if char.isdigit():
            multiplier = int(char)
        elif char.isalpha() and multiplier is not None:
            expanded.append(char * multiplier)
        else:
            expanded.append(char)

    return "".join(expanded)


print(string_expansion('3D2a5d2f'))
print(string_expansion('abcde'))
print(string_expansion('1111'))
print(string_expansion('mmmmmmmjjjiiiikaa'))
print(string_expansion('81eF8dga4c7BBeE5'))



"""Given a string that includes alphanumeric characters ("3a4B2d") return the expansion of that string: 
The numeric values represent the occurrence of each letter following that numeric value. There should be no numeric characters in the final string.


Notes
The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears
If there are multiple consecutive numeric characters, only the last one should be used (ignore the previous ones)
Empty strings should return an empty string.
Your code should be able to work for both lower and capital case letters.

"3D2a5d2f"  -->  "DDDaadddddff"    # basic example: 3 * "D" + 2 * "a" + 5 * "d" + 2 * "f"
"3abc"      -->  "aaabbbccc"       # not "aaabc", nor "abcabcabc"; 3 * "a" + 3 * "b" + 3 * "c"
"3d332f2a"  -->  "dddffaa"         # multiple consecutive digits: 3 * "d" + 2 * "f" + 2 * "a"
"abcde"     -->  "abcde"           # no digits
"1111"      -->  ""                # no characters to repeat
""          -->  ""                # empty string
"""