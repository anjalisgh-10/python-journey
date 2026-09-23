"""
Design a dictionary where each key is a student's name and the corresponding
value is a list of their marks in 3 different subjects. Calculate and prin
the total marks and average marks for eah student.
"""

students = {
    "Alice": [85, 92, 78],
    "Bob": [70, 65, 80],
    "Charlie": [90, 88, 95],
    "Diana": [60, 74, 68],
    "Ethan": [55, 48, 62],
}

for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name} has scored total of {total} marks with avg of {avg:.2f} marks")