def validate_pin(pin):
    return True if pin.isdigit() and (len(pin) == 4 or len(pin) == 6) else False


def validate_pin_alt(pin):
    return len(pin) in (4, 6) and pin.isdigit()


print(validate_pin("1"))
print(validate_pin("12"))
print(validate_pin("123"))
print(validate_pin("1234"))
print(validate_pin("123455"))
print(validate_pin("12346j"))
print(validate_pin("123p"))
print()
print(validate_pin_alt("1"))
print(validate_pin_alt("12"))
print(validate_pin_alt("123"))
print(validate_pin_alt("1234"))
print(validate_pin_alt("123455"))
print(validate_pin_alt("12346j"))
print(validate_pin_alt("123p"))

"""
Attmpt1
Checked all conditions and explicitly returned True to False values

Attmpt2
Reviewing others solution, this uses the fact that True will be returned if the conditionals match, flase otherwise


ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""