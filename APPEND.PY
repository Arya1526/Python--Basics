name = input("Enter student name: ")
age = input("Enter age: ")
marks = input("Enter marks: ")

file = open("student.txt", "a")

file.write("\nName: " + name)
file.write("\nAge: " + age)
file.write("\nMarks: " + marks)
file.write("\n")

file.close()

print("Student details appended to file")