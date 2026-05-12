def validate_phone(phone_number):
    # The phone number must have exactly 12 chars based, so initial check discounts the wrong length
    if not len(phone_number) == 12:
        return False

    # 3 successive calls to check to reject any with an invalid starting char/pattern
    if phone_number.startswith("1") or phone_number.startswith("0") or phone_number.startswith("911"):
        return False

    # Check that duplicates doesn't appear based on the index position.
    # Starting str index 0 this begins at index positon 4 and includes 7 as 6 is non-inclusive

    # Create a set of the middle 3 numbers and if that only returns a length of 1, it means they are all the same
    # If that is the case, then return False.
    if len(set(phone_number[4:7])) == 1:
        return False

    # Create arrays for where the numbers and hyphens should be
    nums = [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]
    hyphens = [3, 7]

    # Loop through using enumerate, matching the index position
    # If the index position being checked is in the nums array and is not a digit, return false
    # If the index position being checked is in the hyphens array and is not a hyphen, return false
    for index, char in enumerate(phone_number):
        if index in nums:
            if not char.isdigit():
                return False
        if index in hyphens:
            if not char == "-":
                return False

    # If none of the invalidating conditions are hit, then return true
    return True



# Test cases
print(validate_phone("212-4567890"))  # False (wrong format)
print(validate_phone("123-456-7890"))  # False (area code starts with 1)
print(validate_phone("911-456-7890"))  # False (area code is 911)
print(validate_phone("212-555-3456"))  # False (middle section has all same digits)
print(validate_phone("212-456-7890"))  # True


"""
Phone Number Validator

Write a function called validate_phone that checks if a string is a valid phone number
according to the following rules:

1. The phone number must be in the format: XXX-XXX-XXXX (3 digits, hyphen, 3 digits, hyphen, 4 digits)
2. All characters except hyphens must be digits
3. The first digit cannot be 0 or 1 (US area codes don't start with these)
4. The first three digits (area code) cannot be 911
5. The middle three digits cannot be all the same digit (e.g., 555)

Your function should return True if all conditions are met, and False otherwise.
"""