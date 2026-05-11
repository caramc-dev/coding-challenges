# Attmpt1:
# Very long winded and verbose:
# Went through the conditionals, accounting for the edge cases first then the different iterations
def to24hourtime(hour, minute, period):
    if period == "am" and hour == 12:
        hour = "00"
    elif period == "pm" and hour == 12:
        hour = "12"
    elif period == "am" and hour < 10:
        hour = f"0{hour}"
    elif period == "am" and hour >= 10:
        hour = str(hour)
    else:
        hour = f"{hour+12}"

    if minute <= 9:
        minute = f"0{minute}"
    else:
        minute = minute

    return f"{hour}{minute}"


# alt 2:
# Much more eloquent
# If the period is am and the hour is 12, then the hour is 0
# or if the period is pm and the hour has not yet hit 12, then ad 12 to the hour
#
# The return statement uses f string formatting that pads any number so that it will have 2 integer digits
# This forces the result to place a 0 before a number if it is single digits
def to24hourtime_1(hour, minute, period):
    if period == 'am' and hour == 12:
        hour = 0
    elif period == 'pm' and hour != 12:
        hour += 12
    return f"{hour:02d}{minute:02d}"


print(to24hourtime(10, 12, "am"))
print(to24hourtime_1(10, 12, "am"))




"""
Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either a.m. or p.m.) as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.

Notes
By convention, noon is 12:00 pm, and midnight is 12:00 am.
On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015.
"""