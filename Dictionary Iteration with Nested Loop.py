students = {
    "Alice": [85, 90, 95],
    "Bob": [70, 80, 75],
    "Charlie": [88, 92, 85]
}

for name, marks in students.items():
    total = 0
    for mark in marks:
        total += mark
    print(f"{name} average = {total / len(marks):.2f}")
# Loops through dictionary + list inside dictionary.