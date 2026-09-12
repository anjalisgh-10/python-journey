"""
Given a list of numbers (which may contain duplicates), write a python script
that takes an integer as input from the user and remove all occurrences of that 
integer from the list.
"""


def remove_occurence(lst, target):
    new_list = []
    for num in lst:
        if num != target:
            new_list.append(num)
    return new_list

nums = [1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 5, 6, 4, 1, 7, 8, 1]
print(remove_occurence(nums, 1))
print(f"nums = {nums}")

