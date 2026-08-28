"""
Ask a number from the user, and print all the factors. 

Enter a number = 10
1 2 5 10

Enter a number = 100
1 2 4 5 10 20 25 50 100
"""

num = int(input("Enter num ="))
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1