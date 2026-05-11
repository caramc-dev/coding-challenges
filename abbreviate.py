def abbrev_name(name):
    return ".".join([char.upper()[0] for char in name.split(" ")])


print(abbrev_name("sam Harris"))


"""
Attmpt 1
list comprehension to return the index[0] position as upper() when splitting on a space. 
join using '.' to meet the required format.  

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""