def accum(str):
    mumble = []
    for index, st in enumerate(str):
        if index == 0:
            mumble.append(st.upper())
        else:
            mumble.append(''.join([st.upper(), st*index]))

    return '-'.join(mumble)


print(accum("abcd"))


"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""
