def count(s):
    dict = {}
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    return dict


"""
Full loop used to check if a key was not already in a dictionary 
Add it if its not, increment the value by 1 if it is

Return the dictionary
"""
print(count('aba'))