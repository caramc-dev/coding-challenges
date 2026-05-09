def capitalize(s, index):
    return "".join(v.upper() if i in index else v for i, v in enumerate(s))


print(capitalize("abcdef",[1,2,5]))


"""
Used enumerate inside a list comprehension to iterate over the characters with the index (i) and values (v)
Conditional branching applied so that if the index (i) appeared in the parameter index (index) then upper case it.
Else return the value.
The list is in lower case according to the challenge so converting the else to .lower() was unnecessary

"""



"""
Given a string of lowercase letters and an array of integer indices, capitalize all letters at the given indices. If an index is beyond the string, it should be ignored.

Examples:
"abcdef", [1,2,5]     ==> "aBCdeF"
"abcdef", [1,2,5,100] ==> "aBCdeF" // There is no index 100.
"""