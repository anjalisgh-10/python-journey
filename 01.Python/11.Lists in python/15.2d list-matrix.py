# 3 x 3
matrix = [
    [4, 8, 1],
    [9, 7, 2],
    [5, 6, 0],
]
total = 0
for i in range(0, 3):
    for j in range(0, 3):
        total = total + matrix[i][j]
        # print(matrox[i][j])
    # print()

print(total)

# print(matrix[0])
# print(matrix[1])
# print(matrix[2])