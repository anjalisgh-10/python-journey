marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
    1: 10
}
# print(marks["science"])
# print(marks[1])
# print(marks["abc"])
print(marks.get("science", -1))