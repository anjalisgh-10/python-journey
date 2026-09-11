nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

# print(100 in nums)
# print(2 in nums)

target = int(input("Enter target = ")) #10

if target in nums:
    nums.remove(target)
    print(f"nums = {nums}")
else:
    print("Cannot remove taarget, target does not exists")