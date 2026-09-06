"""
Create a list of 5 of your favourtie movies. Print the first, last,
and middle movie from your list using both positive ans negatiive 
indexing where approprites.

"""

marks = [54, 21, 56, 76, 787, 453, 432, 43, 93, 11, 32, 1, 54, 65765, 98]

n = len(marks)
print(f"First element = {marks[0]}")
print(f"Last element = {marks[-1]}")
print(f"Middle element = {marks[n//2]}")