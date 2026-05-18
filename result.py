class Student:

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def find_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "Fail"

    def display_result(self):
        print("\nStudent Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.find_grade())


students = []

s1 = Student("Arun", 101, [80, 90, 85])
s2 = Student("Meera", 102, [95, 92, 98])

students.append(s1)
students.append(s2)

for student in students:
    student.display_result()