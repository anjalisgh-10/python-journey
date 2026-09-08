"""
Given a list of numbers, write python code using a loop o find and print
the largest element. Do not use the built-in max() function.
"""

nums = {6, -5, 4, 2, 10, 91, -75, 49, 9}

maxi = float("-inf")
for num in nums:
    if num > maxi:
        maxi = num

print(f"Maximum number = {maxi}")