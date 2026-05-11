def get_count(sentence):
    return sum(char.count(char) for char in sentence.lower() if char in "aeiou")

def get_count_refactor(sentence):
    return sum(1 for char in sentence.lower() if char in "aeiou")

"""
Attmpt 1
Convoluted way of counting chars, when this should have been simplified to 1

Attmpt 2
Simplified bu returning 1 for every instance of aeio or u in the sentence, converted to lower
"""