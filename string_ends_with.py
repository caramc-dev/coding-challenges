def solution(text, ending):
    return True if text.endswith(ending) else False


print(solution("samurai", "ai"))
print(solution("ninja", "ja"))
print(solution("sensei", "i"))
print(solution("sumo", "omo"))
print(solution("samurai", "ra"))
"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false
"""
