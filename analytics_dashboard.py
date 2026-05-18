import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name": ["Asha", "Rahul", "Meera", "Arjun", "Diya",
             "Kiran", "Anu", "Vivek", "Sneha", "Rohan"],

    "Department": ["CS", "IT", "CS", "ECE", "IT",
                   "ECE", "CS", "IT", "ECE", "CS"],

    "Marks": [85, 90, 78, 92, 88,
              75, 95, 81, 69, 87],

    "Attendance": [82, 91, 70, 88, 76,
                   65, 95, 72, 68, 80]
}

df = pd.DataFrame(data)

print("Summary Statistics")
print(df.describe())

df["Pass/Fail"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

df.to_csv("cleaned_students.csv", index=False)

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

department_count = df["Department"].value_counts()

plt.pie(department_count,
        labels=department_count.index,
        autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()

plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

print("Final Analysis Report")
print("Total Students:", len(df))
print("Average Marks:", np.mean(df["Marks"]))
print("Highest Marks:", np.max(df["Marks"]))
print("Lowest Marks:", np.min(df["Marks"]))

print("Students Below 75% Attendance")
print(df[df["Attendance"] < 75])