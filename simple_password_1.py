import string

def simple_password(str_param):
    if "password" in str_param.lower():
        return "false"
    elif not 7 < len(str_param) < 31:
        return "false"

    if not any(char.isdigit() for char in str_param) or not any(char.isupper() for char in str_param) or not any(x in string.punctuation for x in str_param):
        return "false"

    return "true"


