text = "Programming"

# in \ not in


# print("p" in text)
# print("P" in text)
# print("z" not in text)
# print("m" not in text)
# print("gram" not in text)

# total = 0
# for ch in text:
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#         total += 1
# print(total)   
total = 0
for ch in text:
    if ch in "aeiouAEIOU":
        total += 1
print(total)