"""
Unique Words Count

Take a paragraph as input. Print the count of unique words in it
(case insensitive).
"""


def count_unique_words(paragraph: str):
    words = paragraph.split()
    return len(set(words))

paragraph = "Python is great and python is fun and learning Python is the best"
print(count_unique_words(paragraph))