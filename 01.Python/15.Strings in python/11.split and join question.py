text = "anjali is a good coder and is learning python"
# python learning is and coder...anjali

words_list = text.split()
words_list = words_list[::-1]
print(" ".join(words_list))