marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}

# for detail in marks.items():
#     # print(detail[0], detail[1])
#     sub = detail[0]
#     mark = detail[1]
#     print(sub, mark)

for sub, mark in marks.items():
    print(f"sub = {sub} and mark = {mark}")