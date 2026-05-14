students = {
    "Arun": 85,
    "Meera": 92,
    "Rahul": 78,
    "Anu": 95
}

highest_marks = 0
topper = ""

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        topper = name

print("Highest scorer is:", topper)
print("Marks:", highest_marks)