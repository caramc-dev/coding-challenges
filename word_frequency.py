import string


def analyze_text(text):
    # Checks if the parameter (text) is a string
    if not isinstance(text, str):
        return "String not provided"

    # Convert the text to lowercase & remove punctuation
    text = text.lower().replace(string.punctuation, "")

    # Split the text into individual words
    word_list = text.split()

    # Count the frequency of each word
    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return max(word_dict, key=word_dict.get)


# Test cases
print(analyze_text("The quick brown fox jumps over the lazy dog."))  # "the"
print(analyze_text("Hello world! Hello Python. Python is fun."))  # "hello"
print(analyze_text("a a a b b c"))  # "a"
print(analyze_text("Numbers123 and letters456 should be treated as words."))  # "numbers123"
print(analyze_text(123))

"""
Word Frequency Analyser

Write a function called analyze_text that processes a text string and returns the most frequent word.

Your function should:
1. Take a string parameter (text) - checks 
2. Convert the text to lowercase
3. Remove all punctuation marks
4. Split the text into individual words
5. Count the frequency of each word
6. Return the word that appears most frequently

"""

