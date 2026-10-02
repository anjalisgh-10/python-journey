"""
Take a list of input (comma separated). Split them, sort them
alphabetically, and join them back with " | " as separator.
"""
names_input = "Charlie, Alice, Ethan, Bob, Diana"
words = names_input.split(",")
print(" | ".join(words))