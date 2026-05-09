def count(s):
    dict = {}
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    return dict

def count_refectored(s):
    return {char: s.count(char) for char in set(s)}


print(count_refectored('aba'))
"""
Attpt 1
Full loop used to check if a key was not already in a dictionary 
Add it if its not, increment the value by 1 if it is

Return the dictionary

Attpt 2
Used set(s)
 - which removes any duplicates and only returns one instance 
 - s.count(char) counts each instance of the char in the string s
 - x: assigns that count
 
 This is wrapped in a dictionary comprehension {key: value for ...}
 """
