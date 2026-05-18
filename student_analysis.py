import pandas as pd

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

topper = df[df["Marks"] == df["Marks"].max()]
print("Topper:")
print(topper)

print("Average Marks Department-wise:")
print(df.groupby("Department")["Marks"].mean())

print("Students with Attendance below 75%:")
print(df[df["Attendance"] < 75])

print("Students Sorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))