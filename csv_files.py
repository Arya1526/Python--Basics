import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Meera", "Arjun", "Diya"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 65]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

new_df = pd.read_csv("students.csv")

print(new_df)

print("Column Names:")
print(new_df.columns)

print("Data Types:")
print(new_df.dtypes)