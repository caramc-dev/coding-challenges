import re

def reverse_words(text):
    words = re.split(r'(\s+)', text)
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ''.join(reversed_words)


def reverse_words(text):
    return ' '.join(t[::-1] for t in text.split(' '))


