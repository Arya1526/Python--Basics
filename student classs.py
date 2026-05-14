class Student:

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Marks:", self.marks)

    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        print("Average Marks:", average)


s1 = Student("Arun", 101, [80, 90, 85])

s1.display_details()
s1.calculate_average()