# start and end by user
# start to end print using while loop

start = int(input("Enter start number = ")) # 5
end = int(input("Enter end number = ")) # 11

while start <= end:
    print(start, end=" ")
    start += 1

print(f"After while loop, start value is {start}")