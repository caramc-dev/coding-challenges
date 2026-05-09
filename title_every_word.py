def to_jaden_case(str):
    return " ".join(s.capitalize() for s in str.lower().split(" "))


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))